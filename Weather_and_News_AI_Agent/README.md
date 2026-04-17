# 🌤️ Daily Briefing Agent (Google ADK)

A sophisticated conversational AI agent built with the **Google Agent Development Kit (ADK)** that provides live weather updates, global news headlines, and a daily dose of humor. This project demonstrates high-fidelity **Agent Skills**—both file-based and inline—orchestrated by Gemini 2.5 Flash.

---

## ✨ Features
- **Weather Skill (File-Based)**: Fetches real-time atmospheric data from `wttr.in`. Features an intelligent city alias system (`CITIES.md`) to resolve historical or regional names like "Bombay" or "Bangalore" silently.
- **News Skill (Inline)**: A dynamic summarizer using `NewsAPI.org`. Provides deep support for categories like Technology, Business, Science, and Sports (with custom logic for Cricket and Football).
- **Joke-of-the-Day Skill**: A demonstration of instruction-only skills using L3 reference content (`FORMATS.md`) to generate creative outputs without external API calls.
- **Progressive Disclosure**: High-level instructions are always resident in memory, while detailed formatting guides are loaded dynamically via ADK's skill system to maintain a large context window efficiency.

---

## 🏗️ Architecture

```mermaid
graph TD
    User([User Query]) --> Agent[ADK Agent: Gemini 2.5 Flash]
    Agent --> Toolset[SkillToolset]
    
    subgraph Skills
        Toolset --> Weather[Weather Skill: File-Based]
        Toolset --> News[News Skill: Inline]
        Toolset --> Joke[Joke Skill: Instruction-Only]
    end
    
    subgraph Data Sources
        Weather --> WAPI[wttr.in API]
        News --> NAPI[NewsAPI.org]
    end
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10+
- [Google AI Studio API Key](https://aistudio.google.com/apikey)
- [NewsAPI.org Key](https://newsapi.org/register)

### 2. Setup
```bash
# Clone and enter directory
cd Weather_and_News_AI_Agent

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root:
```env
GOOGLE_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_news_api_key
```

### 4. Run the Agent
**Web UI:**
```bash
adk web --port 8002 .
# Open http://localhost:8002 in your browser
```

**CLI Tool:**
```bash
adk run .
```

---

## 🛠️ Project Structure
```text
Weather_and_News_AI_Agent/
├── daily_briefing_agent/     # Agent Discovery Directory
│   ├── agent.py              # Main logic, Inline Skills & Tool Handlers
│   ├── __init__.py           # Required for ADK discovery
│   └── skills/               
│       └── weather-skill/    # File-based skill
│           ├── SKILL.md      # L1/L2 Instructions
│           └── references/   # L3 Progressive Disclosure docs
├── .env                      # API Secrets
└── requirements.txt          # Python Dependencies
```

---

<div align="center">
    <b>Real-Time Grounded Intelligence Powered by Google ADK</b>
</div>
