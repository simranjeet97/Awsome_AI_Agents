# ⚖️ AI Legal Team Agents

A sophisticated, collaborative multi-agent platform designed for high-stakes legal document analysis and research. This system simulates a professional legal team, where specialized AI agents cooperate to review contracts, assess risks, and ensure regulatory compliance.

---

## 👨‍⚖️ The Legal Swarm

By combining **Agno** with **Gemini**, this project orchestrates four distinct legal experts:

| Agent | Role | Focus Area |
| :--- | :--- | :--- |
| **LegalAdvisor** | Research Agent | Finds and cites relevant legal cases, regulations, and precedents. |
| **ContractAnalyst** | Analysis Agent | Reviews clauses for risks, obligations, and potential ambiguities. |
| **LegalStrategist** | Strategy Agent | Provides actionable risk assessments and compliance recommendations. |
| **Team Lead** | Orchestrator Agent | Synthesizes all insights into a professional, cohesive legal report. |

---

## ✨ Features

- **Knowledge Base RAG:** Processes PDFs into a persistent **ChromaDB** vector database with `GeminiEmbedder`.
- **Dynamic Analysis Types:** Choose from Contract Review, Legal Research, Risk Assessment, or Compliance Checks.
- **Collaborative Logic:** The Team Lead merges independent findings from the Researcher, Analyst, and Strategist.
- **Source Referencing:** All agents are instructed to extract data from the knowledge base and cite specific document sections.
- **Hybrid Search:** Uses **DuckDuckGo** to supplement internal knowledge with current legal references.

---

## 🛠️ Tech Stack

- **Model:** Gemini 2.0 Flash
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **Vector DB:** ChromaDB (Persistent)
- **Document Processing:** PDFKnowledgeBase, PDFReader, DocumentChunking
- **UI:** Streamlit (Custom "Legal-Scale" Theme)

---

## 🚀 How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Launch the Dashboard:**
    ```bash
    streamlit run legal_team.py
    ```
3.  **Upload & Analyze:**
    - Enter your Google API Key in the sidebar.
    - Upload a legal PDF.
    - Select an analysis type and click "Analyze".

---

<div align="center">
    <b>Enterprise-Grade Legal Intelligence Powered by AI</b>
</div>
