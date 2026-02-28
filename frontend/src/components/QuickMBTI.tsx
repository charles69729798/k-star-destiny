import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, CheckCircle } from 'lucide-react';

interface QuickMBTIProps {
  onComplete: (mbti: string) => void;
  onClose: () => void;
  lang?: string;
}

const QuickMBTI: React.FC<QuickMBTIProps> = ({ onComplete, onClose, lang = 'en' }) => {
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [mode, setMode] = useState<'picker' | 'quiz'>('picker');

  const mbtiTypes = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
  ];

  const mbtiI18n: any = {
    en: {
      picker: "Direct Picker",
      quiz: "AI Quiz",
      title: "Select MBTI Type",
      step: "Step {s} of {t}",
      questions: [
        { id: 'E/I', q: 'How do you prefer to recharge?', options: { E: 'Talking with friends', I: 'Spending time alone' } },
        { id: 'S/N', q: 'How do you process information?', options: { S: 'Based on facts', N: 'Based on intuition' } },
        { id: 'T/F', q: 'How do you make decisions?', options: { T: 'Logical reasoning', F: 'Personal feelings' } },
        { id: 'J/P', q: 'How do you handle tasks?', options: { J: 'Structured plan', P: 'Go with the flow' } },
      ]
    },
    ko: {
      picker: "직접 선택",
      quiz: "AI 성향 퀴즈",
      title: "MBTI 유형 선택",
      step: "{s} / {t} 단계",
      questions: [
        { id: 'E/I', q: '에너지를 어디서 얻나요?', options: { E: '친구들과 수다', I: '혼자만의 충전' } },
        { id: 'S/N', q: '정보를 어떻게 받아들이나요?', options: { S: '사실과 디테일 중심', N: '상상과 직관 중심' } },
        { id: 'T/F', q: '결정을 내릴 때 중요한 것은?', options: { T: '논리와 원칙', F: '감정과 관계' } },
        { id: 'J/P', q: '일을 어떻게 처리하나요?', options: { J: '계획대로 꼼꼼히', P: '상황대로 유연하게' } },
      ]
    },
    es: {
      picker: "Selector Directo",
      quiz: "Cuestionario IA",
      title: "Seleccionar Tipo MBTI",
      step: "Paso {s} de {t}",
      questions: [
        { id: 'E/I', q: '¿Cómo prefieres recargar energías?', options: { E: 'Hablando con amigos', I: 'Pasando tiempo a solas' } },
        { id: 'S/N', q: '¿Cómo procesas la información?', options: { S: 'Basado en hechos', N: 'Basado en la intuición' } },
        { id: 'T/F', q: '¿Cómo tomas decisiones?', options: { T: 'Razonamiento lógico', F: 'Sentimientos personales' } },
        { id: 'J/P', q: '¿Cómo manejas las tareas?', options: { J: 'Plan estructurado', P: 'Seguir la corriente' } },
      ]
    }
  };

  const currentI18n = mbtiI18n[lang] || mbtiI18n.en;
  const questions = currentI18n.questions;

  const handleAnswer = (val: string) => {
    const newAnswers = { ...answers, [questions[step].id]: val };
    setAnswers(newAnswers);
    if (step < questions.length - 1) {
      setStep(step + 1);
    } else {
      // Calculate final MBTI
      const result = Object.values(newAnswers).join('');
      onComplete(result);
    }
  };

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <motion.div
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        className="bg-slate-900 border-2 border-k-purple/30 rounded-3xl p-8 max-w-md w-full relative overflow-hidden shadow-2xl"
      >
        <div className="flex items-center justify-between mb-6">
          <div className="flex gap-2 p-1 bg-slate-800 rounded-xl">
            <button
              onClick={() => setMode('picker')}
              className={`px-4 py-2 rounded-lg text-xs font-bold transition-all ${mode === 'picker' ? 'bg-k-purple text-white shadow-lg' : 'text-slate-400 hover:text-white'}`}
            >
              {currentI18n.picker}
            </button>
            <button
              onClick={() => {
                setMode('quiz');
                setStep(0);
                setAnswers({});
              }}
              className={`px-4 py-2 rounded-lg text-xs font-bold transition-all ${mode === 'quiz' ? 'bg-k-purple text-white shadow-lg' : 'text-slate-400 hover:text-white'}`}
            >
              {currentI18n.quiz}
            </button>
          </div>
          <motion.button
            whileHover={{ rotate: 90 }}
            whileTap={{ scale: 0.9 }}
            onClick={onClose}
            className="text-slate-500 hover:text-white transition-colors p-2"
          >
            <X className="h-6 w-6" />
          </motion.button>
        </div>

        <AnimatePresence mode="wait">
          {mode === 'picker' ? (
            <motion.div
              key="picker"
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              exit={{ y: -20, opacity: 0 }}
              className="space-y-6"
            >
              <h3 className="text-2xl font-black text-white glow-text">{currentI18n.title}</h3>
              <div className="grid grid-cols-4 gap-3">
                {mbtiTypes.map((type) => (
                  <motion.button
                    key={type}
                    whileHover={{ scale: 1.05, backgroundColor: 'rgba(168, 85, 247, 0.2)', borderColor: '#A855F7' }}
                    whileTap={{ scale: 0.95 }}
                    onClick={() => onComplete(type)}
                    className="aspect-square flex flex-col items-center justify-center bg-slate-800/50 border-2 border-slate-700 rounded-2xl transition-all group"
                  >
                    <span className="text-base font-black text-white group-hover:text-k-purple transition-colors">{type}</span>
                  </motion.button>
                ))}
              </div>
            </motion.div>
          ) : (
            <motion.div
              key="quiz"
              initial={{ x: 20, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              exit={{ x: -20, opacity: 0 }}
              className="space-y-8"
            >
              <div className="mb-2">
                <div className="h-1 w-full bg-slate-800 rounded-full mb-3 overflow-hidden">
                  <motion.div
                    className="h-full bg-gradient-to-r from-k-purple to-k-blue rounded-full"
                    initial={{ width: 0 }}
                    animate={{ width: `${((step + 1) / questions.length) * 100}%` }}
                  />
                </div>
                <p className="text-k-purple font-bold text-[10px] tracking-widest uppercase">
                  {currentI18n.step.replace('{s}', step + 1).replace('{t}', questions.length)}
                </p>
              </div>

              <h3 className="text-2xl font-bold leading-tight">{questions[step].q}</h3>

              <div className="grid gap-4">
                {Object.entries(questions[step].options as Record<string, string>).map(([key, label]) => (
                  <motion.button
                    key={key}
                    whileHover={{ scale: 1.02, x: 5 }}
                    whileTap={{ scale: 0.98 }}
                    onClick={() => handleAnswer(key)}
                    className="w-full text-left p-6 bg-slate-800/50 border-2 border-slate-700 rounded-2xl hover:border-k-purple hover:bg-k-purple/5 transition-all group flex justify-between items-center"
                  >
                    <span className="text-lg font-medium">{label}</span>
                    <CheckCircle className="h-5 w-5 text-k-purple opacity-0 group-hover:opacity-100 transition-opacity" />
                  </motion.button>
                ))}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>
    </div>
  );
};

export default QuickMBTI;
