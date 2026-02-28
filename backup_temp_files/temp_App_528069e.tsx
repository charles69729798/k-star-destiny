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
    footer: "Crafted with 💜 by Abancha · K-Saju AI Engine",
    youLabel: "YOU",
    harmony: "Harmony ✨",
    resonance: "Resonance 🔮",
    tension: "Tension ⚡",
    mbtiMissing: "No MBTI",
    mbtiHint: "Add MBTI for better compatibility! 🎯",
    autoDetect: "🔍 Auto-detect",
    deepBond: "Deep Bond 💜",
    soulmate: "Soulmate 🔥",
    destiny: "Destiny 👑✨",
    selectType: "Select Type",
    enterManually: "AI could not find data. Please enter manually.",
    analysisError: "Failed to analyze. Check your input data.",
    birthDateAlert: "Please enter your birth date...",
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
    visitorsTotal: "Total Visitors",
    modeIdol: "Find an Idol",
    modeFriend: "Match with a Friend",
    friendNameLabel: "Friend's Name",
    friendNamePlaceholder: "Enter friend's name",
    findFriendMbti: "Find Friend's MBTI"
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
    footer: "Abancha가 💜로 만들었어요 · K-사주 AI 엔진",
    youLabel: "나",
    harmony: "상생 ✨",
    resonance: "비화 🔮",
    tension: "상극 ⚡",
    mbtiMissing: "MBTI 미입력",
    mbtiHint: "MBTI를 입력하면 궁합 정확도 UP! 🎯",
    autoDetect: "🔍 자동수집",
    deepBond: "깊은 인연 💜",
    soulmate: "소울메이트 🔥",
    destiny: "천생연분 👑✨",
    selectType: "유형 선택",
    enterManually: "AI가 데이터를 찾지 못했습니다. 직접 입력해 주세요.",
    analysisError: "분석에 실패했습니다. 입력 데이터를 확인해 주세요.",
    birthDateAlert: "본인의 생일을 입력해 주세요...",
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
    visitorsTotal: "누적 접속자",
    modeIdol: "스타 매칭하기",
    modeFriend: "지인과 매칭하기",
    friendNameLabel: "지인 이름",
    friendNamePlaceholder: "친구의 이름을 알려주세요",
    findFriendMbti: "친구의 MBTI 알아보기"
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
    footer: "Creado con 💜 por Abancha · K-Saju AI Engine",
    youLabel: "TÚ",
    harmony: "Armonía ✨",
    resonance: "Resonancia 🔮",
    tension: "Tensión ⚡",
    mbtiMissing: "Sin MBTI",
    mbtiHint: "¡Agrega MBTI para mejor compatibilidad! 🎯",
    autoDetect: "🔍 Auto-detectar",
    deepBond: "Vínculo Profundo 💜",
    soulmate: "Alma Gemela 🔥",
    destiny: "Destino 👑✨",
    selectType: "Seleccionar Tipo",
    enterManually: "La IA no pudo encontrar datos. Ingresa manualmente.",
    analysisError: "Error en el análisis. Verifica tus datos.",
    birthDateAlert: "Por favor, ingresa tu fecha de nacimiento...",
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
    visitorsTotal: "Visitantes Totales",
    modeIdol: "Encontrar un Ídolo",
    modeFriend: "Coincidir con un Amigo",
    friendNameLabel: "Nombre del Amigo",
    friendNamePlaceholder: "Ingresa el nombre del amigo",
    findFriendMbti: "Encuentra el MBTI del Amigo"
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
  const [quizForFriend, setQuizForFriend] = useState(false); // 자신이 아닌 친구/지인 대상 퀴즈인지 구분

  // App Mode State
  const [isFriendMode, setIsFriendMode] = useState(false);

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
  const [completedMissions, setCompletedMissions] = useState<string[]>([]);
  const [expandedMission, setExpandedMission] = useState<string | null>(null);
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
      // 프로필 영역으로 스크롤하여 사용자에게 안내
      document.getElementById('user-profile-section')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
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
    <div className="container mx-auto px-0 md:px-4 py-6 md:py-10 max-w-4xl min-h-screen relative z-10">
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
      <section id="user-profile-section" className="bg-transparent md:bg-slate-800/30 border-none md:border md:border-slate-700/50 rounded-none md:rounded-3xl p-3 md:p-6 mb-8 backdrop-blur-none md:backdrop-blur-sm shadow-none md:shadow-xl">
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

      {/* Mode Switcher */}
      <div className="flex justify-center mb-8">
        <div className="bg-slate-800/80 p-1.5 rounded-full border border-slate-700/50 flex space-x-2">
          <button
            onClick={() => {
              setIsFriendMode(false);
              setErrorMessage(null);
            }}
            className={`px-6 py-2 rounded-full font-bold text-sm transition-all ${!isFriendMode ? 'bg-k-purple text-white shadow-lg' : 'text-slate-400 hover:text-white'}`}
          >
            {t('modeIdol')}
          </button>
          <button
            onClick={() => {
              setIsFriendMode(true);
              setErrorMessage(null);
              setIdolData({ name: '', gender: 'male', birth_date: '', mbti: '' }); // 지인 초기화
            }}
            className={`px-6 py-2 rounded-full font-bold text-sm transition-all ${isFriendMode ? 'bg-k-blue text-white shadow-lg' : 'text-slate-400 hover:text-white'}`}
          >
            {t('modeFriend')}
          </button>
        </div>
      </div>

      {/* Search Bar OR Friend Input */}
      <div className="max-w-2xl mx-auto mb-16">
        {!isFriendMode ? (
          <>
            <div className="mb-4 ml-0 md:ml-2">
              <label className="text-xl font-bold text-k-blue flex items-center gap-2 mb-1">
                <Sparkles className="h-5 w-5" /> {t('searchLabel')}
              </label>
              <p className="text-slate-500 text-sm">{t('searchDescription')}</p>
            </div>
            <form onSubmit={handleSearch} className="relative group px-1 md:px-0">
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
                        <img
                          src={c.thumbnail || `https://api.dicebear.com/7.x/avataaars/svg?seed=${c.title || 'idol'}`}
                          alt={c.title}
                          className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity"
                          onError={(e: any) => {
                            e.target.src = "https://api.dicebear.com/7.x/avataaars/svg?seed=" + (c.title || "idol");
                          }}
                        />
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
                        src={`/avatars/${idol.gender === 'male' ? 'male' : 'female'}_${(idx % 4) + 1}.png`}
                        alt={idol.name_en}
                        className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity"
                      />
                    </div>
                    <p className="text-xs font-black text-white truncate mb-0.5">{lang === 'ko' ? idol.name_kr : idol.name_en}</p>
                    <p className="text-[10px] text-slate-500 font-bold uppercase tracking-tight">{idol.group}</p>
                  </motion.button>
                ))}
              </motion.div>
            </div>
          </>
        ) : (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="bg-slate-800/40 border border-k-blue/30 rounded-3xl p-6 shadow-2xl"
          >
            <h3 className="text-lg font-bold text-k-blue mb-4">{t('modeFriend')}</h3>
            <div className="grid md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <label className="text-xs font-bold text-slate-400 ml-1">{t('friendNameLabel')}</label>
                <input
                  type="text"
                  placeholder={t('friendNamePlaceholder')}
                  value={idolData?.name || ''}
                  onChange={(e) => setIdolData((prev: any) => ({ ...prev, name: e.target.value }))}
                  className="w-full bg-slate-900 border-2 border-slate-700 rounded-xl px-4 py-3 focus:border-k-blue outline-none transition-all text-white"
                />
              </div>
              <div className="space-y-2">
                <label className="text-xs font-bold text-slate-400 ml-1">{t('gender')}</label>
                <select
                  value={idolData?.gender || 'male'}
                  onChange={(e) => setIdolData((prev: any) => ({ ...prev, gender: e.target.value }))}
                  className="w-full bg-slate-900 border-2 border-slate-700 rounded-xl px-4 py-3 focus:border-k-blue outline-none transition-all text-white"
                >
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
              <div className="space-y-2">
                <label className="text-xs font-bold text-slate-400 ml-1">{t('birthDate')}</label>
                <input
                  type="text"
                  placeholder="YYYY-MM-DD"
                  value={idolData?.birth_date || ''}
                  onChange={(e) => setIdolData((prev: any) => ({ ...prev, birth_date: e.target.value }))}
                  className="w-full bg-slate-900 border-2 border-slate-700 rounded-xl px-4 py-3 focus:border-k-blue outline-none transition-all text-white"
                />
              </div>
              <div className="space-y-2">
                <div className="flex justify-between items-center mb-1">
                  <label className="text-xs font-bold text-slate-400 ml-1">MBTI</label>
                  <button
                    onClick={() => { setQuizForFriend(true); setShowMBTIQuiz(true); }}
                    className="text-[10px] text-k-blue hover:underline font-bold"
                  >
                    {t('findFriendMbti')}
                  </button>
                </div>
                <input
                  type="text"
                  placeholder="e.g. ENFP"
                  value={idolData?.mbti || ''}
                  onChange={(e) => setIdolData((prev: any) => ({ ...prev, mbti: e.target.value.toUpperCase() }))}
                  className="w-full bg-slate-900 border-2 border-slate-700 rounded-xl px-4 py-3 focus:border-k-blue outline-none transition-all text-white"
                />
              </div>
            </div>
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              onClick={() => runFullAnalysis(false)}
              className="w-full mt-6 py-4 bg-gradient-to-r from-k-blue to-k-purple rounded-xl font-black text-lg shadow-lg flex items-center justify-center gap-2"
            >
              <Sparkles className="h-5 w-5" /> {t('runAnalysis')}
            </motion.button>
          </motion.div>
        )}
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
            className="bg-slate-800 rounded-2xl md:rounded-[2rem] p-4 md:p-10 border border-slate-700 shadow-2xl overflow-hidden relative"
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

            {/* ===== 아이돌 프로필 배너 (컴팩트) ===== */}
            <div className="flex flex-col items-center md:flex-row gap-4 bg-slate-900/80 rounded-2xl p-4 mb-6 border border-slate-700/50 relative z-10">
              <div className="flex items-center gap-4 flex-1 min-w-0">
                <div className="p-2 bg-k-pink/10 rounded-xl relative w-14 h-14 shrink-0 flex items-center justify-center">
                  <img
                    src={idolData.thumbnail || `https://api.dicebear.com/7.x/avataaars/svg?seed=${idolData.name}`}
                    alt={idolData.name}
                    className="w-full h-full object-cover rounded-xl opacity-90"
                    onError={(e: any) => {
                      e.target.src = "https://api.dicebear.com/7.x/avataaars/svg?seed=" + idolData.name;
                    }}
                  />
                </div>
                <div className="min-w-0">
                  {isManualMode ? (
                    <div className="flex flex-col gap-1">
                      <label className="text-[10px] font-bold text-k-pink/60 uppercase tracking-widest pl-1">Idol Name</label>
                      <input
                        value={idolData.name}
                        onChange={(e) => setIdolData({ ...idolData, name: e.target.value })}
                        className="bg-slate-800/50 border-b-2 border-k-pink text-xl font-black uppercase tracking-tighter outline-none w-full px-2 py-1 rounded-t-lg transition-all focus:bg-slate-800"
                      />
                    </div>
                  ) : (
                    <>
                      <h3 className="text-xl font-black uppercase tracking-tighter text-k-pink">{idolData.name}</h3>
                      <p className="text-xs text-slate-400 mt-0.5">
                        📅 {idolData.birth_date || 'Unknown'} · 🧠 {idolData.mbti || 'Unknown'}
                      </p>
                    </>
                  )}
                </div>
              </div>
              {/* 수동 편집을 위한 추가 필드들 (수동 모드일 때만 표시) */}
              {isManualMode && (
                <div className="flex flex-wrap items-center gap-4 p-4 bg-slate-800/30 rounded-xl border border-slate-700/30 flex-shrink-0">
                  <div className="flex flex-col gap-1">
                    <label className="text-[10px] font-bold text-k-blue/60 uppercase tracking-widest flex items-center gap-1">
                      <Calendar className="h-3 w-3" /> Birth Date
                    </label>
                    <input type="text" placeholder="YYYY-MM-DD" maxLength={10} value={idolData.birth_date}
                      onChange={(e) => {
                        const raw = e.target.value.replace(/\D/g, '').slice(0, 8);
                        let formatted = raw;
                        if (raw.length > 4) formatted = `${raw.slice(0, 4)}-${raw.slice(4)}`;
                        if (raw.length > 6) formatted = `${formatted.slice(0, 7)}-${raw.slice(6)}`;
                        setIdolData({ ...idolData, birth_date: formatted });
                      }}
                      className="bg-slate-900/60 text-sm font-bold outline-none w-32 px-3 py-2 rounded-lg border border-slate-700 focus:border-k-blue text-white transition-all"
                    />
                  </div>
                  <div className="flex flex-col gap-1">
                    <label className="text-[10px] font-bold text-k-purple/60 uppercase tracking-widest flex items-center gap-1">
                      <BrainCircuit className="h-3 w-3" /> MBTI
                    </label>
                    <input ref={mbtiInputRef} type="text" placeholder="MBTI" value={idolData.mbti}
                      onChange={(e) => setIdolData({ ...idolData, mbti: e.target.value })}
                      className="bg-slate-900/60 text-sm font-bold text-k-purple outline-none w-24 px-3 py-2 rounded-lg border border-slate-700 focus:border-k-purple transition-all placeholder:text-slate-600"
                    />
                  </div>
                  {(!idolData.mbti || idolData.mbti === 'Unknown') && (
                    <div className="flex flex-col gap-2 min-w-[200px]">
                      <div className="flex items-center gap-2">
                        <span className="text-[10px] font-bold text-amber-400 bg-amber-500/10 px-2 py-1 rounded-full border border-amber-500/30 animate-pulse whitespace-nowrap">
                          ⚠️ {t('mbtiMissing')}
                        </span>
                        <button onClick={handleAssistantSearch} disabled={assistantLoading}
                          className="px-4 py-2 bg-blue-600/20 hover:bg-blue-600/40 rounded-lg text-xs font-bold text-blue-200 border border-blue-400/30 flex items-center gap-1.5 transition-all shadow-[0_0_15px_rgba(59,130,246,0.1)]"
                        >
                          {assistantLoading ? <RefreshCcw className="h-3 w-3 animate-spin" /> : <Search className="h-3 w-3" />}
                          {t('autoDetect')}
                        </button>
                      </div>
                      <p className="text-[10px] text-amber-300/60 font-medium italic">{t('mbtiHint')}</p>
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* ===== 분석 결과 영역 (전체 폭) ===== */}
            <div className="relative z-10 -mx-1 md:mx-0">
              <div className="relative group">
                <div className="hidden md:block absolute inset-0 bg-gradient-to-br from-k-purple/30 to-k-blue/30 rounded-[2.5rem] blur-2xl group-hover:blur-3xl transition-all"></div>
                <div className={`relative bg-transparent md:bg-slate-900 rounded-none md:rounded-[2rem] flex flex-col border-none md:border-2 md:border-slate-700 p-3 md:p-8 shadow-none md:shadow-inner w-full ${!analysisResult ? 'aspect-square items-center justify-center text-center' : 'min-h-[400px]'}`}>
                  {!analysisResult ? (
                    <>
                      <Sparkles className="h-20 w-16 text-k-pink mb-6 animate-pulse" />
                      <h3 className="text-2xl font-bold mb-3">{t('checkComp')}</h3>
                      <p className="text-slate-400 text-sm leading-relaxed mb-4">
                        {t('connectDestiny', { name: idolData.name })}
                      </p>
                      {errorMessage && (
                        <div className="w-full mb-4 px-4 py-3 bg-red-500/10 border border-red-500/30 rounded-xl text-red-300 text-sm font-bold flex items-center gap-2 animate-pulse">
                          <HelpCircle className="h-4 w-4 flex-shrink-0" />
                          {errorMessage}
                        </div>
                      )}
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
                      <div className="grid grid-cols-1 gap-2 mb-6 px-1 md:px-0">
                        <button
                          onClick={() => setActiveTab('saju')}
                          className={`flex items-center justify-between px-5 py-4 rounded-xl md:rounded-2xl border-2 transition-all ${activeTab === 'saju' ? 'bg-k-pink/10 border-k-pink text-k-pink shadow-[0_0_15px_rgba(236,72,153,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-k-pink/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base">{t('tabSaju')}</span>
                          <span className="text-xl opacity-80">🔮</span>
                        </button>
                        <button
                          onClick={() => setActiveTab('fortune')}
                          className={`flex items-center justify-between px-5 py-4 rounded-xl md:rounded-2xl border-2 transition-all ${activeTab === 'fortune' ? 'bg-yellow-500/10 border-yellow-500 text-yellow-500 shadow-[0_0_15px_rgba(234,179,8,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-yellow-500/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base">{t('tabFortune')}</span>
                          <span className="text-xl opacity-80">📅</span>
                        </button>
                        <button
                          onClick={() => setActiveTab('signal')}
                          className={`flex items-center justify-between px-5 py-4 rounded-xl md:rounded-2xl border-2 transition-all ${activeTab === 'signal' ? 'bg-k-blue/10 border-k-blue text-k-blue shadow-[0_0_15px_rgba(59,130,246,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-k-blue/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base">{t('tabSignal', { name: analysisResult.chemistry_signal?.idol_name || idolData.name })}</span>
                          <span className="text-xl opacity-80">💖</span>
                        </button>
                      </div>

                      {/* Category Content */}
                      <div className="min-h-[300px]">
                        {/* 탭 1: 내 사주 요약 */}
                        {activeTab === 'saju' && (
                          <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-transparent md:bg-slate-800/60 rounded-none md:rounded-2xl p-4 md:p-6 mb-4 border-b md:border border-slate-700/50 shadow-none md:shadow-lg h-full">
                            <div className="flex items-center gap-2 mb-3 px-3 py-1.5 bg-indigo-500/10 border border-indigo-500/30 rounded-lg w-fit">
                              <span className="text-indigo-400 text-xs font-black uppercase tracking-widest">🔮 나의 사주 분석 결과</span>
                            </div>
                            <h4 className="text-2xl font-black mb-4 text-white px-1">{analysisResult.user_saju?.summary || analysisResult.label}</h4>
                            <div className="text-slate-300 text-sm leading-relaxed whitespace-pre-wrap px-1">
                              {analysisResult.user_saju?.content || '사주 분석 결과가 생성되었습니다.'}
                            </div>
                          </motion.div>
                        )}

                        {/* 탭 2: 올해의 K-운세 (월별 캘린더 가로 스크롤) */}
                        {activeTab === 'fortune' && analysisResult.monthly_fortune && (
                          <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-transparent md:bg-slate-800/60 rounded-none md:rounded-2xl p-4 md:p-6 mb-4 border-none md:border border-slate-700/50 shadow-none md:shadow-lg h-full">
                            <div className="flex flex-col gap-3">
                              {analysisResult.monthly_fortune.map((mf: any, idx: number) => (
                                <div key={idx} className="bg-slate-900 md:bg-slate-900/80 p-4 md:p-5 rounded-xl border border-slate-700/30 shadow-sm">
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
                          <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-transparent md:bg-gradient-to-br md:from-k-purple/10 md:to-k-blue/10 rounded-none md:rounded-2xl p-4 md:p-6 mb-4 border-none md:border border-k-purple/20 shadow-none md:shadow-lg h-full">

                            {/* ===== 오행 연결선 인포그래픽 ===== */}
                            <div className="flex items-center justify-center gap-4 mb-6 p-5 bg-slate-900/60 rounded-2xl border border-slate-700/40">
                              <div className="text-center">
                                <div className="w-16 h-16 bg-gradient-to-br from-blue-500/20 to-cyan-500/20 rounded-full flex items-center justify-center border-2 border-blue-400/50 mb-2 mx-auto">
                                  <span className="text-2xl">{analysisResult.user_saju?.element === 'Wood' ? '🌲' : analysisResult.user_saju?.element === 'Fire' ? '🔥' : analysisResult.user_saju?.element === 'Earth' ? '⛰️' : analysisResult.user_saju?.element === 'Metal' ? '⚔️' : '🌊'}</span>
                                </div>
                                <p className="text-xs font-black text-blue-300 uppercase">{t('youLabel')}</p>
                                <p className="text-[10px] text-slate-500">{analysisResult.user_saju?.element || '?'}</p>
                              </div>

                              {(() => {
                                const baseScore = analysisResult.chemistry_signal.base_synergy_score || 52;
                                const missions = analysisResult.chemistry_signal.synergy_missions || [];
                                const totalBoost = missions.filter((m: any) => completedMissions.includes(m.id)).reduce((s: number, m: any) => s + m.boost, 0);
                                const score = Math.min(100, baseScore + totalBoost);
                                const lineColor = score >= 100 ? 'from-pink-400 via-yellow-300 to-pink-400' : score >= 86 ? 'from-emerald-400 to-cyan-400' : score >= 71 ? 'from-purple-400 to-pink-400' : score >= 51 ? 'from-yellow-400 to-amber-400' : 'from-red-500 to-orange-400';
                                const lineH = score >= 100 ? 'h-3' : score >= 86 ? 'h-2.5' : score >= 71 ? 'h-2' : score >= 51 ? 'h-1.5' : 'h-1';
                                const lineShadow = score >= 100 ? 'shadow-[0_0_16px_rgba(236,72,153,0.7)]' : score >= 86 ? 'shadow-[0_0_12px_rgba(52,211,153,0.5)]' : 'shadow-[0_0_8px_rgba(168,85,247,0.5)]';
                                const lineLabel = score >= 100 ? t('destiny') : score >= 86 ? t('soulmate') : score >= 71 ? t('deepBond') : score >= 51 ? t('resonance') : t('tension');
                                const labelColor = score >= 100 ? 'text-yellow-300' : score >= 86 ? 'text-emerald-300' : score >= 71 ? 'text-purple-300' : score >= 51 ? 'text-amber-300' : 'text-red-400';
                                const borderColor = score >= 100 ? 'border-yellow-400' : score >= 86 ? 'border-emerald-400' : score >= 71 ? 'border-purple-400' : score >= 51 ? 'border-amber-400' : 'border-red-400';
                                return (
                                  <div className={`flex-1 relative transition-all duration-700 ${score >= 100 ? '-mx-8' : 'mx-2'}`}>
                                    <motion.div
                                      initial={{ scaleX: 0 }}
                                      animate={{ scaleX: score >= 100 ? 1.05 : 1 }}
                                      transition={{ duration: 1, ease: 'easeOut' }}
                                      className={`${lineH} bg-gradient-to-r ${lineColor} rounded-full ${lineShadow} transition-all duration-700 ${score >= 100 ? 'animate-pulse' : ''}`}
                                    />
                                    <motion.div
                                      initial={{ scale: 0 }}
                                      animate={{ scale: 1 }}
                                      transition={{ delay: 0.3, type: 'spring' }}
                                      className={`absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-slate-900 border-2 ${borderColor} rounded-full px-3 py-1 transition-all duration-500 z-10`}
                                    >
                                      <motion.span key={lineLabel} initial={{ opacity: 0, y: -5 }} animate={{ opacity: 1, y: 0 }} className={`text-xs font-black ${labelColor} whitespace-nowrap`}>
                                        {lineLabel}
                                      </motion.span>
                                    </motion.div>
                                    {score >= 100 && (
                                      <motion.div
                                        initial={{ opacity: 0 }}
                                        animate={{ opacity: 1 }}
                                        className="absolute -top-4 left-1/2 -translate-x-1/2 text-lg z-20"
                                      >
                                        ✨💖✨
                                      </motion.div>
                                    )}
                                  </div>
                                );
                              })()}

                              <div className="text-center">
                                <div className="w-16 h-16 bg-gradient-to-br from-purple-500/20 to-pink-500/20 rounded-full flex items-center justify-center border-2 border-purple-400/50 mb-2 mx-auto">
                                  <span className="text-2xl">⭐</span>
                                </div>
                                <p className="text-xs font-black text-purple-300 uppercase">{analysisResult.chemistry_signal.idol_name}</p>
                                <p className="text-[10px] text-slate-500">{analysisResult.chemistry_signal.idol_mbti}</p>
                              </div>
                            </div>

                            {/* ===== 궁합 게이지 바 (동적) ===== */}
                            {(() => {
                              const baseScore = analysisResult.chemistry_signal.base_synergy_score || 52;
                              const missions = analysisResult.chemistry_signal.synergy_missions || [];
                              const totalBoost = missions.filter((m: any) => completedMissions.includes(m.id)).reduce((sum: number, m: any) => sum + m.boost, 0);
                              const currentScore = Math.min(100, baseScore + totalBoost);
                              const levelName = currentScore >= 100 ? '👑 천생연분' : currentScore >= 86 ? '🔥 소울메이트' : currentScore >= 71 ? '💜 깊은 인연' : currentScore >= 51 ? '💛 공감 단계' : currentScore >= 31 ? '💫 관심 단계' : '🌱 운명의 시작';
                              return (
                                <div className="mb-6 p-4 bg-slate-900/40 rounded-xl border border-slate-700/30">
                                  <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-black text-white flex items-center gap-2">
                                      <Sparkles className="h-4 w-4 text-k-pink" /> SYNERGY LEVEL
                                    </span>
                                    <div className="text-right">
                                      <motion.span
                                        key={currentScore}
                                        initial={{ scale: 1.3, opacity: 0 }}
                                        animate={{ scale: 1, opacity: 1 }}
                                        className="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-k-pink to-k-purple block"
                                      >
                                        {currentScore}%
                                      </motion.span>
                                      <span className="text-[10px] text-slate-400 font-bold">{levelName}</span>
                                    </div>
                                  </div>
                                  <div className="w-full h-3 bg-slate-800 rounded-full overflow-hidden">
                                    <motion.div
                                      key={currentScore}
                                      initial={{ width: `${baseScore}%` }}
                                      animate={{ width: `${currentScore}%` }}
                                      transition={{ duration: 1.2, ease: 'easeOut' }}
                                      className={`h-full rounded-full ${currentScore >= 86 ? 'bg-gradient-to-r from-emerald-500 to-green-400' : currentScore >= 51 ? 'bg-gradient-to-r from-yellow-500 to-amber-400' : 'bg-gradient-to-r from-red-500 to-orange-400'}`}
                                    />
                                  </div>
                                </div>
                              );
                            })()}

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
                            <div className="space-y-4">
                              <div className="bg-slate-900 md:bg-slate-900/40 p-4 md:p-5 rounded-xl border border-slate-700/30">
                                <span className="font-bold text-k-purple block mb-2 text-lg px-1">상대방 성향 🔮</span>
                                <p className="text-sm text-slate-200 leading-relaxed px-1">
                                  {analysisResult.chemistry_signal.idol_love_style}
                                </p>
                              </div>
                              <div className="bg-slate-900/50 rounded-xl p-4 md:p-5 border border-slate-700/30">
                                <p className="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2 px-1"><Sparkles className="h-4 w-4 text-yellow-400" /> 공략 꿀팁</p>
                                <ul className="list-disc list-inside text-sm text-slate-300 space-y-2 marker:text-k-pink px-1">
                                  {analysisResult.chemistry_signal.tips.map((tip: string, idx: number) => (
                                    <li key={idx} className="leading-relaxed">{tip}</li>
                                  ))}
                                </ul>
                              </div>
                            </div>

                            {/* ===== 시너지 부스터 미션 카드 ===== */}
                            {analysisResult.chemistry_signal.synergy_missions && (
                              <div className="mt-6 p-5 bg-gradient-to-br from-slate-900/80 to-slate-800/60 rounded-2xl border border-k-purple/30">
                                <h4 className="text-lg font-black text-white mb-1 flex items-center gap-2">
                                  🎮 도전! 시너지 레벨 UP 치트키
                                </h4>
                                <p className="text-xs text-slate-400 mb-4">미션을 완료하면 시너지 레벨이 상승합니다!</p>
                                <div className="space-y-3">
                                  {analysisResult.chemistry_signal.synergy_missions.map((mission: any) => {
                                    const isCompleted = completedMissions.includes(mission.id);
                                    const lang = localStorage.getItem('lang') || 'ko';
                                    const mLabel = lang === 'en' ? mission.label_en : lang === 'es' ? mission.label_es : mission.label;
                                    return (
                                      <motion.div
                                        key={mission.id}
                                        layout
                                        whileTap={{ scale: 0.98 }}
                                        onClick={() => {
                                          if (isCompleted) {
                                            setCompletedMissions(prev => prev.filter(id => id !== mission.id));
                                          } else {
                                            setCompletedMissions(prev => [...prev, mission.id]);
                                          }
                                        }}
                                        className={`p-4 rounded-xl border cursor-pointer transition-all ${isCompleted
                                          ? 'bg-emerald-500/10 border-emerald-500/40'
                                          : 'bg-slate-900/40 border-slate-700/30 hover:border-k-pink/40'
                                          }`}
                                      >
                                        <div className="flex items-start gap-3">
                                          <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center flex-shrink-0 mt-0.5 transition-all ${isCompleted ? 'bg-emerald-500 border-emerald-400' : 'border-slate-600'
                                            }`}>
                                            {isCompleted && <span className="text-white text-xs">✓</span>}
                                          </div>
                                          <div className="flex-1">
                                            <div className="flex items-center justify-between">
                                              <span className={`text-sm font-bold ${isCompleted ? 'text-emerald-300 line-through' : 'text-white'}`}>
                                                {mLabel}
                                              </span>
                                              <span className="text-xs font-black text-k-pink bg-k-pink/10 px-2 py-0.5 rounded-full">
                                                +{mission.boost}%
                                              </span>
                                            </div>
                                            {/* 아코디언: reason + tasks */}
                                            {(() => {
                                              const isExpanded = expandedMission === mission.id;
                                              const mReason = lang === 'en' ? mission.reason_en : lang === 'es' ? mission.reason_es : mission.reason;
                                              const mTasks = lang === 'en' ? mission.tasks_en : lang === 'es' ? mission.tasks_es : mission.tasks;
                                              return (
                                                <>
                                                  <button
                                                    onClick={(e) => { e.stopPropagation(); setExpandedMission(isExpanded ? null : mission.id); }}
                                                    className="text-[11px] text-k-purple hover:text-k-pink mt-1.5 font-bold transition-colors"
                                                  >
                                                    {isExpanded ? '▲ 접기' : '▼ 상세보기'}
                                                  </button>
                                                  {isExpanded && mReason && (
                                                    <motion.div
                                                      initial={{ opacity: 0, height: 0 }}
                                                      animate={{ opacity: 1, height: 'auto' }}
                                                      exit={{ opacity: 0, height: 0 }}
                                                      className="mt-2 space-y-2"
                                                    >
                                                      <div className="bg-slate-800/60 rounded-lg p-3 border-l-2 border-k-purple">
                                                        <p className="text-[11px] text-slate-300 leading-relaxed">📖 {mReason}</p>
                                                      </div>
                                                      {mTasks && mTasks.length > 0 && (
                                                        <div className="bg-slate-800/40 rounded-lg p-3">
                                                          <p className="text-[11px] font-bold text-emerald-300 mb-1.5">✅ 수행과제</p>
                                                          <ul className="space-y-1">
                                                            {mTasks.map((task: string, ti: number) => (
                                                              <li key={ti} className="text-[11px] text-slate-300 flex items-start gap-1.5">
                                                                <span className="text-emerald-400 mt-0.5">•</span>
                                                                <span>{task}</span>
                                                              </li>
                                                            ))}
                                                          </ul>
                                                        </div>
                                                      )}
                                                    </motion.div>
                                                  )}
                                                </>
                                              );
                                            })()}
                                          </div>
                                        </div>
                                      </motion.div>
                                    );
                                  })}
                                </div>
                              </div>
                            )}
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
            if (quizForFriend) {
              setIdolData((prev: any) => ({ ...prev, mbti }));
              setQuizForFriend(false);
            } else {
              setUserMBTI(mbti);
            }
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
