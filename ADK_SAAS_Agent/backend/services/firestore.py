from google.cloud import firestore_v1 as firestore
import datetime
import os

# Initialize only if GOOGLE_CLOUD_PROJECT is set
db = None
if os.getenv("GOOGLE_CLOUD_PROJECT"):
    try:
        db = firestore.AsyncClient()
    except Exception as e:
        print(f"Warning: Could not initialize Firestore AsyncClient: {e}")

async def save_brief_to_history(user_id, question, brief, session_id):
    if not db:
        print("Firestore not initialized, skipping save.")
        return
    
    doc_ref = db.collection("briefs").document()
    await doc_ref.set({
        "user_id": user_id,
        "question": question,
        "brief": brief,
        "session_id": session_id,
        "created_at": datetime.datetime.utcnow(),
    })

async def get_user_history(user_id):
    if not db:
        print("Firestore not initialized, returning empty history.")
        return []
    
    query = db.collection("briefs").where("user_id", "==", user_id).order_by(
        "created_at", direction=firestore.Query.DESCENDING
    ).limit(20)
    docs = await query.get()
    return [doc.to_dict() for doc in docs]
