import React, { useState, useRef } from 'react';
import axios from 'axios';
import { Search, Sparkles, User, Calendar, BrainCircuit, Share2, HelpCircle, RefreshCcw, Edit3 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import QuickMBTI from './components/QuickMBTI';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const translations: any = {
  en: {
    title: "K-DESTINY AI",
    subtitle: "Global Saju + MBTI Matching for K-pop Fans",
    profile: "Your Profile",
    birthDate: "Your Birth Date",
    gender: "Your Gender",
    female: "Female",
    male: "Male",
    nonBinary: "Non-binary",
    mbti: "Your MBTI",
    dontKnow: "Don't know?",
    searchLabel: "Search Idol",
    searchDescription: "Enter the name of your favorite K-pop star. AI will automatically find their details.",
    searchPlaceholder: "Enter Idol Name (e.g. IU, Jungkook, Stray Kids)...",
    aiMode: "AI MODE",
    searching: "AI is searching for info...",
    extracting: "AI is extracting data...",
    checkComp: "Check Compatibility",
    connectDestiny: "Connect your destiny with {name} through K-Saju algorithms.",
    runAnalysis: "RUN ANALYSIS",
    destinyEnergy: "Destiny Energy",
    shareResult: "SHARE RESULT",
    footer: "Powered by bkit Vibecoding Kit & K-Saju AI Engine",
    selectType: "Select Type",
    enterManually: "AI could not find data. Please enter manually.",
    analysisError: "Failed to analyze. Check your input data.",
    birthDateAlert: "Please enter your birth date first!",
    required: "REQUIRED",
    copied: "Copied to clipboard!",
    trendingTitle: "Trending Idols",
    trendingSubtitle: "Select a star to check your destiny instantly.",
    tabSaju: "Soul Index: K-Saju & Life Indicator",
    tabFortune: "2026 God-saeng Calendar: Monthly Dopamine",
    tabSignal: "Destiny Signal: Universal Telepathy with {name}",
    introTitle: "Find Your Destiny",
    introDesc: "Now, it's time to connect your cosmic signals with K-stars. Who is your fated ideal type? Find out now!",
    birthDatePrompt: "Please enter your birth date first for accurate results!",
    mbtiPrompt: "Don't know the idol's MBTI? Use AI search or pick one from Trending below!",
    visitorsToday: "Today's Challengers",
    visitorsTotal: "Total Visitors"
  },
  ko: {
    title: "K-DESTINY AI",
    subtitle: "K-pop 팬을 위한 사주 + MBTI 매칭",
    profile: "내 프로필",
    birthDate: "생년월일",
    gender: "성별",
    female: "여성",
    male: "남성",
    nonBinary: "논바이너리",
    mbti: "MBTI",
    dontKnow: "모르겠어요?",
    searchLabel: "아이돌 검색",
    searchDescription: "좋아하는 K-pop 스타의 이름을 입력하세요. AI가 자동으로 정보를 찾아줍니다.",
    searchPlaceholder: "아이돌 이름을 입력하세요 (예: 아이유, 정국, 고윤정)...",
    aiMode: "AI 검색",
    searching: "AI가 정보를 검색 중입니다...",
    extracting: "AI가 데이터를 추출 중입니다...",
    checkComp: "궁합 확인",
    connectDestiny: "{name}과(와) 당신의 운명을 K-사주 알고리즘으로 연결해보세요.",
    runAnalysis: "분석 실행",
    destinyEnergy: "운명 에너지",
    shareResult: "결과 공유",
    footer: "bkit 바이브코딩 키트 & K-사주 AI 엔진 제공",
    selectType: "유형 선택",
    enterManually: "AI가 데이터를 찾지 못했습니다. 직접 입력해 주세요.",
    analysisError: "분석에 실패했습니다. 입력 데이터를 확인해 주세요.",
    birthDateAlert: "먼저 생년월일을 입력해 주세요!",
    required: "필수 입력",
    copied: "클립보드에 복사되었습니다!",
    trendingTitle: "인기 아이돌",
    trendingSubtitle: "운명을 바로 확인하고 싶은 스타를 선택하세요.",
    tabSaju: "Soul Index: K-사주 명식과 평생의 지표",
    tabFortune: "2026 갓생 캘린더: 월간 도파민 & 운세 흐름",
    tabSignal: "Destiny Signal: {name}과의 우주적 텔레파시 📡",
    introTitle: "운명적 이상형 찾기",
    introDesc: "자, 이제 K-스타와 당신의 우주적 시그널을 연결할 시간입니다. 당신의 운명적 이상형은 누구일까요? 지금 찾아보세요!",
    birthDatePrompt: "먼저 생년월일을 적어주세요. 꼼꼼히 적을수록 정확해요!",
    mbtiPrompt: "아이돌의 이름, MBTI를 모른다면? 검색 버튼을 누르거나 화면 아래 트렌딩을 선택해 보세요!",
    visitorsToday: "오늘의 도전자",
    visitorsTotal: "누적 접속자"
  },
  es: {
    title: "K-DESTINY AI",
    subtitle: "Saju + MBTI Matching para Fans de K-pop",
    profile: "Tu Perfil",
    birthDate: "Fecha de Nacimiento",
    gender: "Género",
    female: "Femenino",
    male: "Masculino",
    nonBinary: "No binario",
    mbti: "Tu MBTI",
    dontKnow: "¿No sabes?",
    searchLabel: "Buscar Ídolo",
    searchDescription: "Ingresa el nombre de tu estrella K-pop favorita. La IA encontrará sus detalles automáticamente.",
    searchPlaceholder: "Ingresa el nombre del ídolo (ej: IU, Jungkook, Stray Kids)...",
    aiMode: "MODO AI",
    searching: "La IA está buscando información...",
    extracting: "La IA está extrayendo datos...",
    checkComp: "Verificar Compatibilidad",
    connectDestiny: "Conecta tu destino con {name} a través de algoritmos K-Saju.",
    runAnalysis: "EJECUTAR ANÁLISIS",
    destinyEnergy: "Energía del Destino",
    shareResult: "COMPARTIR RESULTADO",
    footer: "Impulsado por bkit Vibecoding Kit & K-Saju AI Engine",
    selectType: "Seleccionar Tipo",
    enterManually: "La IA no pudo encontrar datos. Ingresa manualmente.",
    analysisError: "Error en el análisis. Verifica tus datos.",
    birthDateAlert: "¡Primero ingresa tu fecha de nacimiento!",
    required: "REQUERIDO",
    copied: "¡Copiado al portapapeles!",
    trendingTitle: "Ídolos Populares",
    trendingSubtitle: "Selecciona una estrella para verificar tu destino al instante.",
    tabSaju: "Soul Index: K-Saju y el Indicador de Vida",
    tabFortune: "Calendario 2026: Flujo de Dopamina Mensual",
    tabSignal: "Señal del Destino: Telepatía Universal con {name}",
    introTitle: "Encuentra tu Destino",
    introDesc: "Ahora es el momento de conectar tus señales cósmicas con las estrellas de K-pop. ¿Quién es tu tipo ideal predestinado? ¡Descúbrelo ahora!",
    birthDatePrompt: "¡Por favor, ingresa tu fecha de nacimiento primero para obtener resultados precisos!",
    mbtiPrompt: "¿No sabes el MBTI del ídolo? ¡Usa la búsqueda de IA o elige uno de Popular abajo!",
    visitorsToday: "Retadores de Hoy",
    visitorsTotal: "Visitantes Totales"
  }
};


const App = () => {
  const [lang, setLanguage] = useState('en');

  // 국가별 언어 탭 자동 인식
  React.useEffect(() => {
    const browserLang = navigator.language.slice(0, 2);
    if (browserLang === 'ko') setLanguage('ko');
    else if (browserLang === 'es') setLanguage('es');
    else setLanguage('en');
  }, []);
  const t = (key: string, params: any = {}) => {
    let text = translations[lang][key] || key;
    Object.keys(params).forEach(p => {
      text = text.replace(`{${p}}`, params[p]);
    });
    return text;
  };

  // States for Idol Search & Data
  const [idolSearchName, setIdolSearchName] = useState('');
  const [loading, setLoading] = useState(false);
  const [idolData, setIdolData] = useState<any>(null);
  const [isManualMode, setIsManualMode] = useState(false);

  // States for User Data
  const [userMBTI, setUserMBTI] = useState('');
  const [userBirthDate, setUserBirthDate] = useState('');
  const [userGender, setUserGender] = useState('female');
  const [showMBTIQuiz, setShowMBTIQuiz] = useState(false);
  const [analysisResult, setAnalysisResult] = useState<any>(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [showMissingMbtiModal, setShowMissingMbtiModal] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [showErrorShake, setShowErrorShake] = useState(false);
  const [popularIdols, setPopularIdols] = useState<any[]>([]);
  const [activeTab, setActiveTab] = useState<'saju' | 'fortune' | 'signal'>('saju');
  // 후보 선택 UI
  const [candidates, setCandidates] = useState<any[]>([]);
  const [showCandidates, setShowCandidates] = useState(false);
  const [candidatesLoading, setCandidatesLoading] = useState(false);

  // 구글 보조 검색 UI
  const [assistantLoading, setAssistantLoading] = useState(false);
  const mbtiInputRef = useRef<HTMLInputElement>(null);

  // Fetch Popular Idols on Mount
  React.useEffect(() => {
    const fetchPopular = async () => {
      try {
        const res = await axios.get(`${API_URL}/idols/popular`);
        if (res.data.status === 'success') setPopularIdols(res.data.data);
      } catch (err) {
        console.error('Failed to fetch popular idols', err);
      }
    };
    fetchPopular();
  }, []);

  const handleIdolClick = async (name: string) => {
    setIdolSearchName(name);
    // 상태 업데이트 후 바로 검색 로직 실행
    await executeSearch(name);
  };

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!idolSearchName) return;
    await executeSearch(idolSearchName);
  };

  const executeSearch = async (searchName: string) => {
    setLoading(true);
    setAnalysisResult(null);
    setIsManualMode(false);
    setErrorMessage(null);
    setCandidates([]);
    setShowCandidates(false);

    try {
      // 1단계: 후보 목록 먼저 조회
      setCandidatesLoading(true);
      const candRes = await axios.get(`${API_URL}/idol/candidates`, {
        params: { name: searchName }, timeout: 30000
      });
      setCandidatesLoading(false);

      const cands = candRes.data.candidates || [];
      const personCands = cands.filter((c: any) => c.is_person);

      // 사람 후보가 2개 이상이면 → 선택 UI 표시
      if (personCands.length >= 2) {
        setCandidates(personCands);
        setShowCandidates(true);
        setLoading(false);
        return;
      }

      // 후보가 1개이거나 없으면 → 바로 검색
      const wiki_title = personCands.length === 1 ? personCands[0].title : '';
      const wiki_lang = personCands.length === 1 ? (personCands[0].lang || 'en') : '';

      const response = await axios.get(`${API_URL}/idol/search`, {
        params: { name: searchName, wiki_title, wiki_lang }, timeout: 45000
      });

      if (response.data.status === 'success') {
        setIdolData(response.data.data);
      } else {
        setIdolData({ name: searchName, birth_date: '', gender: 'female', mbti: '' });
        setIsManualMode(true);
      }
    } catch (error) {
      console.error('AI Search Error:', error);
      setCandidatesLoading(false);
      setIsManualMode(true);
      setErrorMessage(t('analysisError'));
    } finally {
      setLoading(false);
    }
  };

  const isValidDate = (dateStr: string) => {
    if (!dateStr || dateStr.length !== 10) return false;
    const [y, m, d] = dateStr.split('-').map(Number);
    if (y < 1900 || y > 2100) return false;
    if (m < 1 || m > 12) return false;
    const date = new Date(y, m - 1, d);
    return date.getFullYear() === y && date.getMonth() === m - 1 && date.getDate() === d;
  };



  const handleCandidateSelect = async (candidate: any) => {
    setShowCandidates(false);
    setCandidates([]);
    setLoading(true);
    setErrorMessage(null);
    try {
      const response = await axios.get(`${API_URL}/idol/search`, {
        params: {
          name: idolSearchName,
          wiki_title: candidate.title,
          wiki_lang: candidate.lang || 'en'
        },
        timeout: 45000
      });
      if (response.data.status === 'success') {
        setIdolData(response.data.data);
      } else {
        setIdolData({ name: idolSearchName, birth_date: '', gender: 'female', mbti: '' });
        setIsManualMode(true);
      }
    } catch (error) {
      setIsManualMode(true);
      setErrorMessage(t('analysisError'));
    } finally {
      setLoading(false);
    }
  };

  const runFullAnalysis = async (skipMbtiCheck = false) => {
    if (!userBirthDate) {
      setErrorMessage(t('birthDateAlert'));
      setShowErrorShake(true);
      setTimeout(() => setShowErrorShake(false), 600);
      return;
    }

    if (isManualMode && !idolData.birth_date) {
      setErrorMessage(t('birthDateAlert'));
      setShowErrorShake(true);
      setTimeout(() => setShowErrorShake(false), 600);
      return;
    }

    // MBTI가 없으면 차단 모달 표출
    if (!skipMbtiCheck && (!idolData.mbti || idolData.mbti === 'Unknown')) {
      setShowMissingMbtiModal(true);
      return;
    }

    setAnalyzing(true);
    setErrorMessage(null);
    try {
      const response = await axios.get(`${API_URL}/saju/analyze`, {
        params: {
          birth_date: userBirthDate,
          gender: userGender,
          user_mbti: userMBTI,
          idol_name: idolData?.name || idolSearchName,
          idol_mbti: idolData?.mbti || '',
          idol_birth_date: idolData?.birth_date || '',
          lang: lang // 현재 선택된 프론트엔드 언어 코드 전송
        }
      });
      setAnalysisResult(response.data.analysis);
      setActiveTab('saju'); // 결과가 나오면 첫 탭으로 초기화
    } catch (error) {
      console.error('Analysis Error:', error);
      setErrorMessage(t('analysisError'));
    } finally {
      setAnalyzing(false);
    }
  };

  const handleAssistantSearch = async () => {
    setAssistantLoading(true);
    try {
      const res = await axios.get(`${API_URL}/idol/assistant`, {
        params: { name: idolData?.name || idolSearchName }
      });
      if (res.data.status === 'success') {
        const info = res.data.data;
        const newMbti = info.mbti || idolData?.mbti;

        setIdolData((prev: any) => ({
          ...prev,
          birth_date: info.birth_date || prev.birth_date,
          mbti: newMbti
        }));

        // 검색했는데도 MBTI가 없으면 수동 입력 모드로 자동 전환 및 포커스
        if (!newMbti || newMbti === 'Unknown') {
          setIsManualMode(true);
          setErrorMessage("검색 결과가 없어 수동 입력 모드로 전환합니다.");
          setTimeout(() => mbtiInputRef.current?.focus(), 100);
        }
      }
    } catch (e) {
      console.error('Assistant Error:', e);
    } finally {
      setAssistantLoading(false);
    }
  };

  const handleShare = async () => {
    const shareData = {
      title: 'My K-Destiny Result',
      text: `I matched with ${idolData.name}! My K-Energy is ${analysisResult?.label}. Check yours on K-Destiny!`,
      url: window.location.href,
    };

    try {
      if (navigator.share) {
        await navigator.share(shareData);
      } else {
        alert(t('copied'));
        navigator.clipboard.writeText(shareData.text);
      }
    } catch (err) {
      console.log('Share failed', err);
    }
  };

  // Language auto-sync for analysis results
  React.useEffect(() => {
    if (analysisResult && !analyzing) {
      // Re-run the analysis to fetch translation using the newly selected language
      runFullAnalysis();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [lang]);

  return (
    <div className="container mx-auto px-4 py-10 max-w-4xl min-h-screen relative z-10">
      {/* Language Switcher */}
      <div className="flex justify-end gap-2 mb-4">
        {['es', 'en', 'ko'].map((l) => (
          <button
            key={l}
            onClick={() => setLanguage(l)}
            className={`px-3 py-1 rounded-full text-xs font-bold transition-all ${lang === l ? 'bg-k-purple text-white shadow-lg' : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
              }`}
          >
            {l.toUpperCase()}
          </button>
        ))}
      </div>

      <header className="text-center mb-12">
        <motion.h1
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="text-6xl font-black mb-4 bg-gradient-to-r from-k-pink via-k-purple to-k-blue bg-clip-text text-transparent italic select-none"
        >
          {t('title')}
        </motion.h1>
        <p className="text-slate-400 text-lg font-medium">
          {t('subtitle')}
        </p>
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5, duration: 1 }}
          className="mt-6 mb-8 max-w-lg mx-auto bg-slate-800/60 border border-k-purple/30 rounded-2xl p-4 shadow-lg"
        >
          <p className="text-slate-300 font-medium leading-relaxed italic text-sm md:text-base">
            ✨ {t('introDesc')} ✨
          </p>
        </motion.div>
      </header>

      {/* User Info Section */}
      <section className="bg-slate-800/30 border border-slate-700/50 rounded-3xl p-6 mb-8 backdrop-blur-sm shadow-xl">
        <h2 className="text-sm font-bold text-slate-500 uppercase tracking-widest mb-4 flex items-center gap-2">
          <User className="h-4 w-4" /> {t('profile')}
        </h2>
        <div className="grid md:grid-cols-3 gap-4">
          <div className="space-y-2">
            <label className="text-xs font-bold text-slate-400 ml-1">{t('birthDate')}</label>
            <motion.input
              animate={showErrorShake && !userBirthDate ? { x: [-10, 10, -10, 10, 0] } : {}}
              transition={{ duration: 0.4 }}
              type="text"
              placeholder="YYYY-MM-DD"
              maxLength={10}
              value={userBirthDate}
              onChange={(e) => {
                const raw = e.target.value.replace(/\D/g, '').slice(0, 8);
                let formatted = raw;
                if (raw.length > 4) formatted = `${raw.slice(0, 4)}-${raw.slice(4)}`;
                if (raw.length > 6) formatted = `${formatted.slice(0, 7)}-${raw.slice(6)}`;
                setUserBirthDate(formatted);
              }}
              className={`w-full bg-slate-900 border-2 rounded-xl px-4 py-3 outline-none transition-all ${userBirthDate.length === 10 && !isValidDate(userBirthDate)
                ? 'border-red-500 ring-2 ring-red-500/20'
                : 'border-slate-700 focus:border-k-blue'
                }`}
            />
            {userBirthDate.length === 10 && !isValidDate(userBirthDate) ? (
              <p className="text-red-400 text-xs mt-1 font-bold animate-pulse">Invalid Date</p>
            ) : (
              <p className="text-[11px] text-slate-500 mt-2 flex items-center gap-1 opacity-80">
                <Sparkles className="h-3 w-3 text-yellow-500" /> {t('birthDatePrompt')}
              </p>
            )}
          </div>
          <div className="space-y-2">
            <label className="text-xs font-bold text-slate-400 ml-1">{t('gender')}</label>
            <select
              value={userGender}
              onChange={(e) => setUserGender(e.target.value)}
              className="w-full bg-slate-900 border-2 border-slate-700 rounded-xl px-4 py-3 focus:border-k-pink outline-none transition-all appearance-none cursor-pointer"
            >
              <option value="female">{t('female')}</option>
              <option value="male">{t('male')}</option>
              <option value="non-binary">{t('nonBinary')}</option>
            </select>
          </div>
          <div className="space-y-2">
            <label className="text-xs font-bold text-slate-400 ml-1 flex justify-between">
              {t('mbti')}
              <motion.button
                whileHover={{ x: 2 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => setShowMBTIQuiz(true)}
                className="text-k-purple hover:underline flex items-center gap-1 font-bold"
              >
                <HelpCircle className="h-3 w-3" /> {t('dontKnow')}
              </motion.button>
            </label>
            <select
              value={userMBTI}
              onChange={(e) => setUserMBTI(e.target.value)}
              className="w-full bg-slate-900 border-2 border-slate-700 rounded-xl px-4 py-3 focus:border-k-purple outline-none transition-all appearance-none cursor-pointer"
            >
              <option value="">{t('selectType')}</option>
              {["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"].map(t_mbti => (
                <option key={t_mbti} value={t_mbti}>{t_mbti}</option>
              ))}
            </select>
          </div>
        </div>
      </section>

      {/* AI Idol Search Bar */}
      <div className="max-w-2xl mx-auto mb-16">
        <div className="mb-4 ml-2">
          <label className="text-xl font-bold text-k-blue flex items-center gap-2 mb-1">
            <Sparkles className="h-5 w-5" /> {t('searchLabel')}
          </label>
          <p className="text-slate-500 text-sm">{t('searchDescription')}</p>
        </div>
        <form onSubmit={handleSearch} className="relative group">
          <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <Search className="h-5 w-5 text-slate-500 group-focus-within:text-k-purple transition-colors" />
          </div>
          <input
            type="text"
            value={idolSearchName}
            onChange={(e) => setIdolSearchName(e.target.value)}
            placeholder={t('searchPlaceholder')}
            className="block w-full pl-12 pr-32 py-5 bg-slate-800 border-2 border-slate-700 rounded-2xl focus:ring-8 focus:ring-k-purple/10 focus:border-k-purple transition-all text-white placeholder-slate-500 text-lg shadow-2xl"
          />
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            type="submit"
            className="absolute right-3 top-2 bottom-2 px-6 bg-gradient-to-r from-k-purple to-k-blue rounded-xl font-bold flex items-center gap-2 hover:brightness-110 transition-all active:scale-95 shadow-lg"
          >
            <Sparkles className="h-4 w-4" />
            {t('aiMode')}
          </motion.button>
        </form>

        {/* 후보 선택 UI - 동명이인이 여러 명일 때 표시 */}
        {candidatesLoading && (
          <motion.div
            initial={{ opacity: 0, y: -8 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-4 text-center py-4"
          >
            <p className="text-slate-400 text-sm animate-pulse flex items-center justify-center gap-2">
              <Sparkles className="h-4 w-4 text-k-purple" />
              Wikipedia에서 후보를 검색하는 중...
            </p>
          </motion.div>
        )}

        {showCandidates && candidates.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-4 bg-slate-800/60 border border-k-purple/30 rounded-2xl p-4 backdrop-blur-sm"
          >
            <div className="flex items-center justify-between mb-3">
              <p className="text-sm font-bold text-k-purple flex items-center gap-1">
                <Search className="h-4 w-4" />
                동명이인이 있습니다. 해당하는 분을 선택해 주세요
              </p>
              <button
                onClick={() => { setShowCandidates(false); setCandidates([]); }}
                className="text-slate-500 hover:text-white text-xs px-2 py-1 rounded-lg hover:bg-slate-700 transition-all"
              >
                ✕ 닫기
              </button>
            </div>
            <div className="grid grid-cols-1 gap-2">
              {candidates.map((c: any, idx: number) => (
                <motion.button
                  key={idx}
                  whileHover={{ scale: 1.01, x: 4 }}
                  whileTap={{ scale: 0.99 }}
                  onClick={() => handleCandidateSelect(c)}
                  className="flex items-center gap-4 p-3 rounded-xl bg-slate-700/50 border border-slate-600/40 hover:border-k-purple/50 hover:bg-slate-700 transition-all text-left w-full"
                >
                  {/* 썸네일 */}
                  <div className="w-14 h-14 rounded-lg overflow-hidden flex-shrink-0 bg-slate-600">
                    {c.thumbnail ? (
                      <img src={c.thumbnail} alt={c.title} className="w-full h-full object-cover" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-400 text-xl">
                        👤
                      </div>
                    )}
                  </div>
                  {/* 이름 + 설명 */}
                  <div className="flex-1 min-w-0">
                    <p className="font-bold text-white text-sm truncate">{c.title}</p>
                    {c.description && (
                      <p className="text-xs text-slate-400 mt-0.5 truncate">{c.description}</p>
                    )}
                    {c.extract && (
                      <p className="text-xs text-slate-500 mt-1 line-clamp-2 leading-relaxed">{c.extract}</p>
                    )}
                  </div>
                  <div className="text-k-purple text-lg flex-shrink-0">›</div>
                </motion.button>
              ))}
            </div>
          </motion.div>
        )}

        {/* Popular Idols Section */}
        <div className="mt-8 px-2 overflow-hidden">
          <h3 className="text-sm font-bold text-slate-500 uppercase tracking-widest mb-4 flex items-center gap-2">
            <Sparkles className="h-3 w-3 text-k-pink" /> {t('trendingTitle')}
          </h3>
          <motion.div
            className="flex gap-4 overflow-x-auto pb-6 scrollbar-hide no-scrollbar"
            style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
          >
            {popularIdols.map((idol: any, idx: number) => (
              <motion.button
                key={idol.id}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: idx * 0.05 }}
                whileHover={{ y: -5, scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => handleIdolClick(idol.name_en)}
                className="flex-shrink-0 w-32 bg-slate-800/50 border border-slate-700/50 rounded-2xl p-3 hover:bg-slate-700/50 hover:border-k-purple/50 transition-all text-center group"
              >
                <div className="w-full aspect-square bg-slate-900 rounded-xl mb-3 flex items-center justify-center overflow-hidden border border-slate-700 group-hover:border-k-purple/30">
                  <img
                    src={`/custom-avatars/${idol.name_en.toLowerCase()}.png`}
                    alt={idol.name_en}
                    className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity"
                    onError={(e: any) => {
                      e.target.src = "https://api.dicebear.com/7.x/avataaars/svg?seed=" + idol.name_en;
                    }}
                  />
                </div>
                <p className="text-xs font-black text-white truncate mb-0.5">{lang === 'ko' ? idol.name_kr : idol.name_en}</p>
                <p className="text-[10px] text-slate-500 font-bold uppercase tracking-tight">{idol.group}</p>
              </motion.button>
            ))}
          </motion.div>
        </div>
      </div>

      {/* Status Messages (Error/Info) */}
      <AnimatePresence>
        {(errorMessage || isManualMode) && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className={`max-w-2xl mx-auto mb-6 px-6 py-4 rounded-2xl flex items-center gap-4 border shadow-lg ${isManualMode && !errorMessage
              ? 'bg-k-blue/10 border-k-blue/30 text-k-blue'
              : 'bg-red-500/10 border-red-500/30 text-red-200'
              }`}
          >
            {isManualMode && !errorMessage ? (
              <BrainCircuit className="h-6 w-6 flex-shrink-0 animate-pulse" />
            ) : (
              <HelpCircle className="h-6 w-6 flex-shrink-0" />
            )}
            <div>
              <p className="text-sm font-black uppercase tracking-widest mb-0.5">
                {isManualMode && !errorMessage ? 'AI-Assisted Manual Mode' : 'ERROR'}
              </p>
              <p className="text-sm opacity-90 mb-2">
                {errorMessage || t('enterManually')}
              </p>
              {isManualMode && (
                <button
                  onClick={handleAssistantSearch}
                  disabled={assistantLoading}
                  className="px-3 py-1.5 bg-k-blue/20 text-k-blue border border-k-blue/30 hover:bg-k-blue/30 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5"
                >
                  {assistantLoading ? <RefreshCcw className="h-3 w-3 animate-spin" /> : <Search className="h-3 w-3" />}
                  구글 검색으로 자동 채우기
                </button>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Missing MBTI Modal */}
      <AnimatePresence>
        {showMissingMbtiModal && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
          >
            <motion.div
              initial={{ scale: 0.9, y: 20 }}
              animate={{ scale: 1, y: 0 }}
              exit={{ scale: 0.9, y: 20 }}
              className="bg-slate-800 border border-slate-700 rounded-[2rem] p-8 max-w-sm w-full shadow-2xl relative overflow-hidden"
            >
              <div className="absolute -top-10 -right-10 w-32 h-32 bg-k-purple/20 rounded-full blur-[40px]"></div>

              <div className="flex justify-center mb-6">
                <div className="p-4 bg-slate-900/50 rounded-full border border-k-purple/30">
                  <BrainCircuit className="h-10 w-10 text-k-purple animate-pulse" />
                </div>
              </div>

              <h3 className="text-xl font-black text-center mb-2">MBTI 정보가 없습니다</h3>
              <p className="text-slate-400 text-sm text-center mb-8 leading-relaxed">
                아이돌의 MBTI를 알면 더 강력하고 섬세한 <strong>Destiny Signal(궁합)</strong>을 분석할 수 있어요! 어떻게 할까요?
              </p>

              <div className="space-y-3">
                <button
                  onClick={async () => {
                    await handleAssistantSearch();
                    setShowMissingMbtiModal(false);
                  }}
                  disabled={assistantLoading}
                  className="w-full flex items-center justify-center gap-2 py-3 px-4 bg-gradient-to-r from-blue-600/20 to-indigo-600/20 hover:from-blue-600/40 hover:to-indigo-600/40 text-blue-300 font-bold rounded-xl border border-blue-500/30 transition-all flex-row"
                >
                  {assistantLoading ? <RefreshCcw className="h-4 w-4 animate-spin" /> : <Search className="h-4 w-4" />}
                  구글 AI로 자동 검색하기
                </button>

                <button
                  onClick={() => {
                    setShowMissingMbtiModal(false);
                    setIsManualMode(true);
                    setTimeout(() => mbtiInputRef.current?.focus(), 100);
                  }}
                  className="w-full flex items-center justify-center gap-2 py-3 px-4 bg-slate-700/50 hover:bg-slate-700 text-slate-300 font-bold rounded-xl transition-all"
                >
                  <Edit3 className="h-4 w-4" />
                  직접 입력할래요
                </button>

                <button
                  onClick={() => {
                    setShowMissingMbtiModal(false);
                    runFullAnalysis(true);
                  }}
                  className="w-full flex items-center justify-center gap-2 py-3 px-4 bg-k-purple hover:bg-opacity-80 text-white font-black rounded-xl shadow-lg transition-all"
                >
                  <Sparkles className="h-4 w-4" />
                  없이 순수 사주로만 분석하기
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Results Display */}
      <AnimatePresence>
        {loading && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-center py-20">
            <div className="animate-spin h-12 w-12 border-4 border-k-purple border-t-transparent rounded-full mx-auto mb-4"></div>
            <p className="text-xl font-medium text-slate-300 italic">{t('searching')}</p>
          </motion.div>
        )}

        {idolData && !loading && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="bg-slate-800 rounded-[2rem] p-10 border border-slate-700 shadow-2xl overflow-hidden relative"
          >
            <div className="absolute -top-20 -right-20 w-64 h-64 bg-k-purple/10 rounded-full blur-[80px]"></div>

            {/* Manual Edit Toggle */}
            <button
              onClick={() => setIsManualMode(!isManualMode)}
              className="absolute top-6 right-6 p-3 bg-slate-900/50 hover:bg-k-blue/20 rounded-full border border-slate-700 transition-colors z-20 group"
              title="Edit Manually"
            >
              <Edit3 className={`h-5 w-5 ${isManualMode ? 'text-k-blue' : 'text-slate-400'}`} />
            </button>

            <div className="grid md:grid-cols-2 gap-12 items-center relative z-10">
              <div className="space-y-8">
                <div className="flex items-center gap-4 text-k-pink">
                  <div className="p-3 bg-k-pink/10 rounded-2xl">
                    <User className="h-8 w-8" />
                  </div>
                  {isManualMode ? (
                    <input
                      value={idolData.name}
                      onChange={(e) => setIdolData({ ...idolData, name: e.target.value })}
                      className="bg-slate-900 border-b-2 border-k-pink text-3xl font-black uppercase tracking-tighter outline-none w-full"
                    />
                  ) : (
                    <h3 className="text-3xl font-black uppercase tracking-tighter">{idolData.name}</h3>
                  )}
                </div>

                <div className="grid grid-cols-1 gap-4">
                  {/* Birth Date Field */}
                  <div className={`flex items-center gap-4 bg-slate-900/80 p-5 rounded-2xl border ${isManualMode && !idolData.birth_date ? 'border-red-500/50' : 'border-slate-700/50'}`}>
                    <Calendar className={`h-6 w-6 ${isManualMode && !idolData.birth_date ? 'text-red-400' : 'text-k-blue'}`} />
                    <div className="flex-1">
                      <div className="flex justify-between items-center mb-1">
                        <p className="text-[10px] text-slate-500 uppercase font-black tracking-widest">Birth Date</p>
                        {isManualMode && !idolData.birth_date && (
                          <span className="text-[9px] font-black bg-red-500 text-white px-2 py-0.5 rounded-full animate-pulse">{t('required')}</span>
                        )}
                      </div>
                      {isManualMode ? (
                        <input
                          type="text"
                          placeholder="YYYY-MM-DD"
                          maxLength={10}
                          value={idolData.birth_date}
                          onChange={(e) => {
                            const raw = e.target.value.replace(/\D/g, '').slice(0, 8);
                            let formatted = raw;
                            if (raw.length > 4) formatted = `${raw.slice(0, 4)}-${raw.slice(4)}`;
                            if (raw.length > 6) formatted = `${formatted.slice(0, 7)}-${raw.slice(6)}`;
                            setIdolData({ ...idolData, birth_date: formatted });
                          }}
                          className={`bg-transparent text-xl font-bold outline-none w-full border-b transition-colors ${idolData.birth_date.length === 10 && !isValidDate(idolData.birth_date)
                            ? 'text-red-400 border-red-500'
                            : 'text-white border-slate-700 focus:border-k-blue'
                            }`}
                        />
                      ) : (
                        <p className="text-xl font-bold">{idolData.birth_date || 'Unknown'}</p>
                      )}
                    </div>
                  </div>


                  {/* MBTI Field */}
                  <div className="flex items-center gap-4 bg-slate-900/80 p-5 rounded-2xl border border-slate-700/50 relative">
                    <BrainCircuit className="h-6 w-6 text-k-purple" />
                    <div className="flex-1">
                      <p className="text-[10px] text-slate-500 uppercase font-black tracking-widest">MBTI-T/A</p>
                      {isManualMode ? (
                        <input
                          ref={mbtiInputRef}
                          type="text"
                          placeholder="e.g. ENFJ-T"
                          value={idolData.mbti}
                          onChange={(e) => setIdolData({ ...idolData, mbti: e.target.value })}
                          className="bg-transparent text-xl font-bold text-k-purple outline-none w-full border-b border-slate-700"
                        />
                      ) : (
                        <p className="text-xl font-bold text-k-purple">{idolData.mbti || 'Unknown'}</p>
                      )}
                    </div>
                    {(!idolData.mbti || idolData.mbti === 'Unknown') && (
                      <button
                        onClick={handleAssistantSearch}
                        disabled={assistantLoading}
                        className="absolute right-3 md:right-4 top-1/2 -translate-y-1/2 p-2 md:px-3 md:py-1.5 bg-gradient-to-r from-blue-600/20 to-indigo-600/20 hover:from-blue-600/40 hover:to-indigo-600/40 rounded-lg text-xs font-bold text-blue-300 border border-blue-500/30 flex items-center justify-center transition-all shadow-sm"
                        title="구글 검색으로 자동 수집"
                      >
                        {assistantLoading ? <RefreshCcw className="h-4 w-4 animate-spin" /> : <Search className="h-4 w-4" />}
                        <span className="hidden md:inline md:ml-1">구글 자동 수집</span>
                      </button>
                    )}
                  </div>
                </div>
              </div>

              <div className="relative group">
                <div className="absolute inset-0 bg-gradient-to-br from-k-purple/30 to-k-blue/30 rounded-[2.5rem] blur-2xl group-hover:blur-3xl transition-all"></div>
                <div className={`relative bg-slate-900 rounded-[2rem] flex flex-col border-2 border-slate-700 p-5 md:p-8 shadow-inner w-full ${!analysisResult ? 'aspect-square items-center justify-center text-center' : 'min-h-[400px]'}`}>
                  {!analysisResult ? (
                    <>
                      <Sparkles className="h-20 w-16 text-k-pink mb-6 animate-pulse" />
                      <h3 className="text-2xl font-bold mb-3">{t('checkComp')}</h3>
                      <p className="text-slate-400 text-sm leading-relaxed mb-8">
                        {t('connectDestiny', { name: idolData.name })}
                      </p>
                      <motion.button
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => runFullAnalysis(false)}
                        disabled={analyzing}
                        className="w-full py-4 bg-gradient-to-r from-k-purple to-k-blue rounded-2xl font-black text-lg shadow-xl flex items-center justify-center gap-3 active:scale-95"
                      >
                        {analyzing ? <RefreshCcw className="h-5 w-5 animate-spin" /> : t('runAnalysis')}
                      </motion.button>
                    </>
                  ) : (
                    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="w-full text-left mt-4">

                      {/* Category Selection */}
                      <div className="grid grid-cols-1 gap-3 mb-6">
                        <button
                          onClick={() => setActiveTab('saju')}
                          className={`flex items-center justify-between px-6 py-4 rounded-2xl border-2 transition-all ${activeTab === 'saju' ? 'bg-k-pink/10 border-k-pink text-k-pink shadow-[0_0_15px_rgba(236,72,153,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-k-pink/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base">{t('tabSaju')}</span>
                          <span className="text-xl opacity-80">🔮</span>
                        </button>
                        <button
                          onClick={() => setActiveTab('fortune')}
                          className={`flex items-center justify-between px-6 py-4 rounded-2xl border-2 transition-all ${activeTab === 'fortune' ? 'bg-yellow-500/10 border-yellow-500 text-yellow-500 shadow-[0_0_15px_rgba(234,179,8,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-yellow-500/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base">{t('tabFortune')}</span>
                          <span className="text-xl opacity-80">📅</span>
                        </button>
                        <button
                          onClick={() => setActiveTab('signal')}
                          className={`flex items-center justify-between px-6 py-4 rounded-2xl border-2 transition-all ${activeTab === 'signal' ? 'bg-k-blue/10 border-k-blue text-k-blue shadow-[0_0_15px_rgba(59,130,246,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-k-blue/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base">{t('tabSignal', { name: analysisResult.chemistry_signal?.idol_name || idolData.name })}</span>
                          <span className="text-xl opacity-80">💖</span>
                        </button>
                      </div>

                      {/* Category Content */}
                      <div className="min-h-[300px]">
                        {/* 탭 1: 내 사주 요약 */}
                        {activeTab === 'saju' && (
                          <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-slate-800/60 rounded-2xl p-6 mb-4 border border-slate-700/50 shadow-lg h-full">
                            <h4 className="text-2xl font-black mb-4 text-white">{analysisResult.user_saju?.summary || analysisResult.label}</h4>
                            <div className="text-slate-300 text-sm leading-relaxed whitespace-pre-wrap">
                              {analysisResult.user_saju?.content || '사주 분석 결과가 생성되었습니다.'}
                            </div>
                          </motion.div>
                        )}

                        {/* 탭 2: 올해의 K-운세 (월별 캘린더 가로 스크롤) */}
                        {activeTab === 'fortune' && analysisResult.monthly_fortune && (
                          <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-slate-800/60 rounded-2xl p-6 mb-4 border border-slate-700/50 shadow-lg h-full">
                            <div className="flex flex-col gap-4">
                              {analysisResult.monthly_fortune.map((mf: any, idx: number) => (
                                <div key={idx} className="bg-slate-900/80 p-5 rounded-xl border border-slate-700/30">
                                  <div className="flex items-center gap-3 mb-2">
                                    <div className="text-sm font-black text-yellow-500 bg-yellow-500/10 px-2 py-1 rounded-md">{mf.month}월</div>
                                    <div className="text-base font-black text-white">{mf.keyword}</div>
                                  </div>
                                  <div className="text-sm text-slate-300 leading-relaxed pl-2 border-l-2 border-slate-700">{mf.desc}</div>
                                </div>
                              ))}
                            </div>
                          </motion.div>
                        )}

                        {/* 탭 3: 아이돌 궁합 시그널 */}
                        {activeTab === 'signal' && analysisResult.chemistry_signal && (
                          <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-gradient-to-br from-k-purple/10 to-k-blue/10 rounded-2xl p-6 mb-4 border border-k-purple/20 shadow-lg h-full">
                            <div className="mb-6 relative">
                              <div className="absolute top-0 left-0 w-1.5 h-full bg-gradient-to-b from-k-pink to-k-purple rounded-full"></div>
                              <div className="pl-6 py-3">
                                <h4 className="text-xl font-bold mb-3 text-white flex items-center gap-2">
                                  <Sparkles className="h-5 w-5 text-k-pink" />
                                  시너지
                                </h4>
                                <p className="text-lg md:text-xl text-slate-200 leading-relaxed font-medium italic opacity-95">
                                  "{analysisResult.chemistry_signal.synergy}"
                                </p>
                              </div>
                            </div>
                            <div className="space-y-6">
                              <div className="bg-slate-900/40 p-5 rounded-xl border border-slate-700/30">
                                <span className="font-bold text-k-purple block mb-2 text-lg">상대방 성향 🔮</span>
                                <p className="text-sm text-slate-200 leading-relaxed">
                                  {analysisResult.chemistry_signal.idol_love_style}
                                </p>
                              </div>
                              <div className="bg-slate-900/50 rounded-xl p-5 border border-slate-700/30">
                                <p className="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2"><Sparkles className="h-4 w-4 text-yellow-400" /> 공략 꿀팁</p>
                                <ul className="list-disc list-inside text-sm text-slate-300 space-y-2 marker:text-k-pink">
                                  {analysisResult.chemistry_signal.tips.map((tip: string, idx: number) => (
                                    <li key={idx} className="leading-relaxed">{tip}</li>
                                  ))}
                                </ul>
                              </div>
                            </div>
                          </motion.div>
                        )}
                      </div>

                      <style dangerouslySetInnerHTML={{
                        __html: `
                        .custom-scrollbar::-webkit-scrollbar { height: 6px; }
                        .custom-scrollbar::-webkit-scrollbar-track { background: rgba(30, 41, 59, 0.5); border-radius: 10px; }
                        .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(99, 102, 241, 0.5); border-radius: 10px; }
                        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(236, 72, 153, 0.5); }
                      `}} />

                      <motion.button
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        onClick={handleShare}
                        className="w-full py-4 bg-white text-slate-900 rounded-2xl font-black text-lg hover:bg-slate-100 transition-all flex items-center justify-center gap-2 shadow-xl"
                      >
                        <Share2 className="h-5 w-5" /> {t('shareResult')}
                      </motion.button>
                    </motion.div>
                  )}
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* MBTI Quiz Modal */}
      {showMBTIQuiz && (
        <QuickMBTI
          onComplete={(mbti) => {
            setUserMBTI(mbti);
            setShowMBTIQuiz(false);
          }}
          onClose={() => setShowMBTIQuiz(false)}
        />
      )}

      <footer className="mt-20 text-center text-slate-600 pb-10">
        <div className="flex justify-center gap-6 mb-6">
          <div className="bg-slate-900/50 px-5 py-3 border border-slate-700/50 rounded-2xl shadow-inner">
            <p className="text-[10px] uppercase font-bold text-slate-500 tracking-widest mb-1">{t('visitorsToday')}</p>
            <p className="text-xl font-black text-white">1,024</p>
          </div>
          <div className="bg-slate-900/50 px-5 py-3 border border-slate-700/50 rounded-2xl shadow-inner">
            <p className="text-[10px] uppercase font-bold text-slate-500 tracking-widest mb-1">{t('visitorsTotal')}</p>
            <p className="text-xl font-black text-k-purple">45,910</p>
          </div>
        </div>
        <p className="text-xs font-bold tracking-widest uppercase">{t('footer')}</p>
      </footer>
    </div>
  );
};

export default App;
