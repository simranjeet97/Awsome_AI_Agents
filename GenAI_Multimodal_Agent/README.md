# 🎥 Multimodal Video Analysis Agent

An intelligent video processing engine that combines state-of-the-art computer vision with agentic reasoning. This agent analyzes video content—whether from a local upload or a YouTube URL—to extract themes, summarize events, and identify key visual elements.

---

## ✨ Features

- **Hybrid Input Support:** Processes both local MP4/MOV/AVI files and live **YouTube** video streams.
- **Intelligent Frame Extraction:** Custom OpenCV logic to sample frames at adjustable rates (default 1 FPS) for efficient analysis.
- **Visual Intelligence:** Uses **Gemini 2.0 Flash** to "see" and interpret the sampled frames in context.
- **Deep Theme Analysis:** Extracts key topics, summarizes content, and identifies primary objects or activities.
- **Web Grounding:** Integrated with **DuckDuckGo** to search for external context about the video's subject matter.
- **Structured Reports:** Provides standardized, markdown-formatted video summaries.

---

## 🛠️ Tech Stack

- **Model:** Gemini 2.0 Flash
- **Vision Logic:** OpenCV (`cv2`)
- **Video Tools:** Pytube (`pytubefix`) for YouTube stream extraction.
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **UI:** Streamlit (Features a custom side-panel for configuration)

---

## 🚀 How to Run

1.  **Install requirements:**
    ```bash
    pip install streamlit agno google-generativeai opencv-python pytubefix
    ```
2.  **Config API Key:**
    Set `GOOGLE_API_KEY` in your environment.
3.  **Launch:**
    ```bash
    streamlit run multimodal.py
    ```
4.  **Analyze:**
    - Paste a YouTube URL or upload a file.
    - Enter your specific question or analysis task (e.g., "Summarized the main arguments in this video").

---

## 🏗️ Architecture

1.  **Ingestion:** Python downloads the YouTube stream or reads the uploaded file.
2.  **Preprocessing:** OpenCV extracts frames at the set `frame_rate` and saves them temporarily.
3.  **Reasoning:** The **MultiModal Agent** receives the frame sequence and the user's task.
4.  **Synthesis:** Gemini analyzes the visual-temporal progression and produces a structured response.

---

<div align="center">
    <b>Next-Generation Video Understanding Powered by Gemini & Agno</b>
</div>
