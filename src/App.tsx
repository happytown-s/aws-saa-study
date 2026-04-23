import { useState, useEffect } from 'react';
import type { TabName, QuizResult } from './types';
import Quiz from './components/Quiz';
import Progress from './components/Progress';

const STORAGE_KEY = 'aws-saa-results';

function loadResults(): QuizResult[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveResults(results: QuizResult[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(results));
}

export default function App() {
  const [tab, setTab] = useState<TabName>('quiz');
  const [results, setResults] = useState<QuizResult[]>(loadResults);

  useEffect(() => {
    saveResults(results);
  }, [results]);

  const addResult = (r: QuizResult) => {
    setResults(prev => [...prev, r]);
  };

  const clearResults = () => {
    setResults([]);
    localStorage.removeItem(STORAGE_KEY);
  };

  const tabs: { key: TabName; label: string }[] = [
    { key: 'quiz', label: 'Quiz' },
    { key: 'exam', label: 'Practice Exam' },
    { key: 'progress', label: 'Progress' },
  ];

  return (
    <div className="min-h-screen bg-dark-bg text-dark-text">
      <header className="bg-dark-surface border-b border-dark-border sticky top-0 z-50">
        <div className="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
          <h1 className="text-xl font-bold text-gold">AWS SAA Study</h1>
          <nav className="flex gap-1">
            {tabs.map(t => (
              <button
                key={t.key}
                onClick={() => setTab(t.key)}
                className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                  tab === t.key
                    ? 'bg-gold text-dark-bg'
                    : 'text-dark-muted hover:text-dark-text hover:bg-dark-card'
                }`}
              >
                {t.label}
              </button>
            ))}
          </nav>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-4 py-6">
        {tab === 'quiz' && <Quiz results={results} addResult={addResult} modeFilter={null} />}
        {tab === 'exam' && <Quiz results={results} addResult={addResult} modeFilter="exam" />}
        {tab === 'progress' && <Progress results={results} onClear={clearResults} />}
      </main>
    </div>
  );
}
