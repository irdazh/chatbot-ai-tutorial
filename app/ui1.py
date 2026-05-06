import streamlit as st
import requests
import time
import os

# from dotenv import load_dotenv
# load_dotenv()

API_BASE_URL = os.getenv("API_URL","http://localhost:8000")

st.set_page_config(page_title = "Groq Photography Chatbot", page_icon=":camera:", layout="wide")
st.title("Groq Photography Chatbot")


# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# User Input
if prompt := st.chat_input("How can I help you today? Ask me anything about photography! To exit, just say 'bye'."):

    # If input including bye, exit the chat
    if prompt.lower() in ["exit", "quit", 'bye']:
        st.write("Exiting chat. Goodbye!")
        st.session_state.messages = []  # Clear chat history
        with st.spinner("Clearing chat..."): # Animate and delay for better UX
            time.sleep(2) 
        st.rerun()  # Refresh the app to clear the UI
    
    # Add user message to UI
    st.session_state.messages.append(
        {"role": "user", "content":prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Call the backend API 
    with st.chat_message("assistant"):
        try:
            # Point to localhost for now
            res = requests.post(f"{API_BASE_URL}/chat", json={"message": prompt})
            answer = res.json().get("response")
            st.markdown(answer)

            # Add assistant message to UI
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception as e:
            st.error(f"Failed to connect to the brain! Error: {e}")
    