# 🕵️‍♂️ AI Web Scraping & Lead Generation Suite

A versatile toolkit for automated data extraction and target intelligence gathering across major platforms. This suite combines high-fidelity web scraping with agentic logic to transform unstructured web data into structured, actionable business leads stored in Google Sheets or PDFs.

---

## 🛠️ Multi-Tool Intelligence

The suite features four specialized scraping agents:

### 1. 📌 Quora Lead Generator (`scrape.py`)
- **Focus:** Finding high-intent discussions about specific products or services.
- **Tools:** **Firecrawl** for extraction, **Composio** for Google Sheets integration.
- **Output:** Professional leads including Username, Bio, Upvotes, and Direct Links.

### 2. 🛒 Amazon Product Scraper (`image_scrape.py`)
- **Focus:** E-commerce market research and competitor monitoring.
- **Tools:** BeautifulSoup (for initial crawling) + Firecrawl (for deep neural extraction).
- **Extracted Data:** Product Titles, Prices, Descriptions, and high-res Image URLs.

### 3. 🔍 Google Job Search Scraper (`linkeidn.py`)
- **Focus:** Identifying hiring trends and job-related leads.
- **Tools:** Firecrawl Neural Search + Gemini Reasoning.
- **Output:** Structured dataframes of job titles and snippets ready for CRM export.

### 4. 📄 AI Web Research to PDF (`pdf.py`)
- **Focus:** Deep subject matter investigation with professional exports.
- **Tools:** DuckDuckGo + Agno + FPDF.
- **Outcome:** Generates a comprehensive, fact-checked markdown report and exports it as a formatted PDF.

---

## ✨ Features

- **Neural Surface Extraction:** Powered by **Firecrawl** to navigate complex JS-rendered pages effortlessly.
- **Composio Integration:** Seamlessly writes extracted data into **Google Sheets** for immediate CRM use.
- **Pydantic Schemas:** Ensures every data point (Price, Bio, Snippet) follows a rigid organizational structure.
- **Agentic Verification:** The AI agents summarize and verify data quality before final storage.

---

## 🚀 How to Run

1.  **Install Requirements:**
    ```bash
    pip install streamlit firecrawl-py composio-agno agno fpdf markdown2
    ```
2.  **Choose your tool:**
    ```bash
    streamlit run scrape.py # For Quora Leads
    streamlit run image_scrape.py # For Amazon Products
    ```

---

<div align="center">
    <b>Transforming the Open Web into Actionable Intelligence</b>
</div>
