import os 
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# Load credentials
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

# Define request model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_groq(request: ChatRequest):
    # Security len check
    if len(request.message) > 1000:
        raise HTTPException(status_code=400, detail="Message too long")

    try: 
        # Secure prompting using system role
        response = client.chat.completions.create(
            model = 'llama-3.3-70b-versatile',
            messages = [
                {"role":"system", "content":"You are a professional assistant. Stay polite and concise, and only talk about anything related to photography."},
                {"role":"user", "content":request.message}
            ],
            temperature = 0.7,
            max_tokens = 500
        )

        return {'response':response.choices[0].message.content}

    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))





























## Berisi sampah below here. 
# api_key = os.getenv("GROQ_API_KEY")

# def chat_with_groq(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
        
#     return response['choices'][0]['message']['content'].strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit", 'bye']:
#             print("Exiting chat. Goodbye!")
#             break
#         response = chat_with_groq(user_input)
#         print(f"Groq: {response}")







# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def chat_with_groq(user_input):
#     response = client.chat(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_input}
#         ]
#     )
#     return response['choices'][0]['message']['content']

# if __name__ == "__main__":
#     user_input = input("You: ")
#     response = chat_with_groq(user_input)
#     print(f"Groq: {response}")


