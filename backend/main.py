import requests
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/codellama/CodeLlama-7b-Instruct"  # example
HUGGINGFACE_API_TOKEN = "your_huggingface_api_token_here"

headers = {"Authorization": f"Bearer "}

@app.post("/generate/")
async def generate_code(prompt: str = Form(...)):
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 300}}
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return {"code": result[0]['generated_text']}
    else:
        return {"error": "Failed to generate code", "details": response.text}
