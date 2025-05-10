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
