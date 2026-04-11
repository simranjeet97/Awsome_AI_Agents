import { useState, useEffect } from 'react';
import { auth, googleProvider, getIdToken } from '../firebase';
import { signInWithPopup, onAuthStateChanged, signOut } from 'firebase/auth';

export default function Research() {
  const [user, setUser] = useState(null);
  const [question, setQuestion] = useState("");
  const [brief, setBrief] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const unsub = onAuthStateChanged(auth, u => setUser(u));
    return () => unsub();
  }, []);

  const handleLogin = async () => {
    try {
      await signInWithPopup(auth, googleProvider);
    } catch(err) {
      console.error(err);
      setError("Login failed.");
    }
  }

  const handleLogout = () => signOut(auth);

  const submitResearch = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setError("");
    setBrief("");
    
    try {
      // Setup base URL from Vite env or fallback to local
      const baseUrl = import.meta.env.VITE_API_URL || "http://localhost:8080";
      
      let token = "test-token";
      try {
           token = await getIdToken();
      } catch (e) {
          console.warn("Could not retrieve auth token, using fallback.");
      }

      const res = await fetch(`${baseUrl}/research`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ question }),
      });
      
      if (!res.ok) throw new Error("API responded with an error");
      
      const data = await res.json();
      setBrief(data.brief);
    } catch (err) {
      console.error(err);
      setError("Research failed. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  if (!user) {
    return (
      <div className="flex flex-col items-center justify-center mt-20 p-12 bg-white rounded-2xl shadow-sm border border-gray-100 max-w-lg mx-auto text-center">
        <h2 className="text-3xl font-bold tracking-tight text-gray-900 mb-4">Welcome to ResearchPilot</h2>
        <p className="text-gray-500 mb-8 max-w-sm">Sign in to start drafting high-quality research briefs synthesized by intelligent agents.</p>
        <button 
          onClick={handleLogin}
          className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-8 rounded-full shadow-lg shadow-blue-500/30 transition-all hover:-translate-y-0.5 active:translate-y-0"
        >
          Sign in with Google
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <div className="flex items-center space-x-3">
          <img src={user.photoURL || 'https://via.placeholder.com/40'} alt="Profile" className="w-10 h-10 rounded-full border border-gray-200" />
          <div>
            <h1 className="text-2xl font-bold text-gray-900">New Research</h1>
            <p className="text-sm text-gray-500">Logged in as {user.email}</p>
          </div>
        </div>
        <button onClick={handleLogout} className="text-sm font-medium text-gray-500 hover:text-gray-900 bg-gray-100 px-4 py-2 rounded-full transition-colors">
          Sign out
        </button>
      </div>

      <div className="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden mb-8">
        <div className="p-6 md:p-8">
          <label htmlFor="question" className="block text-sm font-medium text-gray-700 mb-2">What would you like to investigate?</label>
          <textarea 
            id="question"
            className="w-full border border-gray-300 rounded-xl p-4 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all placeholder:text-gray-400 min-h-[120px] resize-y"
            placeholder="e.g. What are the latest breakthroughs in quantum error correction in 2025?"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          
          <div className="mt-4 flex justify-between items-center">
            <p className="text-sm text-gray-500">Takes ~30 seconds to run the agent pipeline.</p>
            <button 
              onClick={submitResearch}
              disabled={loading || !question.trim()}
              className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed text-white font-medium py-2.5 px-6 rounded-lg transition-colors flex items-center"
            >
              {loading ? (
                <>
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Researching...
                </>
              ) : 'Start Investigation'}
            </button>
          </div>
        </div>
      </div>

      {error && (
        <div className="bg-red-50 text-red-700 p-4 rounded-xl mb-8 border border-red-100 flex items-start">
          <span className="mr-3 mt-0.5">⚠️</span>
          <div>
            <h3 className="text-sm font-semibold text-red-800">Error Encountered</h3>
            <p className="text-sm mt-1">{error}</p>
          </div>
        </div>
      )}

      {brief && (
        <div className="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden mb-8">
          <div className="bg-gray-50 border-b border-gray-200 p-4 px-6 md:px-8">
            <h2 className="font-semibold text-gray-900 flex items-center">
              <span className="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
              Research Brief Generated
            </h2>
          </div>
          <div className="p-6 md:p-8 prose prose-blue max-w-none text-gray-800">
            {brief.split('\n').map((paragraph, idx) => (
              <p key={idx} className={paragraph.startsWith('#') ? 'font-bold text-gray-900 mt-6 mb-3' : 'mb-3'}>{paragraph}</p>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
