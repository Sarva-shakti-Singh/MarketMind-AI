# 🚀 AI Marketing Automation Dashboard

Full-stack AI-powered marketing automation platform with autonomous AI agents, real-time analytics, workflow orchestration (N8N/Zapier), and AI-driven insights — all in a single Streamlit app that runs instantly in VS Code.

## ✨ Features

- **📊 Real-time Dashboard** — campaigns, leads, SEO, KPIs
- **🤖 6 Autonomous AI Agents** — keyword research, SEO trends, campaign health, content ideas, lead scoring, automated reporting
- **🔍 SEO Tracker** — keyword rankings, volume vs difficulty, AI trend analysis
- **📈 Campaign Monitor** — CTR, CPC, conversion rate, bounce rate, alerts
- **🎯 AI Lead Scoring** — automatic high/medium/low classification
- **✍️ Content Generator** — blog titles, ad copy, SEO meta, social captions, full posts
- **📑 Auto Reports** — AI-generated weekly executive reports (download as Markdown)
- **💬 AI Assistant** — chat with your marketing AI
- **⚡ Workflows** — fire N8N / Zapier webhooks for any event
- **⚙️ Settings** — manage API keys & data

## 🚀 Quick Start (VS Code)

1. **Unzip** and open the folder in VS Code
2. **Add your free Gemini API key:**
   - Copy `.streamlit/secrets.toml.example` → `.streamlit/secrets.toml`
   - Get a free key at https://aistudio.google.com/apikey and paste it
3. **Run:**
   - Windows: double-click `run.bat`
   - Mac/Linux: `chmod +x run.sh && ./run.sh`
   - Or press **F5** in VS Code

The app opens at http://localhost:8501

## 🛠 Tech Stack

- **Frontend:** Streamlit + Plotly
- **Backend:** Python (single-process, SQLite)
- **AI:** Google Gemini (free tier)
- **Database:** SQLite (auto-seeded with demo data)
- **Automation:** N8N / Zapier webhooks
- **Optional:** OpenAI, Google Ads API, SERP API, HubSpot, SendGrid

## 📁 Structure

```
genai-marketing/
├── app.py                  # Main entry point
├── pages/                  # 10 Streamlit pages
├── agents/                 # AI agent implementations
├── utils/                  # DB, AI wrapper, state
├── data/                   # SQLite DB (auto-created)
├── .streamlit/             # Theme + secrets
├── .vscode/                # F5 debugger config
├── run.bat / run.sh        # One-click launchers
└── requirements.txt
```

## 🔌 Workflow Automation Setup

**Zapier:** New Zap → Trigger: *Webhooks by Zapier (Catch Hook)* → copy URL → paste in **⚡ Workflows** page.

**N8N:** Add *Webhook* node → POST → copy production URL → paste in **⚡ Workflows** page.

## 📝 Resume Description

> Developed a full-stack AI Marketing Automation Dashboard using Python, Streamlit, Google Gemini, SQLite, N8N, and Zapier — featuring 6 autonomous AI agents for SEO monitoring, keyword research, campaign health analysis, content ideation, lead scoring, and automated executive reporting with real-time analytics and workflow orchestration.



 
