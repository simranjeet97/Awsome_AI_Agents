# 🏋️‍♂️ AI Health & Fitness Plan Generator

A holistic wellness platform that utilizes a multi-agent system to coordinate personalized nutrition and fitness strategies. Built with **Agno** and **Gemini**, this agent acts as your digital personal trainer and nutritionist.

---

## 🤖 Multi-Agent Orchestration

This system features three specialized agents collaborating to achieve your goals:

1.  **Dietary Planner:**
    - Creates personalized meal plans (Breakfast, Lunch, Dinner, Snacks).
    - Hardcoded instructions for Keto, Vegetarian, and Low Carb preferences.
    - Provides detailed nutritional breakdowns and hydration advice.

2.  **Fitness Trainer:**
    - Generates customized workout routines (Beginner, Intermediate, Advanced).
    - Includes warm-ups, main exercises, and cool-downs.
    - Provides critical safety tips and injury prevention advice.

3.  **Team Lead:**
    - The orchestrator that merges the Diet and Fitness plans.
    - Formats the final output into professional tables.
    - Provides lifestyle coaching and motivational consistency tips.

---

## 🛠️ Tech Stack

- **Model:** Gemini 2.0 Flash
- **Framework:** [Agno](https://github.com/agno-ai/agno)
- **Search Tool:** DuckDuckGo (for finding latest fitness research)
- **UI:** Streamlit (with a custom premium fitness-themed "Red/Green" design)

---

## 🚀 How to Run

1.  **Configure API Key:**
    Set your `GOOGLE_API_KEY` in the environment.
2.  **Launch the App:**
    ```bash
    streamlit run fitness.py
    ```
3.  **Personalize Your Profile:**
    - Enter your Age, Weight, and Height.
    - Select your Activity Level (Low, Moderate, High).
    - Choose a Fitness Goal (Weight Loss, Muscle Gain, etc.).

---

## 🎨 Premium Features

- **Stylish UI:** Customized CSS for a high-end personal trainer dashboard feel.
- **Holistic Integration:** Ensures your calorie intake perfectly aligns with your exertion level.
- **Motivation Engine:** Includes a "Goal Card" system to keep users focused on their journey.

---

<div align="center">
    <b>Your Personalized Path to Peak Performance</b>
</div>
