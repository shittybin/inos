from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from huggingface_hub import InferenceClient
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = InferenceClient(
    provider="fireworks-ai",
    api_key="XYZ",  # change it i wont be giving mine
)

OUTPUT_DIR = "generated"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "output.html")

@app.post("/generate/", response_class=HTMLResponse)
async def generate_code(prompt: str = Form(...)):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a highly skilled, professional web developer and content creator specializing in generating clean, modern, and fully functional websites. "
                "Always respond by providing a complete, valid HTML5 document that includes all required elements such as <!DOCTYPE html>, <html>, <head>, <meta> tags, "
                "<title>, <body>, and any necessary CSS or JavaScript inline or linked. Your generated code must be syntactically correct, well-formatted, and ready to be "
                "rendered directly in a web browser without any missing parts or broken tags. Make sure to include accessibility best practices, semantic HTML elements, and "
                "responsive design principles whenever relevant. Do not provide partial snippets or incomplete code — only full, production-quality HTML pages."
            )
        },
        {"role": "user", "content": prompt}
    ]

    completion = client.chat.completions.create(
    model="Qwen/Qwen3-235B-A22B",
    messages=messages,
    max_tokens=4096,  # or 8192 if supported
    temperature=0.7
)

    
    generated_code = completion.choices[0].message.content
    
    # Save generated code to output.html
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(generated_code)
    
    # Return generated HTML code as response to visualize immediately
    return HTMLResponse(content=generated_code, status_code=200)

@app.get("/view/", response_class=HTMLResponse)
async def view_generated_output():
    if os.path.exists(OUTPUT_FILE):
        return FileResponse(OUTPUT_FILE, media_type="text/html")
    return HTMLResponse("<h2>No generated output found. Please generate first!</h2>", status_code=404)
