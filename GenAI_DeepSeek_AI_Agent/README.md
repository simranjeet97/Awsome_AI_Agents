# 🐋 DeepSeek Local RAG Reasoning Agent

A powerful, privacy-focused RAG agent that runs entirely on your local machine using **DeepSeek-R1** (via Ollama). This agent is designed for deep investigation and reasoning over sensitive documents without sending your data to external LLM providers.

---

## ✨ Features

- **DeepSeek Reasoning:** Powered by **DeepSeek-R1:1.5b**, a model specifically optimized for chain-of-thought reasoning.
- **Privacy First:** Entire reasoning chain happens locally via Ollama.
- **Hybrid Search:** Combines local **ChromaDB** document retrieval with a **DuckDuckGo** web search fallback.
- **Clean Interface:** Filtering logic to remove chain-of-thought `<think>` blocks, presenting only the final refined answer to the user.
- **Document Memory:** Remembers processed PDFs and URLs within a session to avoid redundant processing.

---

## 🛠️ Tech Stack

- **Model:** [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) (Local via Ollama)
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **Embeddings:** Google Generative AI (Cloud-based for high quality)
- **Vector DB:** ChromaDB
- **UI:** Streamlit

---

## 🚀 How to Run

1.  **Setup Ollama:**
    Ensure [Ollama](https://ollama.com/) is installed and the DeepSeek model is downloaded:
    ```bash
    ollama pull deepseek-r1:1.5b
    ```
2.  **Environment Setup:**
    Provide your Google API Key for embeddings in the environment.
3.  **Launch:**
    ```bash
    streamlit run deepseek_reasoning_ai_agent.py
    ```

---

## 🏗️ How it Works

1.  **Upload:** User provides a PDF or URL.
2.  **Embed & Store:** Content is tokenized, embedded via Google AI, and stored in a local ChromaDB collection.
3.  **Query:** When a question is asked, the agent first searches the local database.
4.  **Reason:** DeepSeek-R1 analyzes the retrieved context to formulate a response.
5.  **Grounding:** If the local context is insufficient, the **Web Search Agent** (powered by Gemini) fills the gaps.

---

<div align="center">
    <b>Local Reasoning Intelligence Powered by DeepSeek & Agno</b>
</div>
