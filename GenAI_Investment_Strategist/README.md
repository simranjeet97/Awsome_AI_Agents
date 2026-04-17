# 📈 AI Investment Strategist

A professional financial intelligence platform powered by a **Swarm of AI Agents** designed to provide executive-grade market analysis and stock recommendations. This agent uses real-time market data to simplify complex investment decisions.

---

## 🧠 The Investment Swarm

The platform leverages specialized agents working in tandem:

| Agent | Expertise |
| :--- | :--- |
| **Market Analyst** | Focuses on price action and relative performance over 6-month horizons. |
| **Company Researcher** | Fetches deep fundamentals, business summaries, and 5-tier news cycles. |
| **Stock Strategist** | Evaluates risk-reward ratios and industry trends to create actionable insights. |
| **Team Lead** | Aggregates all data into a final, ranked investor report with buy/sell logic. |

---

## ✨ Key Features

- **Real-Time Data:** Direct integration with **Yahoo Finance** (`yfinance`) for up-to-the-minute stock prices and news.
- **Performance Benchmarking:** Automated calculation of 6-month percentage changes and relative ranking.
- **Interactive Visuals:** High-end **Plotly** charts (Dark Mode) for visual stock comparison.
- **Fundamental Analysis:** Deep-dives into market cap, sector metrics, and business summaries.
- **Investor Reports:** Generates professional markdown reports with clear "Top Ranked" buy lists.

---

## 🛠️ Tech Stack

- **Model:** Gemini 2.0 Flash
- **Fintech Tools:** Yahoo Finance SDK (`yfinance`)
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **Charts:** Plotly Graph Objects
- **UI:** Streamlit (Custom Green/Gray "Financial" Theme)

---

## 🚀 How to Run

1.  **Install Requirements:**
    ```bash
    pip install streamlit yfinance agno plotly
    ```
2.  **Launch Platform:**
    ```bash
    streamlit run investment.py
    ```
3.  **Analyze:** Enter your tickers (e.g., `AAPL, TSLA, NVDA`) and generate your strategist report.

---

<div align="center">
    <b>Data-Driven Investment Insights Powered by AI</b>
</div>
