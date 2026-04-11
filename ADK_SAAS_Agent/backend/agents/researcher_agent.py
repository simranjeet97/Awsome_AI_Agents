from google.adk.tools.google_search_tool import google_search
import pathlib
from google.adk import Agent
from utils.skill_loader import load_skill_instructions

# Load the researcher skill instructions
researcher_skill_dir = pathlib.Path(__file__).parent.parent / "skills" / "researcher_skill"
researcher_instructions = load_skill_instructions(researcher_skill_dir)

researcher_agent = Agent(
    model="gemini-2.5-flash",
    name="ResearcherAgent",
    description="Executes the research plan using web search and synthesizes findings.",
    instruction=(
        f"You are a research analyst. Read session state key 'research_plan'. "
        f"Follow it precisely. Use google_search to find real, current information. "
        f"Your specific instructions are:\n\n{researcher_instructions}"
    ),
    tools=[google_search],
    output_key="findings",
)
