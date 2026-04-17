# 🔬 AI Research Assistant Swarm

A high-intelligence, multi-agent research platform designed to automate deep-dive subject matter investigations. This system utilizes the **Swarm** design pattern to coordinate specialized agents, transforming a simple topic into an executive-grade research report.

---

## 🤖 The Research Swarm

This platform employs a sequential handing-off architecture with four distinct agents:

| Agent | Responsibility |
| :--- | :--- |
| **Triage Agent** | The "Director" that generates search queries, focus areas, and a structured research plan. |
| **Query Rewriting Agent** | Refines raw topics into 5–8 diverse and precise search vectors. |
| **Research Agent** | The "Investigator" that searches the web and saves key insights into persistent state. |
| **Editor Agent** | The "Synthesizer" that compiles all facts into a structured, cited markdown report. |

---

## ✨ Features

- **Autonomous Tooling:** Agents use a custom `save_important_fact` tool to build a verified knowledge base on-the-fly.
- **Progressive UI:** Real-time visibility into the research plan, collected facts, and report generation progress.
- **Deep Web Grounding:** Integrated with **OpenAI WebSearchTool** for high-quality information gathering.
- **Structured Outputs:** Uses Pydantic for rigid `ResearchPlan` and `ResearchReport` schemas to ensure consistent results.
- **Export Ready:** One-click download of the final report in Markdown format.

---

## 🛠️ Tech Stack

- **Large Language Models:** GPT-4o & GPT-4-Turbo
- **Framework:** OpenAI Swarm / Runner Logic
- **UI:** Streamlit (Custom progress-tracking dashboard)
- **Data Validation:** Pydantic

---

## 🚀 How to Run

1.  **Configure Environment:**
    Set `OPENAI_API_KEY` in the script or your environment.
2.  **Launch Dashboard:**
    ```bash
    streamlit run researchagent.py
    ```
3.  **Start Research:** Enter any topic (e.g., "Future of Solid State Batteries") and watch the swarm work.

---

<div align="center">
    <b>Autonomous Intelligence for the Modern Researcher</b>
</div>
