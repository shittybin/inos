````markdown
# 🖥️ AI Desktop OS Generator — INOS

This is the AI backend that powers **AI Desktop OS Generator**, a web tool that builds interactive desktop-style environments from plain text prompts. Just say something like:

> “I want a retro hacker OS with a terminal and a code editor.”

And instantly get a custom layout with draggable windows, themes, and apps.

## ✨ Features

- 🔗 OpenAI GPT-powered layout generation
- ⚙️ Express.js backend with JSON output
- 🌈 Customizable themes and app types
- 📦 Easy to integrate with any frontend

## 🚀 API Endpoint

`POST /generate-layout`

### Request body:
```json
{
  "prompt": "A futuristic OS with AI assistant and file manager"
}
````

### Response:

```json
{
  "theme": "cyberpunk",
  "apps": [
    { "name": "AI Assistant", "type": "chat" },
    { "name": "File Manager", "type": "explorer" }
  ]
}
```

## 🛠️ Tech Stack

* Node.js + Express
* OpenAI GPT-4
* dotenv for environment secrets
* CORS enabled for frontend integration

## 🧪 How to Run

```bash
git clone https://github.com/shittybin/inos.git
cd inos
npm install
echo "OPENAI_API_KEY=your_key_here" > .env
node index.js
```

## 📌 Coming Soon

* 🎨 Layout preview generator
* 🔗 Shareable link storage
* 🖱️ Drag-and-drop UI via frontend

---

Made with ☕️!
