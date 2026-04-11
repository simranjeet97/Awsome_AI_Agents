import pathlib
from google.adk import Agent
from utils.skill_loader import load_skill_instructions

# Load the planner skill instructions from the file system
planner_skill_dir = pathlib.Path(__file__).parent.parent / "skills" / "planner_skill"
planner_instructions = load_skill_instructions(planner_skill_dir)

planner_agent = Agent(
    model="gemini-2.5-flash",
    name="PlannerAgent",
    description="Breaks a research question into a structured investigation plan.",
    instruction=(
        f"You are a research strategist. Follow these instructions to decompose "
        f"the user's question into a clear plan:\n\n{planner_instructions}"
    ),
    tools=[], # Skills are now part of instructions
    output_key="research_plan",   # auto-saves to session.state
)
