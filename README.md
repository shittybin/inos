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
  "prompt": "Design a futuristic WebOS inspired by Windows XP, blending retro aesthetics with modern technology. The interface should include an AI assistant, a classic-style file manager, a working notepad app, and a paint application. The file manager should visibly show saved text and image files from the notepad and paint apps. Use a nostalgic color scheme (e.g., blue and silver tones) with glossy buttons, pixel-style icons, and soft shadows. The overall vibe should be a perfect mix of early 2000s UI and futuristic UX — clean, vibrant, functional, and slightly playful."
}
LINK OF WHAT INOS GENERATED: 
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
