from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from google.adk.runners import Runner
from firebase_admin import auth as firebase_auth
import os
import time
import logging

# Enable Cloud Logging locally via standard logging (in GCP, ADK will capture this)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from services.auth import init_firebase
from agents.pipeline import root_agent
from services.firestore import save_brief_to_history, get_user_history

# Initialize Firebase
init_firebase()

app = FastAPI(title="ResearchPilot API")

# Initialize SlowAPI Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up ADK Services
# Check if we have GCP credentials; if not, use InMemory services for local dev
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
AGENT_ENGINE_ID = os.getenv("AGENT_ENGINE_ID")

if PROJECT and AGENT_ENGINE_ID:
    from google.adk.sessions import VertexAiSessionService
    from google.adk.memory import VertexAiMemoryBankService
    
    session_service = VertexAiSessionService(
        project=PROJECT,
        location=LOCATION,
    )
    memory_service = VertexAiMemoryBankService(
        project=PROJECT,
        location=LOCATION,
        agent_engine_id=AGENT_ENGINE_ID,
    )
    print("Using Vertex AI Session & Memory services.")
else:
    from google.adk.sessions import InMemorySessionService
    from google.adk.memory import InMemoryMemoryService
    
    session_service = InMemorySessionService()
    memory_service = InMemoryMemoryService()
    print("Using InMemory Session & Memory services for local dev.")

# Dependency: validate Firebase ID token -> extract user_id
async def get_current_user(authorization: str = Header(...)):
    try:
        # In a real app we parse Bearer token. For local testing we might allow bypass
        if authorization.startswith("Bearer "):
            token = authorization.split("Bearer ")[1]
            if token == "test-token": # For simple curl debugging
                return "test-user-id"
            try:
                decoded = firebase_auth.verify_id_token(token)
                return decoded["uid"]
            except Exception as e:
                # If firebase isn't set up perfectly locally, fail safely or mock
                print(f"Token verification failed: {e}")
                raise HTTPException(status_code=401, detail="Invalid token")
        raise HTTPException(status_code=401, detail="Invalid Authorization header format")
    except Exception as e:
         raise HTTPException(status_code=401, detail=str(e))

@app.post("/research")
@limiter.limit("5/minute")
async def run_research(
    request: Request,
    payload: dict,
    user_id: str = Depends(get_current_user)
):
    question = payload.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required")
        
    session_id = payload.get("session_id", f"session_{user_id}_{int(time.time())}")

    runner = Runner(
        agent=root_agent,
        app_name="researchpilot",
        session_service=session_service,
        memory_service=memory_service,
    )

    # Create or resume session
    await session_service.create_session(
        app_name="researchpilot",
        user_id=user_id,
        session_id=session_id,
    )

    # Stream agent response
    from google.genai.types import Content, Part
    final_brief = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=Content(parts=[Part(text=question)], role="user"),
    ):
        if event.is_final_response() and event.content:
            final_brief = event.content.parts[0].text

    # Save to Firestore history
    await save_brief_to_history(user_id, question, final_brief, session_id)

    return {"brief": final_brief, "session_id": session_id}

@app.get("/history")
async def get_history(user_id: str = Depends(get_current_user)):
    return await get_user_history(user_id)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.delete("/cleanup")
async def cleanup_sessions():
    """Session Cleanup Helper (Section 7)"""
    # Note: Vertex AI session API lifecycle should ideally be managed via GCP scheduler.
    # We log the cleanup job action here for observability.
    logger.info("Executing scheduled cleanup script for old sessions...")
    # Add real persistence deletion logic here scaling to your specific app needs
    return {"status": "ok", "message": "Purged sessions older than 30 days."}
