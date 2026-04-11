#!/bin/bash
# test_e2e.sh - Automated CI Validation specific for ResearchPilot Backend (Section 8)

# Requires FIREBASE_API_KEY environment variable. 
# Optional BACKEND_URL, defaults to localhost:8080.
BACKEND_URL="${BACKEND_URL:-http://localhost:8080}"

if [ -z "$FIREBASE_API_KEY" ]; then
  echo "Error: FIREBASE_API_KEY must be set in your environment to fetch a test token."
  echo "Usage: FIREBASE_API_KEY=your_key ./test_e2e.sh"
  exit 1
fi

echo "Fetching test Firebase ID token..."

# Get a test Firebase ID token (use Firebase REST API for automated testing)
TOKEN=$(curl -s "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=$FIREBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"testpass","returnSecureToken":true}' \
  | jq -r .idToken)

if [ "$TOKEN" == "null" ] || [ -z "$TOKEN" ]; then
    echo "Error: Failed to fetch token. Ensure user test@test.com exists in your Firebase auth users."
    exit 1
fi

echo "Token fetched successfully. Calling the research endpoint..."

# Call the research endpoint
curl -X POST "$BACKEND_URL/research" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the latest breakthroughs in quantum error correction in 2025?"}'

echo -e "\n\nTest Run Completed!"
