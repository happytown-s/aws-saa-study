import type { QuizConfig } from '../core/types';

export const quizConfig: QuizConfig = {
  id: 'aws-saa-exam',
  title: 'AWS SAA-C03',
  description: 'AWS Solutions Architect Associate 問題集',
  passLine: 72,
  examQuestions: 65,
  examTimeLimit: 130,
  categories: [
    { id: 'compute', name: 'EC2 & Compute', label: 'EC2 & Compute', icon: '🖥️', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'compute')) },    { id: 'storage', name: 'S3 & Storage', label: 'S3 & Storage', icon: '🗄️', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'storage')) },    { id: 'networking', name: 'VPC & Networking', label: 'VPC & Networking', icon: '🌐', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'networking')) },    { id: 'iam', name: 'IAM & Security', label: 'IAM & Security', icon: '🔒', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'iam')) },    { id: 'databases', name: 'RDS & Databases', label: 'RDS & Databases', icon: '💾', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'databases')) },    { id: 'monitoring', name: 'Monitoring & Logging', label: 'Monitoring & Logging', icon: '📊', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'monitoring')) },    { id: 'resilient', name: 'Resilient Architectures', label: 'Resilient Architectures', icon: '🏗️', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'resilient')) },    { id: 'performant', name: 'High-Performing Architectures', label: 'High-Performing Architectures', icon: '⚡', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'performant')) },    { id: 'secure', name: 'Secure Architectures', label: 'Secure Architectures', icon: '🛡️', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'secure')) },    { id: 'cost', name: 'Cost-Optimized Architectures', label: 'Cost-Optimized Architectures', icon: '💰', file: () => import('./questions').then(m => m.allQuestions.filter(q => q.category === 'cost')) }
  ],
  termsFile: () => import('./terms').then(m => m.terms),
};
