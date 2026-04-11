import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Research from './pages/Research';

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <header className="bg-white border-b border-gray-200 py-4 px-6 md:px-12 flex justify-between items-center sticky top-0 z-10 shadow-sm">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 rounded bg-blue-600 flex items-center justify-center text-white font-bold text-xl">R</div>
            <Link to="/" className="text-xl font-bold text-gray-900 tracking-tight">ResearchPilot</Link>
          </div>
          <nav className="flex space-x-6 text-sm font-medium text-gray-600">
            <Link to="/" className="hover:text-blue-600 transition-colors">Dashboard</Link>
            <a href="#" className="hover:text-blue-600 transition-colors">History</a>
          </nav>
        </header>

        <main className="flex-1 w-full max-w-6xl mx-auto p-6 md:p-8">
          <Routes>
            <Route path="/" element={<Research />} />
          </Routes>
        </main>
        
        <footer className="py-6 text-center text-gray-400 text-sm border-t border-gray-200">
          © {new Date().getFullYear()} ResearchPilot. Built with Google ADK.
        </footer>
      </div>
    </Router>
  );
}

export default App;
