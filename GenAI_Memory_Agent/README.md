# 🧠 Digital Chatbot with Persistent Memory

A sophisticated support assistant that bridges the gap between conversational AI and persistent user knowledge. By combining **Mem0** with **Gemini**, this agent remembers user preferences, past interactions, and context across different sessions.

---

## ✨ Features

- **Long-Term Memory:** Integrated with [Mem0](https://mem0.ai) to store and retrieve user facts, preferences, and session context.
- **Memory Freshness:** Logic to prioritize "fresh" memories (from the last 7 days) for high-relevance interactions.
- **Web Search Fallback:** If internal reasoning fails or data is missing, the agent autonomously calls the **WebSearchAgent** (DuckDuckGo).
- **Graceful Fallbacks:** Intelligent detection of phrases like "I don't know" or "as an AI language model" to trigger proactive web research.
- **Multi-Framework Orchestration:** Combines **Microsoft AutoGen** for conversation management and **Agno** for specialized web tools.

---

## 🛠️ Tech Stack

- **Large Language Model:** Gemini 2.0 Flash
- **Memory Layer:** Mem0 Client
- **Frameworks:** Microsoft AutoGen & Agno
- **Search:** DuckDuckGo
- **UI:** Streamlit (Cyberpunk/Dark Mode Theme)

---

## 🚀 How to Run

1.  **Install Dependencies:**
    ```bash
    pip install streamlit mem0ai autogen-agentchat agno google-generativeai
    ```
2.  **Setup Keys:**
    - Create an account on [Mem0](https://mem0.ai) to get your `MEM0_API_KEY`.
    - Provide your `GOOGLE_API_KEY`.
3.  **Run the Chatbot:**
    ```bash
    streamlit run memory.py
    ```

---

## 🏗️ Intelligence Flow

1.  **Recognition:** The agent identifies the user and searches for relevant past memories.
2.  **Synthesis:** Combines current time, user memories, and the user's query into a rich prompt.
3.  **Generation:** Primary model attempts a response.
4.  **Verification:** If the response is a "standard AI refusal," the system switches to **Web Search Agent**.
5.  **Retention:** The final high-quality interaction is sanitized and saved back to **Mem0**.

---

<div align="center">
    <b>AI with a Memory: A Personalized Digital Companion</b>
</div>
