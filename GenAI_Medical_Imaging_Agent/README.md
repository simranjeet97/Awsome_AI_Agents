# 🩺 Medical Image Analysis Tool

An AI-powered radiological diagnostic assistant designed to interpret complex medical imaging documents including **X-rays**, **MRIs**, **CT scans**, and **Ultrasounds**. This tool provides a structured, professional-grade clinical analysis coupled with patient-friendly explanations.

---

## ✨ Features

- **Multi-Modality Support:** Analyzes any medical imaging format (JPG, PNG, DICOM-derived images).
- **Structured Clinical Reporting:**
    - **Modality & Region Identification:** Precise anatomical positioning.
    - **Key Findings:** Systematic highlighting of abnormalities and measurements.
    - **Diagnostic Assessment:** Confidence-ranked primary and differential diagnoses.
- **Patient-Friendly Logic:** Translates clinical jargon into clear, relatable analogies for patients.
- **Research Grounding:** Automatically searches the web for the latest medical literature and treatment protocols supporting the findings.
- **Visual Intelligence:** Powered by **Gemini 2.0 Flash** for state-of-the-art vision reasoning.

---

## 🛠️ Tech Stack

- **Model:** Gemini 2.0 Flash (Vision-capable)
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **Search Tool:** DuckDuckGo Tools
- **Image Processing:** PIL (Pillow)
- **UI:** Streamlit

---

## 🚀 How to Run

1.  **Configure API Key:**
    Provide your `GOOGLE_API_KEY` in the environment.
2.  **Launch:**
    ```bash
    streamlit run medical.py
    ```
3.  **Analyze Image:**
    - Upload a scan (e.g., a chest X-ray).
    - Clinical analysis will be generated automatically.

---

## 📋 Comprehensive Analysis Schema

The agent follows an expert-vetted reporting structure:
1. **Image Type & Region**
2. **Key Findings** (systematic observation)
3. **Diagnostic Assessment** (evidence-backed)
4. **Patient-Friendly Explanation**
5. **Research Context** (PubMed-adjacent grounding)

---

> [!IMPORTANT]
> **Disclaimer:** This tool is for educational and informational purposes only. All AI-generated analyses must be reviewed and validated by a qualified medical professional.

---

<div align="center">
    <b>AI-Assisted Diagnostics for the Modern Radiologist</b>
</div>
