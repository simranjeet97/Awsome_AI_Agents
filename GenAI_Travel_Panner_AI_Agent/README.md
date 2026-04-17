# ✈️ AI-Powered Travel Planner

An intelligent, multi-agent travel concierge that automates the planning of your dream vacation. This platform fetches real-time flight data, researches local attractions, and builds a comprehensive, schedule-optimized itinerary tailord to your budget and preferences.

---

## 🤖 The Planning Swarm

Three specialized agents collaborate to design your perfect trip:

1.  **Researcher Agent:**
    - Deep-dives into the destination's climate, culture, and safety.
    - Curates must-visit landmarks and local hidden gems based on your interests.
2.  **Hotel & Restaurant Finder:**
    - Identifies highly-rated accommodations near your planned activities.
    - Discovers top-tier dining options matching your preferred cuisine.
3.  **Planner Agent:**
    - The master orchestrator that synthesizes flights, research, and stays.
    - Builds a day-by-day itinerary with scheduled activities and cost estimates.

---

## ✨ Key Features

- **Live Flight Search:** Direct integration with **Google Flights** via **SerpApi** to find the top 3 cheapest options.
- **Dynamic Itineraries:** Generates multi-day schedules considering departure/arrival times and travel themes (Adventure, Solo, Family, etc.).
- **Interactive Flight Cards:** Professional UI cards with airline logos, booking tokens, and "Book Now" links.
- **Personalized Recommendations:** Factors in budget levels (Economy, Standard, Luxury) and hotel ratings.
- **Travel Toolkit:** Includes a packing checklist, visa requirements toggle, and currency essentials.

---

## 🛠️ Tech Stack

- **Model:** Gemini 2.0 Flash
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **External APIs:** Google Search & Google Flights (SerpApi)
- **UI:** Streamlit (Custom "Sunset Orange" Travel Theme)

---

## 🚀 How to Run

1.  **Configure API Keys:**
    - `SERPAPI_KEY` (from [SerpApi](https://serpapi.com/))
    - `GOOGLE_API_KEY` (from [Google AI Studio](https://aistudio.google.com/))
2.  **Launch:**
    ```bash
    streamlit run travelagent.py
    ```
3.  **Plan:** Enter your Departure/Destination IATA codes (e.g., `NYC`, `LON`) and click "Generate Travel Plan".

---

<div align="center">
    <b>Your Personalized Journey, Planned by Intelligence</b>
</div>
