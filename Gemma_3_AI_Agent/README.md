# 🤖 Gemma 3 Local RAG Reasoning Agent

A high-performance, local-first retrieval-augmented generation (RAG) agent powered by Google's **Gemma 3** (via Ollama) and the **Agno** agentic framework. This agent combines document intelligence with web-based grounding for unparalleled reasoning capabilities.

---

## ✨ Features

- **Local Reasoning:** Uses **Gemma 3:1b** (Ollama) for fast, private, and powerful local inference.
- **Agentic RAG:** Automatically retrieves and synthesizes information from uploaded PDFs and web URLs.
- **Smart Summarization:** Generates concise summaries of long-form content.
- **Follow-up Generation:** Intelligent agent that creates 5 pedagogical questions to test understanding of the source material.
- **Web Search Fallback:** Integrated with **Gemini** and **DuckDuckGo** to find real-time information when local documents aren't enough.
- **Thinking Transparency:** Filters out raw `<think>` tags for a clean, professional user experience.

---

## 🛠️ Tech Stack

- **Model:** [Gemma 3](https://blog.google/technology/developers/google-gemma-3-open-models/) (Ollama)
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **Vector Database:** ChromaDB
- **Embeddings:** Google Generative AI (`models/embedding-001`)
- **UI:** Streamlit
- **Search:** DuckDuckGo Tools

---

## 🚀 How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Ensure Ollama is running** and you have the Gemma 3 model pulled:
    ```bash
    ollama pull gemma3:1b
    ```
3.  **Set your Google API Key** in the environment or update the script:
    ```python
    os.environ["GOOGLE_API_KEY"] = "your_key_here"
    ```
4.  **Start the application:**
    ```bash
    streamlit run gemma_3_rag_bot.py
    ```

---

## 🏗️ Architecture

1.  **Data Ingestion:** PDFs/URLs are parsed via LangChain and chunked using `RecursiveCharacterTextSplitter`.
2.  **Indexing:** High-dimensional embeddings are generated via Google AI and stored in a persistent **ChromaDB** collection.
3.  **Reasoning Pipeline:**
    - The **RAG Agent** retrieves the most relevant context.
    - If needed, the **Web Search Agent** fetches external data.
    - Gemma 3 synthesizes the final answer with a focus on detailed explanations and examples.

---

<div align="center">
    <b>Built with ❤️ using Gemma 3 + Agno Agentic AI</b>
</div>
