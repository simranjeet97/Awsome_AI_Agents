# 💻 SDE Coding Assistant Swarm

A professional software development ecosystem powered by a **Swarm of specialized AI agents**. This assistant streamlines the entire development lifecycle—from architectural planning and subtask decomposition to implementation and rigorous code review.

---

## 🤖 The SDE Pipeline

The assistant coordinates three high-level autonomous agents:

1.  **Planner Agent:**
    - Analyzes the development requirement.
    - Suggests a modern tech stack.
    - Breaks the project into actionable, prioritized subtasks.

2.  **Code Generator:**
    - Implements specific subtasks chosen by the user.
    - Generates clean, well-commented code.
    - Provides a contextual explanation for the architectural choices.

3.  **Code Reviewer:**
    - Performs an adversarial review of the generated code.
    - Identifies potential bugs, performance bottlenecks, and security risks.
    - Suggests optimizations following industry best practices.

---

## ✨ Key Features

- **Decomposition:** Automatically turns vague requirements into concrete engineering plans.
- **Dual-Model Logic:** Uses **GPT-4o** for both planning and high-fidelity code generation.
- **Adversarial Review:** Ensures code quality through a separate reviewer persona.
- **Context-Aware Implementations:** The coder agent respects the tech stack suggested by the planner.
- **User-in-the-Loop:** Users select which subtasks to implement, maintaining control of the build.

---

## 🛠️ Tech Stack

- **Model:** OpenAI GPT-4o
- **Framework:** OpenAI Swarm-based Runner architecture
- **Data Validation:** Pydantic (Structured JSON Output)
- **UI:** Streamlit

---

## 🚀 How to Run

1.  **Environment Setup:**
    Ensure `OPENAI_API_KEY` is available in your shell or script.
2.  **Launch Assistant:**
    ```bash
    streamlit run coding_agent.py
    ```
3.  **Start Building:**
    - Enter your feature request (e.g., "Build a React dashboard for monitoring solar panels").
    - Review the generated plan.
    - Select tasks to implement and review the code.

---

<div align="center">
    <b>Empowering Developers with Autonomous Engineering Agents</b>
</div>
