import os
from groq import Groq # Example using Groq

client = Groq(api_key="YOUR_FREE_KEY_HERE")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Explain Docker like I'm five."}
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

