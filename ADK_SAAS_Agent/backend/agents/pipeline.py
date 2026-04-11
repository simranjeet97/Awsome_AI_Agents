from google.adk.agents.sequential_agent import SequentialAgent
from .planner_agent import planner_agent
from .researcher_agent import researcher_agent
from .writer_agent import writer_agent

async def save_to_memory_callback(callback_context):
    """Auto-ingest completed sessions into long-term memory."""
    # Note: Only fires if memory_service is configured
    try:
        if hasattr(callback_context._invocation_context, 'memory_service') and callback_context._invocation_context.memory_service is not None:
             await callback_context._invocation_context.memory_service.add_session_to_memory(
                 callback_context._invocation_context.session
             )
    except Exception as e:
        print(f"Failed to ingest session into memory: {e}")

# Root agent: runs Planner -> Researcher -> Writer in sequence
root_agent = SequentialAgent(
    name="ResearchPipeline",
    description="A three-stage research pipeline: Plan -> Research -> Write.",
    sub_agents=[planner_agent, researcher_agent, writer_agent],
    after_agent_callback=save_to_memory_callback,
)
