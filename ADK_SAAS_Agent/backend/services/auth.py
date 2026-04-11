import firebase_admin
from firebase_admin import credentials
import os

def init_firebase():
    """Initialize Firebase App with credentials."""
    try:
        cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "./service-account.json"))
        firebase_admin.initialize_app(cred)
        print("Firebase Admin initialized successfully.")
    except Exception as e:
        print(f"Warning: Could not initialize Firebase Admin SDK: {e}")
        # Initialize default app if there's no specific key but running in GCP
        try:
            firebase_admin.initialize_app()
        except ValueError:
            pass # Already initialized
