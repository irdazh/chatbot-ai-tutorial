import requests
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

# save response as pretty json to file
with open("groq_models.json", "w") as f:
    f.write(response.text)
    

# print(response.json())