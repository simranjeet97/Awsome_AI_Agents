from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.readonly_context import ReadonlyContext
import pathlib
from utils.skill_loader import load_skill_instructions

# Load the writer skill instructions
writer_skill_dir = pathlib.Path(__file__).parent.parent / "skills" / "writer_skill"
writer_instructions = load_skill_instructions(writer_skill_dir)

# InstructionProvider lets us inject session state dynamically
def writer_instruction(context: ReadonlyContext) -> str:
    plan = context.state.get("research_plan", "No plan found.")
    return (
        f"You are a professional research writer. "
        f"The original plan was:\n{plan}\n\n"
        f"Specific writing instructions:\n{writer_instructions}\n\n"
        f"Using the findings in session state, write a polished research brief "
        f"with: Executive Summary, Key Findings (with citations), and Conclusion. "
        f"Format in clean Markdown."
    )

writer_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="WriterAgent",
    description="Writes a polished research brief from findings.",
    instruction=writer_instruction,   # InstructionProvider function
    tools=[],
    output_key="final_brief",
)
