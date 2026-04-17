# 🤔 Agentic RAG with Gemini Flash Thinking

A state-of-the-art Agentic RAG system that leverages **Gemini 2.0 Flash Thinking** for deep reasoning over complex documents. This agent doesn't just retrieve; it *thinks* through the context to provide precise, cited, and search-grounded answers.

---

## ✨ Features

- **Gemini Thinking Model:** Utilizes `gemini-2.0-flash-thinking-exp` for superior reasoning over large context windows.
- **Multi-Source Ingestion:** Seamlessly processes **PDFs** and **Web URLs** into a unified knowledge base.
- **Query Rewriting:** An autonomous **Query Rewriter Agent** reformulates user questions to be search-friendly and precise.
- **Exa Web Search:** Deep integration with [Exa.ai](https://exa.ai) for retrieving "clean" neural web results instead of just keyword-based links.
- **Vector Intelligence:** Persistent **ChromaDB** storage with custom monkey-patching for high stability on macOS.
- **Citations:** Every answer focus on relevant details and direct citations from the uploaded sources.

---

## 🛠️ Tech Stack

- **Models:** Gemini 2.0 Flash Thinking / exp
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **Search Tool:** Exa AI Tools
- **Embeddings:** Google Gemini Embeddings (`models/embedding-001`)
- **Vector DB:** ChromaDB (with `hnswlib` optimizations)
- **UI:** Streamlit

---

## 🚀 How to Run

1.  **Install dependencies:**
    ```bash
    pip install streamlit agno google-generativeai langchain-community bs4 chromadb hnswlib
    ```
2.  **Acquire API Keys:**
    - [Google AI Studio](https://aistudio.google.com/) (Gemini Key)
    - [Exa AI Dashboard](https://dashboard.exa.ai/) (Exa Key)
3.  **Run the Agent:**
    ```bash
    streamlit run agentic_rag.py
    ```

---

## 🧠 Core Pipeline

| Step | Agent / Tool | Rationale |
| :--- | :--- | :--- |
| **Ingestion** | `PyPDFLoader` / `WebBaseLoader` | Extracting raw intelligence from unstructured data. |
| **Search** | `ExaTools` | Fetching real-time context from the open web as a fallback. |
| **Reasoning** | `Gemini RAG Agent` | Synthesizing final answers using the Thinking model for maximum accuracy. |

---

<div align="center">
    <b>Advanced Agentic Reasoning powered by Gemini & Agno</b>
</div>
