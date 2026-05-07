import os 
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# Load credentials
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

# Define request model --> from str to history
class ChatRequest(BaseModel):
    # message: str
    history: list

@app.post("/chat")
async def chat_with_groq(request: ChatRequest):
    # trimming the history
    limited_history = request.history[-6:] if len(request.history) > 6 else request.history

    # Safety check but. Hmm. IDK haha. 
    total_chars = sum(len(msg['content']) for msg in limited_history)
    if total_chars > 5000:
        raise HTTPException(status_code=400, detail="Conversation context too large")
    
    try: 
        # secret system instructions
        messages = [{"role":"system", "content":"You are a professional photography assistant. Keep your memory sharp! And only talk about photography!"}]
        
        # append user messages from history
        messages.extend(limited_history)

        # response from Groq
        response = client.chat.completions.create(
            model = 'llama-3.3-70b-versatile',
            messages = messages,
            temperature = 0.7,
            # max_tokens = 500
        ) 
        return {'response':response.choices[0].message.content}
    
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))