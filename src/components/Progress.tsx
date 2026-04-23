import { useMemo } from 'react';
import type { QuizResult } from '../types';
import examData from '../data/aws-saa-exam.json';

const categories = [...new Set((examData as any[]).map(q => q.category))].sort();

interface Props {
  results: QuizResult[];
  onClear: () => void;
}

export default function Progress({ results, onClear }: Props) {
  const stats = useMemo(() => {
    const total = results.length;
    const correct = results.filter(r => r.correct).length;
    const accuracy = total > 0 ? correct / total : 0;

    const byCategory = categories.map(cat => {
      const catResults = results.filter(r => r.category === cat);
      const c = catResults.filter(r => r.correct).length;
      return {
        category: cat,
        total: catResults.length,
        correct: c,
        accuracy: catResults.length > 0 ? c / catResults.length : 0,
      };
    });

    const estimatedScore = total > 0 ? Math.round(accuracy * 1000) : 0;

    const recent = results.slice(-50);
    const recentAccuracy = recent.length > 0 ? recent.filter(r => r.correct).length / recent.length : 0;

    let currentStreak = 0;
    let maxStreak = 0;
    let tempStreak = 0;
    for (const r of [...results].reverse()) {
      if (r.correct) {
        tempStreak++;
        maxStreak = Math.max(maxStreak, tempStreak);
      } else {
        break;
      }
    }
    currentStreak = tempStreak;

    return { total, correct, accuracy, byCategory, estimatedScore, recentAccuracy, currentStreak, maxStreak };
  }, [results]);

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <div className="bg-dark-surface rounded-xl p-4 border border-dark-border text-center">
          <div className="text-2xl font-bold text-gold">{stats.total}</div>
          <div className="text-xs text-dark-muted">Total Questions</div>
        </div>
        <div className="bg-dark-surface rounded-xl p-4 border border-dark-border text-center">
          <div className="text-2xl font-bold text-green-400">{stats.correct}</div>
          <div className="text-xs text-dark-muted">Correct</div>
        </div>
        <div className="bg-dark-surface rounded-xl p-4 border border-dark-border text-center">
          <div className="text-2xl font-bold text-gold-dark">{stats.total > 0 ? Math.round(stats.accuracy * 100) : 0}%</div>
          <div className="text-xs text-dark-muted">Accuracy</div>
        </div>
        <div className="bg-dark-surface rounded-xl p-4 border border-dark-border text-center">
          <div className="text-2xl font-bold text-gold-light">{stats.currentStreak}</div>
          <div className="text-xs text-dark-muted">Current Streak</div>
        </div>
      </div>

      <div className="bg-dark-surface rounded-xl p-6 border border-dark-border">
        <h3 className="text-sm font-semibold text-dark-muted mb-2">Estimated SAA Score</h3>
        <div className="text-4xl font-bold text-gold">{stats.total > 0 ? stats.estimatedScore : '---'}</div>
        <p className="text-xs text-dark-muted mt-1">Range: 0-1000 | Passing: 720</p>
        {stats.total >= 10 && (
          <p className="text-sm mt-2">
            {stats.accuracy >= 0.9
              ? 'Excellent! You are consistently scoring above the passing threshold.'
              : stats.accuracy >= 0.75
                ? 'Good work! Focus on weak categories to boost your score.'
                : stats.accuracy >= 0.6
                  ? 'Keep practicing. Review explanations for missed questions.'
                  : 'Build a strong foundation with more practice on each domain.'}
          </p>
        )}
      </div>

      <div className="bg-dark-surface rounded-xl p-6 border border-dark-border">
        <h3 className="text-sm font-semibold text-dark-muted mb-4">Category Breakdown</h3>
        <div className="space-y-3">
          {stats.byCategory.map(cat => (
            <div key={cat.category}>
              <div className="flex items-center justify-between mb-1">
                <span className="text-sm">{cat.category}</span>
                <span className="text-xs text-dark-muted">
                  {cat.total > 0 ? `${cat.correct}/${cat.total} (${Math.round(cat.accuracy * 100)}%)` : 'No data'}
                </span>
              </div>
              {cat.total > 0 && (
                <div className="w-full h-2 bg-dark-card rounded-full overflow-hidden">
                  <div
                    className={`h-full rounded-full transition-all ${
                      cat.accuracy >= 0.8 ? 'bg-green-500' : cat.accuracy >= 0.6 ? 'bg-gold' : 'bg-red-400'
                    }`}
                    style={{ width: `${cat.accuracy * 100}%` }}
                  />
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {results.length >= 10 && (
        <div className="bg-dark-surface rounded-xl p-6 border border-dark-border">
          <h3 className="text-sm font-semibold text-dark-muted mb-2">Recent Trend (Last 50)</h3>
          <div className="text-2xl font-bold text-gold-dark">{Math.round(stats.recentAccuracy * 100)}%</div>
          <p className="text-xs text-dark-muted">
            {stats.recentAccuracy > stats.accuracy ? 'Improving!' : stats.recentAccuracy < stats.accuracy ? 'Needs attention' : 'Steady'}
          </p>
        </div>
      )}

      {results.length > 0 && (
        <div className="text-center">
          <button
            onClick={onClear}
            className="px-4 py-2 text-sm text-dark-muted hover:text-red-400 transition-colors"
          >
            Clear All Progress Data
          </button>
        </div>
      )}
    </div>
  );
}
