import React, { useState, useRef, useEffect, useMemo } from 'react';
import axios from 'axios';
import { Search, Sparkles, User, Calendar, BrainCircuit, Share2, HelpCircle, RefreshCcw, Edit3, ThumbsUp, MessageSquare, Send, LayoutGrid, TrendingUp, Users, ChevronDown, Star, Heart, Zap, Target } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import QuickMBTI from './components/QuickMBTI';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';
const translations: any = {
  en: {
    title: "K-DESTINY AI",
    subtitle: "Saju + MBTI Matching for K-pop Fans",
    profile: "PROFILE",
    birthDate: "Birth Date",
    gender: "Gender",
    female: "female",
    male: "male",
    nonBinary: "nonbinary",
    mbti: "mbti",
    dontKnow: "dontKnow?",
    searchLabel: "Idol Search",
    searchDescription: "Enter your favorite K-pop star's name. AI will automatically find the info.",
    searchPlaceholder: "Enter idol name (e.g., IU, Jungkook, Go Youn-jung)...",
    aiMode: "AI Search",
    searching: "AI is searching data...",
    extracting: "AI is extracting data...",
    checkComp: "Check Compatibility",
    connectDestiny: "Connect your destiny with {name} via K-Saju algorithms.",
    runAnalysis: "Run Analysis",
    destinyEnergy: "Destiny Energy",
    shareResult: "Share Result",
    footer: "Made with 💜 by ABANCHA · K-Saju AI Engine",
    youLabel: "YOU",
    harmony: "Harmony ✨",
    resonance: "Resonance 🔮",
    tension: "Tension ⚡",
    mbtiMissing: "MBTI Missing",
    mbtiHint: "Add MBTI for higher accuracy! 🎯",
    autoDetect: "🔍 Auto-search",
    deepBond: "Deep Bond 💜",
    soulmate: "Soulmate 🔥",
    destiny: "Destiny 👑✨",
    selectType: "Select Type",
    enterManually: "AI could not find data. Please enter manually.",
    analysisError: "Analysis failed. Please check your data.",
    birthDateAlert: "Please enter your birth date...",
    required: "REQUIRED",
    copied: "Copied to clipboard!",
    trendingTitle: "Trending Idols",
    trendingSubtitle: "Select a star to check your destiny instantly.",
    tabSaju: "Soul Index: K-Saju and Lifetime Indicators",
    tabFortune: "2026 God-life Calendar: Monthly Dopamine & Luck Flow",
    tabSignal: "Destiny Signal: Cosmic Telepathy with {name} 📡",
    introTitle: "Find Your Destiny",
    introDesc: "It's time to connect your cosmic signals with K-stars. Who is your predestined type? Find out now!",
    birthDatePrompt: "Please enter your birth date first. The more accurate, the better!",
    mbtiPrompt: "Don't know the idol's name or MBTI? Click the search button or select from trending below!",
    visitorsToday: "Today's Challengers",
    visitorsTotal: "Total Visitors",
    modeIdol: "Match with Star",
    modeFriend: "Match with Friend",
    friendNameLabel: "Friend's Name",
    friendNamePlaceholder: "Enter friend's name",
    findFriendMbti: "Find Friend's MBTI",
    friendGenderLabel: "Friend's Gender",
    friendBirthLabel: "Friend's Birth Date",
    googleAutoFill: "Auto-fill with Google Search",
    googleAiSearch: "Auto-search with Google AI",
    searchingWiki: "Searching candidates on Wikipedia...",
    mbtiNotFound: "No MBTI information found",
    mbtiNotFoundDesc: "Knowing the idol's MBTI allows for more powerful analysis! What would you like to do?",
    inputManually: "I'll enter it myself",
    pureSajuOnly: "Analyze with pure Saju only",
    close: "Close",
    sameNameFound: "Multiple people found. Please select the correct one.",
    manualModeTitle: "Manual Mode",
    manualModeDesc: "AI could not find exact data. Please enter manually.",
    analysisSuccess: "Data input complete. Ready to analyze!",
    missionTitle: "🎮 Challenge! Synergy Level UP Cheat",
    missionDesc: "Complete missions to increase your synergy level!",
    expand: "▼ View Details",
    collapse: "▲ Collapse",
    tasksHeader: "✅ Tasks",
    userSajuResult: "🔮 Your Saju Analysis Result",
    sajuSuccess: "Saju analysis result has been generated.",
    idolTraits: "Idol's Personality 🔮",
    attackTips: "Success Tips",
    levelDestiny: "👑 Destiny",
    levelSoulmate: "🔥 Soulmate",
    levelDeepBond: "💜 Deep Bond",
    levelResonance: "💛 Resonance",
    levelInterest: "💫 Interest",
    levelStart: "🌱 Starting Point",
    feedbackTitle: "💬 Soul Reactions & Stories",
    feedbackDesc: "Share your results anonymously! What's your vibe today?",
    placeholderFeedback: "Write a message or a wish...",
    post: "POST",
    reactions: "Reactions",
    communityTitle: "Soul Community",
    communitySubtitle: "Real-time reactions from the galaxy",
    addComment: "Add a public comment...",
    cancel: "Cancel",
    comment: "Comment",
    posting: "Posting...",
    reply: "REPLY",
    lifetimeTitle: "🌟 [Lifetime Destiny Path]",
    lifetimeDesc: "Your soul's blueprint based on Gyeokguk analysis.",
    mbti_select_title: "Select MBTI",
    lifetimeStageTitle: "🌟 [Lifetime Destiny Path]",
    visitor_count: "Total Visitors: {count}",
    expertHealth: "Health Advice",
    expertWealth: "Wealth Advice",
    expertCareer: "Career Advice",
    expertLove: "Love Advice",
    expertCommentTitle: "Expert consultants' comments",
    commentsCount: "Comments ({count})",
    mbtiNotFoundTitle: "MBTI information missing",
    friendInfoTitle: "FRIEND / PARTNER INFO",
    invalidDate: "Invalid date format",
    stage: "STAGE"
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
    searching: "AI가 데이터를 찾는 중...",
    extracting: "AI가 데이터를 추출하는 중...",
    checkComp: "궁합 확인하기",
    connectDestiny: "{name}님과 당신의 운명을 K-사주 알고리즘으로 연결합니다.",
    runAnalysis: "분석하기",
    destinyEnergy: "데스티니 에너지",
    shareResult: "결과 공유하기",
    footer: "ABANCHA가 💜로 만들었음 · K-사주 AI 엔진",
    youLabel: "나",
    harmony: "조화 ✨",
    resonance: "공감 🔮",
    tension: "긴장 ⚡",
    mbtiMissing: "MBTI 미입력",
    mbtiHint: "MBTI를 입력하면 더 정확한 분석이 가능해요! 🎯",
    autoDetect: "🔍 자동 찾기",
    deepBond: "깊은 인연 💜",
    soulmate: "소울메이트 🔥",
    destiny: "천생연분 👑✨",
    selectType: "유형 선택",
    enterManually: "데이터를 찾지 못했습니다. 직접 입력해 주세요.",
    analysisError: "분석에 실패했습니다. 입력 데이터를 확인해 주세요.",
    birthDateAlert: "생년월일을 입력해 주세요...",
    required: "필수",
    copied: "클립보드에 복사되었습니다!",
    trendingTitle: "인기 아이돌",
    trendingSubtitle: "스타를 선택하면 바로 궁합을 확인할 수 있어요.",
    tabSaju: "Soul Index: K-사주 명식과 평생의 지표",
    tabFortune: "2026 갓생 캘린더: 월별 도파민 & 운세 흐름",
    tabSignal: "Destiny Signal: {name}님과의 우주 텔레파시 📡",
    introTitle: "운명 찾기",
    introDesc: "자, 이제 K-스타와 당신의 우주적 시그널을 연결할 시간입니다. 당신의 운명적 이상형은 누구일까요? 지금 찾아보세요!",
    birthDatePrompt: "먼저 생년월일을 적어주세요. 꼼꼼히 적을수록 정확해요!",
    mbtiPrompt: "아이돌의 이름이나 MBTI를 모르시나요? 검색 버튼이나 인기 스타를 선택해 보세요!",
    visitorsToday: "오늘의 도전자",
    visitorsTotal: "누적 접속자",
    modeIdol: "스타와 매칭",
    modeFriend: "친구와 매칭",
    friendNameLabel: "친구 이름",
    friendNamePlaceholder: "친구 이름을 입력하세요",
    findFriendMbti: "친구 MBTI 찾기",
    friendGenderLabel: "친구 성별",
    friendBirthLabel: "친구 생일",
    googleAutoFill: "구글 검색 자동 채우기",
    googleAiSearch: "구글 AI 자동 검색",
    searchingWiki: "위키백과에서 후보를 찾는 중...",
    mbtiNotFound: "MBTI 정보를 찾을 수 없습니다",
    mbtiNotFoundDesc: "아이돌의 MBTI를 알면 더 강력하고 섬세한 Destiny Signal(궁합)을 분석할 수 있어요! 어떻게 할까요?",
    inputManually: "직접 입력할래요",
    pureSajuOnly: "없이 순수 사주로만 분석하기",
    close: "닫기",
    sameNameFound: "동명이인이 있습니다. 해당하는 분을 선택해 주세요",
    manualModeTitle: "수동 입력 모드",
    manualModeDesc: "AI가 데이터를 찾지 못했습니다. 직접 입력하거나 구글 검색을 이용해 주세요.",
    analysisSuccess: "데이터 입력이 완료되었습니다. 분석을 시작할 수 있습니다!",
    missionTitle: "🎮 도전! 시너지 레벨 UP 치트키",
    missionDesc: "미션을 완료하면 시너지 레벨이 상승합니다!",
    expand: "▼ 상세보기",
    collapse: "▲ 접기",
    tasksHeader: "✅ 수행과제",
    userSajuResult: "🔮 나의 사주 분석 결과",
    sajuSuccess: "사주 분석 결과가 생성되었습니다.",
    idolTraits: "상대방 성향 🔮",
    attackTips: "공략 꿀팁",
    levelDestiny: "👑 천생연분",
    levelSoulmate: "🔥 소울메이트",
    levelDeepBond: "💜 깊은 인연",
    levelResonance: "💛 공감 단계",
    levelInterest: "💫 관심 단계",
    levelStart: "🌱 운명의 시작",
    feedbackTitle: "💬 소울 리액션 & 익명 게시판",
    feedbackDesc: "오늘의 사주 결과를 익명으로 공유해보세요! 당신의 소울은 지금 어떤가요?",
    placeholderFeedback: "응원 멘트나 소원을 적어보세요...",
    post: "올리기",
    reactions: "리액션",
    communityTitle: "소울 커뮤니티",
    communitySubtitle: "우주에서 전해지는 실시간 리액션",
    addComment: "공개 댓글 추가...",
    cancel: "취소",
    comment: "댓글",
    posting: "게시 중...",
    reply: "답글",
    lifetimeTitle: "🌟 [평생 도약의 운명 경로]",
    lifetimeDesc: "격국(Gyeokguk) 분석을 통한 당신의 소울 설계도와 성공 포인트입니다.",
    mbti_select_title: "MBTI 선택",
    lifetimeStageTitle: "🌟 [평생 도약의 운명 경로]",
    visitor_count: "누적 접속자: {count}",
    expertHealth: "건강 조언",
    expertWealth: "재물 조언",
    expertCareer: "직업 조언",
    expertLove: "애정 조언",
    expertCommentTitle: "전문가 코멘트",
    commentsCount: "댓글 ({count})",
    mbtiNotFoundTitle: "MBTI 정보 누락",
    friendInfoTitle: "친구 / 연인 정보 입력",
    invalidDate: "올바른 날짜 형식이 아닙니다",
    stage: "단계"
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
    dontKnow: "No sabes?",
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
    introDesc: "Ahora es el momento de conectar tus señales cósmicas con las estrellas de K-pop. Quién es tu tipo ideal predestinado? Descúbrelo ahora!",
    birthDatePrompt: "Por favor, ingresa tu fecha de nacimiento primero para obtener resultados precisos!",
    mbtiPrompt: "No sabes el MBTI del ídolo? Usa la búsqueda de IA o elige uno de Popular abajo!",
    visitorsToday: "Retadores de Hoy",
    visitorsTotal: "Visitantes Totales",
    modeIdol: "Encontrar un Ídolo",
    modeFriend: "Coincidir con un Amigo",
    friendNameLabel: "Nombre del Amigo",
    friendNamePlaceholder: "Ingresa el nombre del amigo",
    findFriendMbti: "Encuentra el MBTI del Amigo",
    friendGenderLabel: "Género del Amigo",
    friendBirthLabel: "Fecha de Nacimiento del Amigo",
    googleAutoFill: "Autocompletar con Búsqueda de Google",
    googleAiSearch: "Búsqueda Automática con IA de Google",
    searchingWiki: "Buscando candidatos en Wikipedia...",
    mbtiNotFound: "No se encontró información de MBTI",
    mbtiNotFoundDesc: "Conocer el MBTI del ídolo permite un análisis de la Señal del Destino más potente y delicado! Qué te gustaría hacer?",
    inputManually: "Lo ingresaré yo mismo",
    pureSajuOnly: "Analizar solo con Saju puro",
    close: "Cerrar",
    sameNameFound: "Hay varias personas con el mismo nombre. Por favor, selecciona la correcta.",
    manualModeTitle: "Modo Manual",
    manualModeDesc: "La IA no pudo encontrar datos exactos. Por favor, verifica e ingresa manualmente.",
    analysisSuccess: "Entrada de datos completa. ¡Listo para analizar!",
    missionTitle: "🎮 ¡Desafío! Truco para SUBIR de Nivel",
    missionDesc: "¡Completa misiones para subir tu nivel!",
    expand: "▼ Ver detalles",
    collapse: "▲ Contraer",
    tasksHeader: "✅ Tareas",
    userSajuResult: "🔮 Tu Resultado de Análisis Saju",
    sajuSuccess: "Se ha generado el resultado del análisis Saju.",
    idolTraits: "Personalidad del Ídolo 🔮",
    attackTips: "Tips de Éxito",
    levelDestiny: "👑 Destino",
    levelSoulmate: "🔥 Alma Gemela",
    levelDeepBond: "💜 Vínculo Profundo",
    levelResonance: "💛 Resonancia",
    levelInterest: "💫 Interés",
    levelStart: "🌱 Inicio del Destino",
    feedbackTitle: "💬 Reacciones y Historias del Alma",
    feedbackDesc: "Comparte tus resultados de forma anónima! Cuál es tu vibra hoy?",
    placeholderFeedback: "Escribe un mensaje o un deseo...",
    post: "PUBLICAR",
    reactions: "Reacciones",
    communityTitle: "Comunidad del Alma",
    communitySubtitle: "Reacciones en tiempo real de la galaxia",
    addComment: "Añadir un comentario público...",
    cancel: "Cancelar",
    comment: "Comentar",
    posting: "Publicando...",
    reply: "RESPONDER",
    lifetimeTitle: "🌟 [Camino del Destino de por Vida]",
    lifetimeDesc: "Tu plano de alma y camino al éxito basado en el análisis Gyeokguk.",
    mbti_select_title: "Seleccionar MBTI",
    lifetimeStageTitle: "🌟 [Camino del Destino de por Vida]",
    visitor_count: "Visitantes Totales: {count}",
    expertHealth: "Consejos de Salud",
    expertWealth: "Consejos de Riqueza",
    expertCareer: "Consejos de Carrera",
    expertLove: "Consejos de Amor",
    expertCommentTitle: "Comentarios de Consultores Expertos",
    mbtiNotFoundTitle: "Información de MBTI faltante",
    bias: "Bias",
    visualLine: "Visual Line",
    center: "Center",
    maknae: "Maknae",
    vocalLine: "Vocal Line",
    danceLine: "Dance Line",
    soulBond: "Vínculo de Alma",
    tmi: "TMI del Destino",
    relationship: "Relación K-pop",
    recentFortune: "Suerte de Actividades Recentes",
    friendInfoTitle: "INFORMACIÓN DE AMIGO / PAREJA",
    invalidDate: "Formato de fecha inválido",
    stage: "ETAPA"
  },
  pt: {
    title: "K-DESTINY AI",
    subtitle: "Saju + MBTI Matching para Fãs de K-pop",
    profile: "Seu Perfil",
    birthDate: "Data de Nascimento",
    gender: "Gênero",
    female: "Feminino",
    male: "Masculino",
    nonBinary: "Não binário",
    mbti: "Seu MBTI",
    dontKnow: "Não sabe?",
    searchLabel: "Buscar Ídolo",
    searchDescription: "Digite o nome da sua estrela K-pop favorita. A IA encontrará os detalhes automaticamente.",
    searchPlaceholder: "Digite o nome do ídolo (ex: IU, Jungkook, Stray Kids)...",
    aiMode: "MODO AI",
    searching: "A IA está buscando informações...",
    extracting: "A IA está extraindo dados...",
    checkComp: "Verificar Compatibilidade",
    connectDestiny: "Conecte seu destino com {name} através de algoritmos K-Saju.",
    runAnalysis: "EXECUTAR ANÁLISE",
    destinyEnergy: "Energia do Destino",
    shareResult: "COMPARTILHAR RESULTADO",
    footer: "Criado com 💜 por Abancha · K-Saju AI Engine",
    youLabel: "VOCÊ",
    harmony: "Harmonia ✨",
    resonance: "Ressonância 🔮",
    tension: "Tensão ⚡",
    mbtiMissing: "Sem MBTI",
    mbtiHint: "Adicione MBTI para melhor compatibilidade! 🎯",
    autoDetect: "🔍 Auto-detectar",
    deepBond: "Vínculo Profundo 💜",
    soulmate: "Alma Gêmea 🔥",
    destiny: "Destino 👑✨",
    selectType: "Selecionar Tipo",
    enterManually: "A IA não conseguiu encontrar dados. Insira manualmente.",
    analysisError: "Erro na análise. Verifique seus dados.",
    birthDateAlert: "Por favor, insira sua data de nascimento...",
    required: "OBRIGATÓRIO",
    copied: "Copiado para a área de transferência!",
    trendingTitle: "Ídolos Populares",
    trendingSubtitle: "Selecione uma estrela para verificar seu destino instantaneamente.",
    tabSaju: "Soul Index: K-Saju e o Indicador de Vida",
    tabFortune: "Calendário 2026: Fluxo de Dopamina Mensal",
    tabSignal: "Sinal do Destino: Telepatia Universal com {name}",
    introTitle: "Encontre seu Destino",
    introDesc: "Agora é o momento de conectar seus sinais cósmicos com as estrelas de K-pop. Quem é seu tipo ideal predestinado? Descubra agora!",
    birthDatePrompt: "Por favor, insira sua data de nascimento primeiro para obter resultados precisos!",
    mbtiPrompt: "Não sabe o MBTI do ídolo? Use a busca de IA ou escolha um dos Populares abaixo!",
    visitorsToday: "Desafiadores de Hoje",
    visitorsTotal: "Visitantes Totais",
    modeIdol: "Encontrar um Ídolo",
    modeFriend: "Combinar com um Amigo",
    friendNameLabel: "Nome do Amigo",
    friendNamePlaceholder: "Digite o nome do amigo",
    findFriendMbti: "Encontre o MBTI do Amigo",
    friendGenderLabel: "Gênero do Amigo",
    friendBirthLabel: "Data de Nascimento do Amigo",
    friendInfoTitle: "INFO DE AMIGO / PARCEIRO",
    invalidDate: "Formato de data inválido",
    googleAutoFill: "Auto-preencher com Busca do Google",
    googleAiSearch: "Busca Automática com IA do Google",
    searchingWiki: "Buscando candidatos na Wikipedia...",
    mbtiNotFound: "Informação de MBTI não encontrada",
    mbtiNotFoundDesc: "Conhecer o MBTI do ídolo permite uma análise do Sinal do Destino mais potente e delicada! O que você gostaria de fazer?",
    inputManually: "Eu inserirei manualmente",
    pureSajuOnly: "Analisar apenas com Saju puro",
    close: "Fechar",
    sameNameFound: "Existem várias pessoas com o mesmo nome. Por favor, selecione a correta.",
    manualModeTitle: "Modo Manual",
    manualModeDesc: "A IA não conseguiu encontrar dados exatos. Por favor, verifique e insira manualmente.",
    analysisSuccess: "Entrada de dados completa. Pronto para analisar!",
    missionTitle: "🎮 Desafio! Truque para SUBIR de Nível",
    missionDesc: "Complete missões para subir seu nível!",
    expand: "▼ Ver detalhes",
    collapse: "▲ Recolher",
    tasksHeader: "✅ Tarefas",
    userSajuResult: "🔮 Seu Resultado de Análise Saju",
    sajuSuccess: "O resultado da análise Saju foi gerado.",
    idolTraits: "Personalidade do Ídolo 🔮",
    attackTips: "Dicas de Sucesso",
    levelDestiny: "👑 Destino",
    levelSoulmate: "🔥 Alma Gêmea",
    levelDeepBond: "💜 Vínculo Profundo",
    levelResonance: "💛 Ressonância",
    levelInterest: "💫 Interesse",
    levelStart: "🌱 Início do Destino",
    feedbackTitle: "💬 Reações e Histórias da Alma",
    feedbackDesc: "Compartilhe seus resultados de forma anônima! Qual é a sua vibra hoje?",
    placeholderFeedback: "Escreva uma mensagem ou um desejo...",
    post: "POSTAR",
    reactions: "Reações",
    communityTitle: "Comunidade da Alma",
    communitySubtitle: "Reações em tempo real da galáxia",
    addComment: "Adicionar um comentário público...",
    cancel: "Cancelar",
    comment: "Comentar",
    posting: "Postando...",
    reply: "RESPONDER",
    lifetimeTitle: "🌟 [Caminho do Destino de Toda a Vida]",
    lifetimeDesc: "Seu plano de alma e caminho para o sucesso baseado na análise Gyeokguk.",
    mbti_select_title: "Selecionar MBTI",
    lifetimeStageTitle: "🌟 [Caminho do Destino de Toda a Vida]",
    visitor_count: "Visitantes Totais: {count}",
    expertHealth: "Conselhos de Saúde",
    expertWealth: "Conselhos de Riqueza",
    expertCareer: "Conselhos de Carreira",
    expertLove: "Conselhos de Amor",
    expertCommentTitle: "Comentários dos Consultores Especialistas",
    commentsCount: "Comentários ({count})",
    mbtiNotFoundTitle: "Informação de MBTI ausente",
    bias: "Bias",
    visualLine: "Visual Line",
    center: "Center",
    maknae: "Maknae",
    vocalLine: "Vocal Line",
    danceLine: "Dance Line",
    soulBond: "Vínculo de Alma",
    tmi: "TMI do Destino",
    relationship: "Relação K-pop",
    recentFortune: "Sorte de Atividades Recentes",
    stage: "ETAPA"
  },
};

const getElementTheme = (element: string) => {
  const themes: any = {
    Wood: { bg: '--wood-bg', accent: '--wood-accent', shadow: 'shadow-green-500/20' },
    Fire: { bg: '--fire-bg', accent: '--fire-accent', shadow: 'shadow-red-500/20' },
    Earth: { bg: '--earth-bg', accent: '--earth-accent', shadow: 'shadow-yellow-500/20' },
    Metal: { bg: '--metal-bg', accent: '--metal-accent', shadow: 'shadow-slate-400/20' },
    Water: { bg: '--water-bg', accent: '--water-accent', shadow: 'shadow-sky-500/20' },
  };
  return themes[element] || themes.Metal;
};

const ParticleField = ({ element }: { element: string }) => {
  const particles = useMemo(() => Array.from({ length: 15 }).map((_, i) => ({
    id: i,
    left: `${Math.random() * 100}%`,
    duration: `${Math.random() * 8 + 6}s`,
    delay: `${Math.random() * 5}s`,
    size: `${Math.random() * 6 + 2}px`
  })), [element]);

  const elementMap: any = {
    'Wood': 'wood',
    'Fire': 'fire',
    'Earth': 'earth',
    'Metal': 'metal',
    'Water': 'water'
  };
  const type = elementMap[element] || 'metal';

  return (
    <div className="particle-field">
      {particles.map(p => (
        <div
          key={p.id}
          className={`particle particle-${type}`}
          style={{
            left: p.left,
            width: p.size,
            height: p.size,
            animationDuration: p.duration,
            animationDelay: p.delay
          }}
        />
      ))}
    </div>
  );
};

const CountingScore = ({ targetScore }: { targetScore: number }) => {
  const [displayScore, setDisplayScore] = useState(0);

  useEffect(() => {
    let start = 0;
    const duration = 2000;
    const increment = targetScore / (duration / 16);

    const timer = setInterval(() => {
      start += increment;
      if (start >= targetScore) {
        setDisplayScore(targetScore);
        clearInterval(timer);
      } else {
        setDisplayScore(Math.floor(start));
      }
    }, 16);

    return () => clearInterval(timer);
  }, [targetScore]);

  return <>{displayScore}</>;
};

const SoulCommunity: React.FC<{
  comments: any[];
  onPostComment: (text: string) => void;
  onDeleteComment: (id: string) => void;
  isAdmin: boolean;
  isPosting: boolean;
  commentText: string;
  setCommentText: (text: string) => void;
  t: (key: string, params?: any) => string;
}> = ({ comments, onPostComment, onDeleteComment, isAdmin, isPosting, commentText, setCommentText, t }) => {
  return (
    <div className="mt-12 pt-10 border-t border-slate-800/50">
      <div className="flex items-center justify-between mb-8">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-k-pink/10 rounded-lg">
            <MessageSquare className="h-6 w-6 text-k-pink" />
          </div>
          <div>
            <h3 className="text-xl font-black text-white tracking-tight">{t('communityTitle')}</h3>
            <p className="text-xs text-slate-500 font-medium">{t('communitySubtitle')}</p>
          </div>
        </div>
        <div className="bg-slate-800/80 backdrop-blur-sm border border-slate-700 px-3 py-1 rounded-full">
          <span className="text-xs font-bold text-slate-300">{t('commentsCount', { count: comments.length })}</span>
        </div>
      </div>

      {/* Post Comment Input (YouTube Style) */}
      <div className="flex gap-4 mb-10 group">
        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center text-white font-black text-sm shadow-lg border border-white/10 flex-shrink-0">
          U
        </div>
        <div className="flex-1">
          <input
            type="text"
            value={commentText}
            onChange={(e) => setCommentText(e.target.value)}
            placeholder={t('addComment')}
            className="w-full bg-transparent border-b border-slate-700 focus:border-k-pink outline-none py-1.5 text-slate-200 transition-all placeholder:text-slate-600 focus:placeholder:text-slate-700"
            onKeyDown={(e) => e.key === 'Enter' && onPostComment(commentText)}
          />
          <div className="flex justify-end gap-3 mt-3 opacity-0 group-focus-within:opacity-100 transition-opacity">
            <button
              onClick={() => setCommentText('')}
              className="px-4 py-1.5 text-sm font-bold text-slate-400 hover:text-white transition-colors"
            >
              {t('cancel')}
            </button>
            <button
              disabled={isPosting || !commentText.trim()}
              onClick={() => onPostComment(commentText)}
              className="px-5 py-1.5 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-30 disabled:hover:bg-indigo-600 text-white rounded-full text-sm font-bold transition-all flex items-center gap-2 shadow-md hover:shadow-indigo-500/20"
            >
              {isPosting ? <RefreshCcw className="h-3.5 w-3.5 animate-spin" /> : <Send className="h-3.5 w-3.5" />}
              {isPosting ? t('posting') : t('comment')}
            </button>
          </div>
        </div>
      </div>

      {/* Comment List */}
      <div className="space-y-8">
        <AnimatePresence initial={false}>
          {comments.map((c) => (
            <motion.div
              key={c.id}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              className="flex gap-4"
            >
              <div
                className="w-10 h-10 rounded-full flex items-center justify-center text-white font-black text-sm flex-shrink-0 shadow-inner border border-white/5"
                style={{ backgroundColor: c.avatar_color, boxShadow: `0 4px 12px ${c.avatar_color}33` }}
              >
                {c.author[0].toUpperCase()}
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-[13px] font-bold text-white hover:text-indigo-300 cursor-pointer transition-colors">{c.handle}</span>
                  <span className="text-[11px] text-slate-500 font-medium">{c.timestamp}</span>
                </div>
                <p className="text-sm text-slate-300 leading-relaxed font-medium">{c.content}</p>
                <div className="flex items-center gap-5 mt-3">
                  <div className="flex items-center gap-1">
                    <button className="p-1 hover:bg-slate-800 rounded-full text-slate-500 hover:text-k-pink transition-all">
                      <ThumbsUp className="h-4 w-4" />
                    </button>
                    <span className="text-[11px] text-slate-500 font-bold">{c.likes > 0 ? c.likes : ''}</span>
                  </div>
                  <button className="text-[11px] text-slate-500 hover:bg-slate-800 px-2 py-1 rounded-full transition-all font-bold">{t('reply')}</button>
                  {isAdmin && (
                    <button
                      onClick={() => {
                        if (window.confirm("Delete this comment?")) {
                          onDeleteComment(c.id);
                        }
                      }}
                      className="text-[11px] text-red-500 hover:bg-red-500/10 px-2 py-1 rounded-full transition-all font-bold"
                    >
                      Delete
                    </button>
                  )}
                </div>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>
    </div>
  );
};

const App = () => {
  const [lang, setLanguage] = useState('en');
  const [isAdmin, setIsAdmin] = useState(false);

  React.useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    if (params.get('admin') === 'true') {
      setIsAdmin(true);
    }
  }, []);

  // 국가별 언어 탭 자동 인식
  React.useEffect(() => {
    const browserLang = navigator.language.slice(0, 2);
    if (browserLang === 'ko') setLanguage('ko');
    else if (browserLang === 'es') setLanguage('es');
    else if (browserLang === 'pt') setLanguage('pt');
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
  const [mbtiTarget, setMbtiTarget] = useState<'user' | 'idol'>('user');

  const [analysisResult, setAnalysisResult] = useState<any>(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [showMissingMbtiModal, setShowMissingMbtiModal] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [showErrorShake, setShowErrorShake] = useState(false);
  const [popularIdols, setPopularIdols] = useState<{ male: any[], female: any[] }>({ male: [], female: [] });
  const [activeTab, setActiveTab] = useState<'saju' | 'fortune' | 'signal'>('saju');
  const [commentText, setCommentText] = useState('');
  const [isPostingComment, setIsPostingComment] = useState(false);
  const [comments, setComments] = useState<any[]>([]);
  const [mode, setMode] = useState<'idol' | 'friend'>('idol');
  const [friendData, setFriendData] = useState({ name: '', birth_date: '', gender: 'female', mbti: '' });
  const [stats, setStats] = useState({ today_challengers: 0, total_visitors: 0 });

  // Browser Unique ID Generator (Fingerprint)
  const getVisitorId = () => {
    let vid = localStorage.getItem('k_destiny_vid');
    if (!vid) {
      vid = 'v_' + Math.random().toString(36).substring(2, 15) + Date.now().toString(36);
      localStorage.setItem('k_destiny_vid', vid);
    }
    return vid;
  };

  const fetchStats = async () => {
    try {
      const res = await axios.get(`${API_URL.replace('/api', '')}/api/stats`);
      if (res.data.status === 'success') {
        setStats(res.data.data);
      }
    } catch (e) {
      console.error("Fetch stats error:", e);
    }
  };

  const recordVisit = async () => {
    try {
      const vid = getVisitorId();
      await axios.post(`${API_URL.replace('/api', '')}/api/stats/visit?visitor_id=${vid}`);
    } catch (e) { console.error("Record visit error", e); }
  };

  const recordChallenge = async () => {
    try {
      await axios.post(`${API_URL.replace('/api', '')}/api/stats/challenge`);
    } catch (e) { console.error("Record challenge error", e); }
  };

  const fetchComments = async () => {
    try {
      const res = await axios.get(`${API_URL.replace('/api', '')}/api/comments`);
      if (res.data.status === 'success') {
        setComments(res.data.comments);
      }
    } catch (e) {
      console.error("Fetch comments error:", e);
    }
  };

  const handlePostComment = async () => {
    if (!commentText.trim()) return;
    setIsPostingComment(true);
    try {
      const res = await axios.post(`${API_URL.replace('/api', '')}/api/comments`, {
        author: 'User',
        content: commentText
      });
      if (res.data.status === 'success') {
        setComments(prev => [res.data.comment, ...prev]);
        setCommentText('');
      }
    } catch (e) {
      console.error("Post comment error:", e);
    } finally {
      setIsPostingComment(false);
    }
  };

  const handleDeleteComment = async (commentId: string) => {
    try {
      await axios.delete(`${API_URL.replace('/api', '')}/api/comments/${commentId}`);
      setComments(prev => prev.filter(c => c.id !== commentId));
    } catch (e) {
      console.error("Delete comment error:", e);
    }
  };

  React.useEffect(() => {
    if (analysisResult && activeTab === 'signal') {
      fetchComments();
    }
  }, [analysisResult, activeTab]);

  React.useEffect(() => {
    fetchStats();
    recordVisit();
  }, []);
  // 후보 선택 UI
  const [candidates, setCandidates] = useState<any[]>([]);
  const [showCandidates, setShowCandidates] = useState(false);
  const [candidatesLoading, setCandidatesLoading] = useState(false);

  // 구글 보조 검색 UI
  const [assistantLoading, setAssistantLoading] = useState(false);
  const [completedMissions, setCompletedMissions] = useState<string[]>([]);
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

  const resetAppState = () => {
    setIdolData(null);
    setAnalysisResult(null);
    setCompletedMissions([]);
    setErrorMessage(null);
    setCandidates([]);
    setShowCandidates(false);
    setIsManualMode(false);
  };

  const handleIdolClick = async (name: string) => {
    resetAppState();
    // 인기 아이돌 목록에 현재 클릭한 아이돌이 있고 데이터가 이미 있으면 바로 로드 (검색 단계 생략)
    // popularIdols의 객체 구조는 {name_en, name_kr, ...} 이므로 둘 다 체크
    const found = [...popularIdols.male, ...popularIdols.female].find(p => p.name_en === name || p.name_kr === name);

    if (found && found.birth_date) {
      setIdolSearchName(lang === 'ko' ? found.name_kr : found.name_en);
      setIdolData({
        ...found,
        name: lang === 'ko' ? found.name_kr : found.name_en
      });
      return;
    }

    setIdolSearchName(name);
    // 데이터가 없거나 부족한 경우에만 검색 실행
    await executeSearch(name);
  };

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!idolSearchName) return;
    await executeSearch(idolSearchName);
  };

  const executeSearch = async (searchName: string) => {
    resetAppState();
    setLoading(true);

    try {
      // 1단계: 후보 목록 먼저 조회
      setCandidatesLoading(true);
      const candRes = await axios.get(`${API_URL}/idol/candidates`, {
        params: { name: searchName }, timeout: 30000
      });
      setCandidatesLoading(false);

      // 후보 목록 처리
      const allCands = candRes.data.candidates || [];
      // 백엔드에서 이미 is_person 여부를 판단해서 보내주므로 이를 활용
      const personCands = allCands.filter((c: any) => c.is_person !== false);

      // 후보가 1개보다 많으면 → 선택 UI 표시
      if (personCands.length >= 1) {
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
      setErrorMessage(null); // 에러 대신 수동 모드 안내 유도
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
      setErrorMessage(null);
    } finally {
      setLoading(false);
    }
  };

  const runFullAnalysis = async (skipMbtiCheck = false, keepTab = false) => {
    if (!userBirthDate || !isValidDate(userBirthDate)) {
      setErrorMessage(t('birthDateAlert'));
      setShowErrorShake(true);
      setTimeout(() => setShowErrorShake(false), 600);
      document.getElementById('user-profile-section')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      return;
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
      const p_name = mode === 'friend' ? t('friendMatchingTitle') : (idolData?.name || idolSearchName);
      const p_mbti = mode === 'friend' ? friendData.mbti : (idolData?.mbti || '');
      const p_birth = mode === 'friend' ? friendData.birth_date : (idolData?.birth_date || '');

      const response = await axios.get(`${API_URL}/saju/analyze`, {
        params: {
          birth_date: userBirthDate,
          gender: userGender,
          user_mbti: userMBTI,
          idol_name: p_name,
          idol_mbti: p_mbti,
          idol_birth_date: p_birth,
          lang: lang // 현재 선택된 프론트엔드 언어 코드 전송
        },
        timeout: 60000
      });
      setAnalysisResult(response.data.analysis);
      if (!keepTab) setActiveTab('saju'); // 결과가 새로 나올 때만 첫 탭으로 초기화
    } catch (error) {
      console.error('Analysis Error:', error);
      setErrorMessage(t('analysisError'));
    } finally {
      setAnalyzing(false);
      recordChallenge();
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

        // 검색했는데도 데이터가 부족하면 수동 입력 모드로 자동 전환 및 포커스
        if (!info.birth_date && (!newMbti || newMbti === 'Unknown')) {
          setIsManualMode(true);
          setErrorMessage(null);
          setTimeout(() => mbtiInputRef.current?.focus(), 100);
        } else {
          // 데이터가 충분히 수집되었으면 시각적 피드백 제공 후 자동 스크롤
          setIsManualMode(false);
          document.getElementById('idol-data-ready')?.scrollIntoView({ behavior: 'smooth' });
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
      text: `I matched with ${idolData.name} !My K - Energy is ${analysisResult?.label}. Check yours on K - Destiny!`,
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
      // Re-run the analysis to fetch translation using the newly selected language without resetting tab
      runFullAnalysis(false, true);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [lang]);

  return (
    <div className="container mx-auto px-4 py-10 max-w-4xl min-h-screen relative z-10">
      {/* Language Switcher */}
      <div className="flex justify-end gap-2 mb-4">
        {['es', 'pt', 'en', 'ko'].map((l) => (
          <button
            key={l}
            onClick={() => setLanguage(l)}
            className={`px - 3 py - 1 rounded - full text - xs font - bold transition - all ${lang === l ? 'bg-k-purple text-white shadow-lg' : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
              } `}
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
        <div className="mt-8 flex items-center justify-center gap-2 text-slate-500 text-xs font-bold">
          <Users className="h-3 w-3" />
          {t('visitor_count', { count: stats.total_visitors.toLocaleString() })}
        </div>
      </header>

      {/* User Info Section */}
      <section id="user-profile-section" className="bg-slate-800/30 border border-slate-700/50 rounded-3xl p-6 mb-8 backdrop-blur-sm shadow-xl">
        <h2 className="text-sm font-bold text-slate-500 uppercase tracking-widest mb-4 flex items-center gap-2">
          <User className="h-4 w-4" /> {t('profile')}
        </h2>
        <div className="grid md:grid-cols-3 gap-4 mb-6">
          {/* Birth Date Box */}
          <div className="flex flex-col h-[102px]">
            <label className="text-xs font-bold text-slate-400 ml-1 mb-2">{t('birthDate')}</label>
            <div className="relative flex-1">
              <motion.input
                animate={showErrorShake && !userBirthDate ? { x: [-10, 10, -10, 10, 0] } : {}}
                transition={{ duration: 0.4 }}
                id="user-birth-date-input"
                aria-label="User Birth Date YYYY-MM-DD"
                placeholder="YYYY-MM-DD"
                value={userBirthDate}
                onChange={(e) => {
                  const raw = e.target.value.replace(/\D/g, '').slice(0, 8);
                  let formatted = raw;
                  if (raw.length > 4) formatted = `${raw.slice(0, 4)}-${raw.slice(4)}`;
                  if (raw.length > 6) formatted = `${formatted.slice(0, 7)}-${raw.slice(6)}`;
                  setUserBirthDate(formatted);
                }}
                className={`w-full bg-slate-900/80 border-2 rounded-2xl px-4 py-3 outline-none transition-all text-white placeholder:text-slate-600 ${userBirthDate.length === 10 && !isValidDate(userBirthDate)
                  ? 'border-red-500 ring-2 ring-red-500/20'
                  : 'border-slate-700/50 focus:border-k-blue focus:bg-slate-900 group-hover:border-slate-600'
                  }`}
              />
              {userBirthDate.length === 10 && !isValidDate(userBirthDate) ? (
                <p className="absolute -bottom-5 left-1 text-red-400 text-[10px] font-bold animate-pulse">Invalid Date</p>
              ) : (
                <p className="absolute -bottom-5 left-1 text-[10px] text-slate-500 flex items-center gap-1 opacity-80 whitespace-nowrap overflow-hidden text-ellipsis max-w-full">
                  <Sparkles className="h-2.5 w-2.5 text-yellow-500" /> {t('birthDatePrompt')}
                </p>
              )}
            </div>
          </div>


          {/* Gender Box */}
          <div className="flex flex-col h-[102px]">
            <label className="text-xs font-bold text-slate-400 ml-1 mb-2">{t('gender')}</label>
            <div className="relative flex-1">
              <select
                id="user-gender-select"
                aria-label="User Gender Selection"
                value={userGender}
                onChange={(e) => setUserGender(e.target.value)}
                className="w-full h-[52px] bg-slate-900/80 border-2 border-slate-700/50 rounded-2xl px-4 py-3 focus:border-k-pink focus:bg-slate-900 outline-none transition-all appearance-none cursor-pointer text-white"
              >
                <option value="female">{t('female')}</option>
                <option value="male">{t('male')}</option>
                <option value="non-binary">{t('nonBinary')}</option>
              </select>
              <div className="absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-slate-500">
                <ChevronDown className="h-4 w-4" />
              </div>
            </div>
          </div>

          {/* MBTI Box */}
          <div className="flex flex-col h-[102px]">
            <div className="flex justify-between items-center mb-2 px-1">
              <label className="text-xs font-bold text-slate-400">{t('mbti')}</label>
              <motion.button
                whileHover={{ x: 2 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => setShowMBTIQuiz(true)}
                className="text-k-purple hover:text-k-pink transition-colors flex items-center gap-1 font-black text-[10px] uppercase tracking-tighter"
              >
                <HelpCircle className="h-3 w-3" /> {t('dontKnow')}
              </motion.button>
            </div>
            <div className="relative flex-1">
              <select
                value={userMBTI}
                onChange={(e) => setUserMBTI(e.target.value)}
                className="w-full h-[52px] bg-slate-900/80 border-2 border-slate-700/50 rounded-2xl px-4 py-3 focus:border-k-purple focus:bg-slate-900 outline-none transition-all appearance-none cursor-pointer text-white"
              >
                <option value="">{t('selectType')}</option>
                {["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"].map(t_mbti => (
                  <option key={t_mbti} value={t_mbti}>{t_mbti}</option>
                ))}
              </select>
              <div className="absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-slate-500">
                <ChevronDown className="h-4 w-4" />
              </div>
            </div>
          </div>
        </div>

        <div className="mt-4 pt-6 border-t border-slate-700/30 flex flex-col items-center">
          <label className="text-xs font-bold text-slate-500 uppercase tracking-widest mb-3">{t('selectType')}</label>
          <div className="inline-flex p-1 bg-slate-900/80 rounded-2xl border-2 border-slate-700/50 shadow-2xl w-full max-w-md">
            <button
              onClick={() => {
                setMode('idol');
                setAnalysisResult(null);
                setCompletedMissions([]);
              }}
              className={`flex-1 px-6 py-3 rounded-xl text-sm font-black transition-all flex items-center justify-center gap-2 ${mode === 'idol' ? 'bg-gradient-to-r from-k-purple to-k-blue text-white shadow-lg shadow-k-purple/20' : 'text-slate-500 hover:text-slate-300'}`}
            >
              <Sparkles className="h-4 w-4" /> {t('modeIdol')}
            </button>
            <button
              onClick={() => {
                setMode('friend');
                setIdolData(null);
                setAnalysisResult(null);
                setCompletedMissions([]);
              }}
              className={`flex-1 px-6 py-3 rounded-xl text-sm font-black transition-all flex items-center justify-center gap-2 ${mode === 'friend' ? 'bg-gradient-to-r from-k-blue to-cyan-500 text-white shadow-lg shadow-k-blue/20' : 'text-slate-500 hover:text-slate-300'}`}
            >
              <Users className="h-4 w-4" /> {t('modeFriend')}
            </button>
          </div>
        </div>
      </section>

      {/* Friend Input Section - Shown below user profile in friend mode */}
      <AnimatePresence>
        {mode === 'friend' && (
          <motion.section
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            className="bg-slate-800/30 border border-slate-700/50 rounded-3xl p-6 mb-8 backdrop-blur-sm shadow-xl"
          >
            <h2 className="text-sm font-bold text-k-blue uppercase tracking-widest mb-4 flex items-center gap-2">
              <Users className="h-4 w-4" /> {t('friendInfoTitle')}
            </h2>
            <div className="grid md:grid-cols-3 gap-4">
              <div className="flex flex-col h-[102px]">
                <label className="text-xs font-bold text-slate-400 ml-1 mb-2">{t('friendBirthLabel')}</label>
                <input
                  type="text"
                  value={friendData.birth_date}
                  onChange={(e) => {
                    const raw = e.target.value.replace(/\D/g, '').slice(0, 8);
                    let formatted = raw;
                    if (raw.length > 4) formatted = `${raw.slice(0, 4)}-${raw.slice(4)}`;
                    if (raw.length > 6) formatted = `${formatted.slice(0, 7)}-${raw.slice(6)}`;
                    setFriendData({ ...friendData, birth_date: formatted });
                  }}
                  placeholder="YYYY-MM-DD"
                  className={`w-full bg-slate-900/80 border-2 rounded-2xl px-4 py-3 outline-none transition-all text-white placeholder:text-slate-600 ${friendData.birth_date.length === 10 && !isValidDate(friendData.birth_date) ? 'border-red-500' : 'border-slate-700/50 focus:border-k-blue'}`}
                />
                {friendData.birth_date.length === 10 && !isValidDate(friendData.birth_date) && (
                  <p className="text-red-400 text-[10px] font-bold mt-1 ml-1">{t('invalidDate')}</p>
                )}
              </div>
              <div className="flex flex-col h-[102px]">
                <label className="text-xs font-bold text-slate-400 ml-1 mb-2">{t('friendGenderLabel')}</label>
                <select
                  value={friendData.gender}
                  onChange={(e) => setFriendData({ ...friendData, gender: e.target.value })}
                  className="w-full h-[52px] bg-slate-900/80 border-2 border-slate-700/50 rounded-2xl px-4 py-3 focus:border-k-pink outline-none appearance-none cursor-pointer text-white"
                >
                  <option value="female">{t('female')}</option>
                  <option value="male">{t('male')}</option>
                </select>
              </div>
              <div className="flex flex-col h-[102px]">
                <label className="text-xs font-bold text-slate-400 ml-1 mb-2">{t('mbti')}</label>
                <select
                  value={friendData.mbti}
                  onChange={(e) => setFriendData({ ...friendData, mbti: e.target.value })}
                  className="w-full h-[52px] bg-slate-900/80 border-2 border-slate-700/50 rounded-2xl px-4 py-3 focus:border-k-purple outline-none appearance-none cursor-pointer text-white"
                >
                  <option value="">{t('selectType')}</option>
                  {["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"].map(m => (
                    <option key={m} value={m}>{m}</option>
                  ))}
                </select>
              </div>
            </div>

            {/* 분석 버튼 (친구용) */}
            {!analysisResult && (
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                onClick={() => runFullAnalysis(true)}
                disabled={analyzing}
                className="w-full mt-6 py-4 bg-gradient-to-r from-k-blue to-cyan-500 rounded-2xl font-black text-lg shadow-xl shadow-k-blue/20 flex items-center justify-center gap-3 active:scale-95 text-white"
              >
                {analyzing ? <RefreshCcw className="h-5 w-5 animate-spin" /> : t('runAnalysis')}
              </motion.button>
            )}
          </motion.section>
        )}
      </AnimatePresence>

      {/* Search Bar & Idol UI - Only visible in IDOL mode */}
      <AnimatePresence>
        {mode === 'idol' && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            className="max-w-2xl mx-auto mb-16"
          >
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
                  {t('searchingWiki')}
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
                    {t('sameNameFound')}
                  </p>
                  <button
                    onClick={() => { setShowCandidates(false); setCandidates([]); }}
                    className="text-slate-500 hover:text-white text-xs px-2 py-1 rounded-lg hover:bg-slate-700 transition-all"
                  >
                    {t('close')}
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
                      </div >
                      {/* 이름 + 설명 */}
                      < div className="flex-1 min-w-0" >
                        <p className="font-bold text-white text-sm truncate">{c.title}</p>
                        {
                          c.description && (
                            <p className="text-xs text-slate-400 mt-0.5 truncate">{c.description}</p>
                          )
                        }
                        {
                          c.extract && (
                            <p className="text-xs text-slate-500 mt-1 line-clamp-2 leading-relaxed">{c.extract}</p>
                          )
                        }
                      </div >
                      <div className="text-k-purple text-lg flex-shrink-0">›</div>
                    </motion.button >
                  ))}
                </div >
              </motion.div >
            )}

            {/* Popular Idols Section (Horizontal Swipe Restored) */}
            <div className="mt-8 px-2 overflow-hidden">
              <div className="space-y-8">
                {/* Male Idols (Boys) */}
                <div>
                  <h3 className="text-sm font-bold text-k-blue uppercase tracking-widest mb-4 flex items-center gap-2 px-2">
                    <Star className="h-3 w-3 text-k-blue" /> {lang === 'ko' ? '인기 남성 그룹' : 'Trending Boys'}
                  </h3>
                  {(!popularIdols || !popularIdols.male || popularIdols.male.length === 0) ? (
                    <div className="py-4 text-center bg-slate-800/30 rounded-2xl border border-slate-700/30 mx-2">
                      <p className="text-slate-500 text-[10px]">데이터 로드 중...</p>
                    </div>
                  ) : (
                    <motion.div
                      className="flex gap-4 overflow-x-auto pb-6 px-2 scrollbar-hide no-scrollbar"
                      style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
                    >
                      {popularIdols.male.map((idol: any, idx: number) => (
                        <motion.button
                          key={idol.id}
                          initial={{ opacity: 0, x: 20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: idx * 0.05 }}
                          whileHover={{ y: -5, scale: 1.05 }}
                          whileTap={{ scale: 0.95 }}
                          onClick={() => handleIdolClick(idol.name_en)}
                          className="flex-shrink-0 w-32 bg-slate-800/50 border border-slate-700/50 rounded-2xl p-3 hover:bg-slate-700/50 hover:border-k-blue/50 transition-all text-center group shadow-lg shadow-k-blue/5"
                        >
                          <div className="w-full aspect-square bg-slate-900 rounded-xl mb-3 flex items-center justify-center overflow-hidden border border-slate-700 group-hover:border-k-blue/30">
                            <img
                              src={`/avatars/male_${(idx % 8) + 1}.png`}
                              alt={idol.name_en}
                              className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity"
                              onError={(e: any) => { e.target.src = `/avatars/male_1.png`; }}
                            />
                          </div>
                          <p className="text-xs font-black text-white truncate mb-0.5">{lang === 'ko' ? idol.name_kr : idol.name_en}</p>
                          <p className="text-[10px] text-slate-500 font-bold uppercase tracking-tight truncate">{idol.group}</p>
                        </motion.button>
                      ))}
                    </motion.div>
                  )}
                </div>

                {/* Female Idols (Girls) */}
                <div>
                  <h3 className="text-sm font-bold text-k-pink uppercase tracking-widest mb-4 flex items-center gap-2 px-2">
                    <Heart className="h-3 w-3 text-k-pink" /> {lang === 'ko' ? '인기 여성 그룹' : 'Trending Girls'}
                  </h3>
                  {(!popularIdols || !popularIdols.female || popularIdols.female.length === 0) ? (
                    <div className="py-4 text-center bg-slate-800/30 rounded-2xl border border-slate-700/30 mx-2">
                      <p className="text-slate-500 text-[10px]">데이터 로드 중...</p>
                    </div>
                  ) : (
                    <motion.div
                      className="flex gap-4 overflow-x-auto pb-6 px-2 scrollbar-hide no-scrollbar"
                      style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
                    >
                      {popularIdols.female.map((idol: any, idx: number) => (
                        <motion.button
                          key={idol.id}
                          initial={{ opacity: 0, x: 20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: 0.2 + idx * 0.05 }}
                          whileHover={{ y: -5, scale: 1.05 }}
                          whileTap={{ scale: 0.95 }}
                          onClick={() => handleIdolClick(idol.name_en)}
                          className="flex-shrink-0 w-32 bg-slate-800/50 border border-slate-700/50 rounded-2xl p-3 hover:bg-slate-700/50 hover:border-k-pink/50 transition-all text-center group shadow-lg shadow-k-pink/5"
                        >
                          <div className="w-full aspect-square bg-slate-900 rounded-xl mb-3 flex items-center justify-center overflow-hidden border border-slate-700 group-hover:border-k-pink/30">
                            <img
                              src={`/avatars/female_${(idx % 8) + 1}.png`}
                              alt={idol.name_en}
                              className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity"
                              onError={(e: any) => { e.target.src = `/avatars/female_1.png`; }}
                            />
                          </div>
                          <p className="text-xs font-black text-white truncate mb-0.5">{lang === 'ko' ? idol.name_kr : idol.name_en}</p>
                          <p className="text-[10px] text-slate-500 font-bold uppercase tracking-tight truncate">{idol.group}</p>
                        </motion.button>
                      ))}
                    </motion.div>
                  )}
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Status Messages (Purified for UAT) */}
      <AnimatePresence>
        {
          errorMessage && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              className="max-w-2xl mx-auto mb-6 px-6 py-4 rounded-2xl flex items-center gap-4 border shadow-lg bg-red-500/10 border-red-500/30 text-red-200"
            >
              <HelpCircle className="h-6 w-6 flex-shrink-0" />
              <div>
                <p className="text-sm font-black uppercase tracking-widest mb-0.5">ERROR</p>
                <p className="text-sm opacity-90">{errorMessage}</p>
              </div>
            </motion.div>
          )
        }
      </AnimatePresence >

      {/* Missing MBTI Modal */}
      <AnimatePresence>
        {
          showMissingMbtiModal && (
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

                <h3 className="text-xl font-black text-center mb-2">{t('mbtiNotFound')}</h3>
                <p className="text-slate-400 text-sm text-center mb-8 leading-relaxed">
                  {t('mbtiNotFoundDesc')}
                </p>

                <div className="space-y-3">
                  <button
                    onClick={() => {
                      setShowMissingMbtiModal(false);
                      setMbtiTarget('idol');
                      setShowMBTIQuiz(true);
                    }}
                    className="w-full flex items-center justify-center gap-2 py-3 px-4 bg-k-purple text-white font-black rounded-xl shadow-lg transition-all"
                  >
                    <LayoutGrid className="h-4 w-4" />
                    {t('mbti_select_title')}
                  </button>

                  <button
                    onClick={() => {
                      setShowMissingMbtiModal(false);
                      runFullAnalysis(true);
                    }}
                    className="w-full flex items-center justify-center gap-2 py-4 px-4 bg-slate-700/50 hover:bg-k-purple text-white font-black rounded-xl transition-all shadow-lg"
                  >
                    <Sparkles className="h-4 w-4" />
                    {t('pureSajuOnly')}
                  </button>
                </div>
              </motion.div>
            </motion.div>
          )
        }
      </AnimatePresence >

      {/* QuickMBTI Quiz */}
      <AnimatePresence>
        {
          showMBTIQuiz && (
            <QuickMBTI
              onClose={() => setShowMBTIQuiz(false)}
              onComplete={(mbti: string) => {
                if (mbtiTarget === 'user') {
                  setUserMBTI(mbti);
                } else if (mbtiTarget === 'idol') {
                  setIdolData((prev: any) => ({ ...prev, mbti: mbti }));
                }
                setShowMBTIQuiz(false);
              }}
            />
          )
        }
      </AnimatePresence >

      {/* Results Display */}
      <AnimatePresence>
        {
          loading && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-center py-20">
              <div className="animate-spin h-12 w-12 border-4 border-k-purple border-t-transparent rounded-full mx-auto mb-4"></div>
              <p className="text-xl font-medium text-slate-300 italic">{t('searching')}</p>
            </motion.div>
          )
        }

        {((idolData && !loading) || (mode === 'friend' && analysisResult)) && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="bg-slate-800 rounded-[2rem] p-4 sm:p-10 border border-slate-700 shadow-2xl overflow-hidden relative"
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
            <div className="flex flex-col md:flex-row items-center gap-4 bg-slate-900/80 rounded-2xl p-4 mb-6 border border-slate-700/50 relative z-10">
              <div className="flex items-center gap-4 flex-1 min-w-0">
                <div className="p-2 bg-k-pink/10 rounded-xl relative w-14 h-14 shrink-0 flex items-center justify-center">
                  <img
                    src={`/avatars/${(mode === 'friend' ? friendData.gender : (idolData?.gender || 'female')) === 'male' ? 'male' : 'female'}_1.png`}
                    alt={mode === 'friend' ? 'Friend' : (idolData?.name || 'Idol')}
                    className="w-full h-full object-cover opacity-90"
                    onError={(e: any) => {
                      e.target.src = `/avatars/female_1.png`;
                    }}
                  />
                </div>
                <div className="min-w-0 flex flex-col">
                  {mode === 'friend' ? (
                    <h3 className="text-xl font-black uppercase tracking-tighter text-k-blue leading-none mb-1">{t('friendMatchingTitle')}</h3>
                  ) : isManualMode ? (
                    <input
                      value={idolData?.name || ''}
                      onChange={(e) => setIdolData({ ...idolData, name: e.target.value })}
                      className="bg-transparent border-b-2 border-k-pink text-xl font-black uppercase tracking-tighter outline-none w-full mb-1"
                    />
                  ) : (
                    <h3 className="text-xl font-black uppercase tracking-tighter text-k-pink leading-none mb-1">{idolData.name}</h3>
                  )}
                  {/* 스타 생일 & MBTI 표시 (복구) */}
                  <div className="flex items-center gap-2 text-[10px] font-bold text-slate-400">
                    <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700">🎂 {mode === 'friend' ? friendData.birth_date : (idolData.birth_date || '????-??-??')}</span>
                    <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700 uppercase">⚡ {mode === 'friend' ? friendData.mbti : (idolData.mbti || 'Unknown')}</span>
                  </div>
                </div>
              </div>
              {/* 수동 편집을 위한 추가 필드들 (수동 모드일 때만 표시) */}
              {isManualMode && (
                <div className="flex flex-wrap items-center gap-x-4 gap-y-2 flex-shrink-0 bg-slate-800/50 p-3 rounded-xl border border-slate-700/50">
                  <div className="flex items-center gap-2">
                    <Calendar className="h-4 w-4 text-k-blue" />
                    <input type="text" placeholder="YYYY-MM-DD" maxLength={10} value={idolData.birth_date}
                      onChange={(e) => {
                        const raw = e.target.value.replace(/\D/g, '').slice(0, 8);
                        let formatted = raw;
                        if (raw.length > 4) formatted = `${raw.slice(0, 4)}-${raw.slice(4)}`;
                        if (raw.length > 6) formatted = `${formatted.slice(0, 7)}-${raw.slice(6)}`;
                        setIdolData({ ...idolData, birth_date: formatted });
                      }}
                      className="bg-transparent text-sm font-bold outline-none w-28 border-b border-slate-700 focus:border-k-blue text-white"
                    />
                  </div>
                  <div className="flex items-center gap-2">
                    <BrainCircuit className="h-4 w-4 text-k-purple cursor-pointer hover:text-k-pink transition-colors" onClick={() => { setMbtiTarget('idol'); setShowMBTIQuiz(true); }} />
                    <input
                      ref={mbtiInputRef}
                      type="text"
                      placeholder="MBTI"
                      value={idolData.mbti}
                      onChange={(e) => {
                        const val = e.target.value.toUpperCase().slice(0, 4);
                        setIdolData({ ...idolData, mbti: val });
                      }}
                      className="bg-transparent text-sm font-bold outline-none w-16 border-b border-slate-700 focus:border-k-purple text-white"
                    />
                  </div>
                  {(!idolData.mbti || idolData.mbti === 'Unknown') && (
                    <div className="flex items-center gap-2">
                      <span className="text-xs font-bold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded-full border border-amber-500/30 animate-pulse">⚠️ {t('mbtiMissing')}</span>
                      <button onClick={handleAssistantSearch} disabled={assistantLoading}
                        className="px-3 py-1.5 bg-blue-600/40 hover:bg-blue-600/60 rounded-lg text-sm font-bold text-blue-200 border border-blue-400/50 flex items-center gap-1.5 transition-all animate-pulse ring-1 ring-blue-400/30 shadow-[0_0_10px_rgba(59,130,246,0.3)]"
                      >
                        {assistantLoading ? <RefreshCcw className="h-4 w-4 animate-spin" /> : <Search className="h-4 w-4" />}
                        {t('autoDetect')}
                      </button>
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* ===== 분석 결과 영역 (전체 폭) ===== */}
            <div className="relative z-10">
              <div className="relative group">
                <motion.div
                  layout
                  className="absolute inset-0 bg-gradient-to-br from-k-purple/30 to-k-blue/30 rounded-[2.5rem] blur-2xl group-hover:blur-3xl transition-all"
                ></motion.div>
                <motion.div
                  layout
                  className={`relative bg-slate-900 rounded-[2rem] flex flex-col border-2 border-slate-700 p-4 sm:p-8 shadow-inner w-full ${!analysisResult ? 'aspect-square items-center justify-center text-center' : 'min-h-[400px]'}`}
                >
                  {/* Results Display Area - Enhanced with Bento Grid for UAT */}
                  {!analysisResult ? (
                    <div className="w-full flex flex-col items-center">
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full mb-8">
                        {/* Card 1: Star TMI */}
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          className="bg-slate-800/40 p-5 rounded-3xl border border-slate-700/50 flex flex-col gap-3 hover:border-k-pink/30 transition-all group"
                        >
                          <div className="flex items-center gap-2">
                            <Sparkles className="h-4 w-4 text-k-pink" />
                            <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Star TMI</span>
                          </div>
                          <p className="text-sm font-bold text-white leading-relaxed">
                            {idolData?.tmi || "이 스타의 에너지는 당신의 하루를 더 밝게 빛내줄 거예요! ✨"}
                          </p>
                        </motion.div>

                        {/* Card 2: Destiny Preview */}
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: 0.1 }}
                          className="bg-slate-800/40 p-5 rounded-3xl border border-slate-700/50 flex flex-col gap-3 hover:border-k-blue/30 transition-all"
                        >
                          <div className="flex items-center gap-2">
                            <BrainCircuit className="h-4 w-4 text-k-blue" />
                            <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Destiny Preview</span>
                          </div>
                          <div className="flex items-center gap-3">
                            <div className="text-2xl">🔮</div>
                            <p className="text-xs text-slate-300 font-medium">
                              {t('connectDestiny', { name: idolData.name })}
                            </p>
                          </div>
                        </motion.div>

                        {/* Card 3: Real-time Signal (Wide) */}
                        <motion.div
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: 0.2 }}
                          className="md:col-span-2 bg-gradient-to-r from-k-purple/10 to-k-blue/10 p-5 rounded-3xl border border-k-purple/20 flex items-center justify-between group"
                        >
                          <div className="flex items-center gap-4">
                            <div className="w-10 h-10 rounded-full bg-slate-900 border border-k-purple/30 flex items-center justify-center text-lg animate-pulse">📡</div>
                            <div>
                              <p className="text-[10px] font-black text-k-purple uppercase tracking-widest mb-1">Live Signal</p>
                              <p className="text-xs font-bold text-white">현재 {stats.today_challengers.toLocaleString()}명이 이 스타와 교신 중...</p>
                            </div>
                          </div>
                          <TrendingUp className="h-5 w-5 text-k-blue opacity-50 group-hover:opacity-100 transition-opacity" />
                        </motion.div>
                      </div>

                      <h3 className="text-xl font-bold mb-6 text-slate-400 italic">{t('checkComp')}</h3>

                      {errorMessage && (
                        <div className="w-full mb-6 px-4 py-3 bg-red-500/10 border border-red-500/30 rounded-xl text-red-300 text-sm font-bold flex items-center gap-2 animate-pulse">
                          <HelpCircle className="h-4 w-1 flex-shrink-0" />
                          {errorMessage}
                        </div>
                      )}

                      <motion.button
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => runFullAnalysis(false)}
                        disabled={analyzing}
                        className="w-full py-5 bg-gradient-to-r from-k-purple to-k-blue rounded-2xl font-black text-xl shadow-[0_0_20px_rgba(139,92,246,0.3)] flex items-center justify-center gap-3 active:scale-95"
                      >
                        {analyzing ? <RefreshCcw className="h-6 w-6 animate-spin" /> : (
                          <>
                            <Sparkles className="h-6 w-6" />
                            {t('runAnalysis')}
                          </>
                        )}
                      </motion.button>
                    </div>
                  ) : (

                    <motion.div
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 0.8, ease: "easeOut" }}
                      className="w-full text-left mt-4"
                    >

                      {/* Category Selection */}
                      <div className="grid grid-cols-1 gap-3 mb-6">
                        <button
                          onClick={() => setActiveTab('saju')}
                          className={`flex items-center justify-between px-5 py-3 sm:py-4 rounded-2xl border-2 transition-all ${activeTab === 'saju' ? 'bg-k-pink/10 border-k-pink text-k-pink shadow-[0_0_15px_rgba(236,72,153,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-k-pink/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base break-keep">{t('tabSaju')}</span>
                          <span className="text-lg sm:text-xl opacity-80">🔮</span>
                        </button>
                        <button
                          onClick={() => setActiveTab('fortune')}
                          className={`flex items-center justify-between px-6 py-2.5 sm:py-4 rounded-2xl border-2 transition-all ${activeTab === 'fortune' ? 'bg-yellow-500/10 border-yellow-500 text-yellow-500 shadow-[0_0_15px_rgba(234,179,8,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-yellow-500/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base break-keep">{t('tabFortune')}</span>
                          <span className="text-lg sm:text-xl opacity-80">📅</span>
                        </button>
                        <button
                          onClick={() => setActiveTab('signal')}
                          className={`flex items-center justify-between px-6 py-2.5 sm:py-4 rounded-2xl border-2 transition-all ${activeTab === 'signal' ? 'bg-k-blue/10 border-k-blue text-k-blue shadow-[0_0_15px_rgba(59,130,246,0.2)]' : 'bg-slate-800/50 border-slate-700/50 hover:bg-slate-800 hover:border-k-blue/50 text-slate-400 hover:text-white'}`}
                        >
                          <span className="font-bold text-sm md:text-base break-keep">{t('tabSignal', { name: analysisResult?.chemistry_signal?.idol_name || idolData?.name || '' })}</span>
                          <span className="text-lg sm:text-xl opacity-80">💖</span>
                        </button>
                      </div>

                      {/* Category Content - Gutter Minimalized & Noise Reduced */}
                      <div className="min-h-[300px] relative backdrop-blur-md bg-slate-900/40 rounded-3xl p-1.5 sm:p-4 border border-slate-700/30 -mx-1 sm:mx-0">
                        <AnimatePresence mode="wait">
                          {/* 탭 1: 내 사주 심층 분석 (전문가 조언 포함) */}
                          {activeTab === 'saju' && (
                            <motion.div
                              key="saju-tab"
                              initial={{ opacity: 0, x: 20 }}
                              animate={{ opacity: 1, x: 0 }}
                              exit={{ opacity: 0, x: -20 }}
                              transition={{ duration: 0.3 }}
                              className="flex flex-col gap-6 h-full"
                            >
                              {/* Lifetime Fortune Panel */}
                              {analysisResult?.lifetime_fortune && (
                                <div className="bg-gradient-to-br from-indigo-900/60 to-slate-900/80 rounded-2xl p-4 sm:p-6 border border-k-purple/40 shadow-2xl relative overflow-hidden backdrop-blur-xl">
                                  <div className="absolute top-0 right-0 w-32 h-32 bg-k-purple/20 rounded-full blur-3xl"></div>
                                  <div className="flex items-center gap-2 mb-4 px-3 py-1.5 bg-k-purple/30 border border-k-purple/50 rounded-lg w-fit">
                                    <TrendingUp className="h-4 w-4 text-k-pink" />
                                    <span className="text-k-pink text-[10px] font-black uppercase tracking-widest">{t('lifetimeStageTitle')}</span>
                                  </div>

                                  <div className="space-y-4">
                                    {analysisResult.lifetime_fortune.split('\n\n').map((segment: string, i: number) => (
                                      <div key={i} className="p-4 sm:p-5 bg-slate-900/80 rounded-xl border border-slate-600/50 text-slate-200 text-sm sm:text-[15px] leading-relaxed break-keep shadow-inner">
                                        <div className="font-black text-k-blue mb-2 text-xs uppercase tracking-tighter opacity-80">{t('stage')} {i + 1}</div>
                                        {segment}
                                      </div>
                                    ))}
                                  </div>
                                </div>
                              )}

                              {/* Expert Advice Grid (NEW Phase 15) */}
                              {analysisResult?.chemistry_signal?.expert_advice && (
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                  {Object.entries(analysisResult.chemistry_signal.expert_advice).map(([cat, pool]: [string, any]) => (
                                    <div key={cat} className="bg-slate-800/40 border border-slate-700/50 rounded-2xl p-5 hover:border-k-blue/30 transition-all">
                                      <div className="flex items-center gap-2 mb-3">
                                        <div className="w-8 h-8 rounded-full bg-slate-900 flex items-center justify-center text-sm border border-slate-700/50 shadow-inner">
                                          {cat === 'Health' ? '🍎' : cat === 'Wealth' ? '💰' : cat === 'Career' ? '💼' : '❤️'}
                                        </div>
                                        <span className="text-xs font-black text-slate-200 uppercase tracking-tighter">{t(`expert${cat}`)}</span>
                                      </div>
                                      <div className="space-y-2">
                                        {pool.map((txt: string, i: number) => (
                                          <p key={i} className="text-[11px] leading-relaxed text-slate-400 pl-2 border-l border-slate-700">
                                            {txt}
                                          </p>
                                        ))}
                                      </div>
                                    </div>
                                  ))}
                                </div>
                              )}

                              {/* Expert Consultant Comments (NEW Phase 15) */}
                              {analysisResult?.chemistry_signal?.lifetime_experts && (
                                <div className="bg-slate-800/60 rounded-2xl p-6 border border-slate-700/50 shadow-lg mt-2">
                                  <h5 className="text-sm font-black text-white mb-4 flex items-center gap-2">
                                    <MessageSquare className="h-4 w-4 text-k-pink" />
                                    {t('expertCommentTitle')}
                                  </h5>
                                  <div className="space-y-4">
                                    {analysisResult.chemistry_signal.lifetime_experts.map((exp: any, i: number) => (
                                      <div key={i} className="p-4 bg-slate-900/40 rounded-xl border border-slate-700/30 flex gap-4">
                                        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-slate-700 to-slate-900 flex-shrink-0 flex items-center justify-center text-xs font-black text-white border border-slate-600/50">
                                          EX
                                        </div>
                                        <div>
                                          <div className="flex items-center gap-2 mb-1">
                                            <span className="text-xs font-black text-white">{exp.name}</span>
                                            <span className="text-[9px] text-slate-500 font-bold px-1.5 py-0.5 bg-slate-800 rounded">{exp.focus}</span>
                                          </div>
                                          <p className="text-[11px] text-slate-300 leading-relaxed italic line-clamp-2 md:line-clamp-none">"{exp.comment}"</p>
                                        </div>
                                      </div>
                                    ))}
                                  </div>
                                </div>
                              )}

                              {/* Existing Saju Content (Layout Optimized for Mobile) */}
                              <div className="bg-slate-800/60 rounded-2xl p-4 sm:p-8 border border-slate-700/50 shadow-lg w-full">
                                <div className="flex items-center gap-2 mb-4 px-3 py-1.5 bg-indigo-500/10 border border-indigo-500/30 rounded-lg w-fit">
                                  <span className="text-indigo-400 text-[10px] font-black uppercase tracking-widest">{t('userSajuResult')}</span>
                                </div>
                                <h4 className="text-xl sm:text-2xl font-black mb-4 text-white break-keep leading-tight">
                                  {analysisResult?.user_saju?.summary || analysisResult?.label}
                                </h4>
                                <div className="text-slate-300 text-[15px] sm:text-base leading-relaxed whitespace-pre-wrap break-keep">
                                  {analysisResult?.user_saju?.content || t('sajuSuccess')}
                                </div>
                              </div>
                            </motion.div>
                          )}

                          {/* 탭 2: 올해의 K-운세 (월별 캘린더 상세 확장) */}
                          {activeTab === 'fortune' && analysisResult?.monthly_fortune && (
                            <motion.div
                              key="fortune-tab"
                              initial={{ opacity: 0, x: 20 }}
                              animate={{ opacity: 1, x: 0 }}
                              exit={{ opacity: 0, x: -20 }}
                              transition={{ duration: 0.3 }}
                              className="flex flex-col gap-4"
                            >
                              <div className="grid grid-cols-1 gap-4 pb-10">
                                {analysisResult.monthly_fortune.map((mf: any, idx: number) => (
                                  <motion.div
                                    key={idx}
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: idx * 0.05 }}
                                    className="bg-slate-800/60 p-6 rounded-3xl border border-slate-700/50 hover:border-yellow-500/30 transition-all shadow-lg group"
                                  >
                                    <div className="flex items-center justify-between mb-4">
                                      <div className="flex items-center gap-3">
                                        <div className="w-10 h-10 rounded-2xl bg-yellow-500/20 flex items-center justify-center text-lg font-black text-yellow-500 border border-yellow-500/30 shadow-inner">
                                          {mf.month}
                                        </div>
                                        <div>
                                          <h4 className="text-white font-black text-base md:text-lg break-keep">{mf.theme || mf.keyword}</h4>
                                          {mf.synergy && (
                                            <div className="flex items-center gap-1 mt-0.5">
                                              <div className="h-1 w-20 bg-slate-700 rounded-full overflow-hidden">
                                                <div className="h-full bg-yellow-500" style={{ width: `${mf.synergy}%` }}></div>
                                              </div>
                                              <span className="text-[10px] text-yellow-500/70 font-bold">{mf.synergy}% Synergy</span>
                                            </div>
                                          )}
                                        </div>
                                      </div>
                                      <Calendar className="h-5 w-5 text-slate-600 group-hover:text-yellow-500/50 transition-colors" />
                                    </div>

                                    <div className="space-y-4">
                                      {/* Signal with Idol */}
                                      <div className="flex gap-3 items-start p-3 bg-slate-900/50 rounded-2xl border border-slate-700/30">
                                        <div className="p-2 bg-k-blue/10 rounded-xl">
                                          <Zap className="w-5 h-5 text-k-blue" />
                                        </div>
                                        <div>
                                          <p className="text-[10px] font-black text-k-blue uppercase tracking-widest mb-1">Star Signal</p>
                                          <p className="text-sm text-slate-300 leading-loose font-medium break-keep">{mf.signal}</p>
                                        </div>
                                      </div>

                                      {/* Action Guide */}
                                      <div className="flex gap-3 items-start p-3 bg-yellow-500/5 rounded-2xl border border-yellow-500/20">
                                        <div className="p-2 bg-yellow-500/10 rounded-xl">
                                          <Target className="w-5 h-5 text-yellow-500" />
                                        </div>
                                        <div>
                                          <p className="text-[10px] font-black text-yellow-500 uppercase tracking-widest mb-1">Action Point</p>
                                          <p className="text-sm text-slate-300 leading-loose break-keep">{mf.guide}</p>
                                        </div>
                                      </div>
                                    </div>
                                  </motion.div>
                                ))}
                              </div>
                            </motion.div>
                          )}

                          {/* 탭 3: 아이돌 궁합 시그널 */}
                          {activeTab === 'signal' && analysisResult?.chemistry_signal && (
                            <motion.div
                              key="signal-tab"
                              initial={{ opacity: 0, x: 20 }}
                              animate={{ opacity: 1, x: 0 }}
                              exit={{ opacity: 0, x: -20 }}
                              transition={{ duration: 0.3 }}
                              className="bg-gradient-to-br from-k-purple/10 to-k-blue/10 rounded-2xl p-6 mb-4 border border-k-purple/20 shadow-lg h-full"
                            >

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

                              {/* Chemistry Signal Card - Re-engineered for Mobile Gutter Minimization */}
                              <motion.div
                                initial={{ opacity: 0, scale: 0.98 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ duration: 0.8 }}
                                className="relative overflow-hidden group mb-8 rounded-[2rem] glass-premium result-card-glow w-full"
                                style={{ '--theme-accent': getElementTheme(analysisResult.dominant_element).accent } as React.CSSProperties}
                              >
                                <ParticleField element={analysisResult.dominant_element} />
                                <div className="p-5 sm:p-8 relative z-10 w-full">
                                  <div className="flex flex-col md:flex-row items-center gap-10">
                                    {/* Gauge Section */}
                                    <div className="relative w-48 h-48 flex-shrink-0">
                                      <svg className="w-full h-full transform -rotate-90">
                                        <circle
                                          cx="96" cy="96" r="88"
                                          fill="transparent"
                                          stroke="currentColor"
                                          strokeWidth="12"
                                          className="text-slate-700/30"
                                        />
                                        <motion.circle
                                          cx="96" cy="96" r="88"
                                          fill="transparent"
                                          stroke={getElementTheme(analysisResult.dominant_element).accent}
                                          strokeWidth="12"
                                          strokeDasharray={552.92}
                                          initial={{ strokeDashoffset: 552.92 }}
                                          animate={{
                                            strokeDashoffset: 552.92 - (552.92 * Math.min(100, analysisResult.chemistry_signal.base_synergy_score + (analysisResult.chemistry_signal.synergy_missions || []).filter((m: any) => completedMissions.includes(m.id)).reduce((acc: number, m: any) => acc + (m.boost || 0), 0))) / 100
                                          }}
                                          transition={{ duration: 2, ease: "easeOut" }}
                                          strokeLinecap="round"
                                        />
                                      </svg>
                                      <div className="absolute inset-0 flex flex-col items-center justify-center">
                                        <motion.span
                                          initial={{ scale: 0.5, opacity: 0 }}
                                          animate={{ scale: 1, opacity: 1 }}
                                          className="text-5xl font-black text-white"
                                        >
                                          <CountingScore targetScore={Math.min(100, analysisResult.chemistry_signal.base_synergy_score + (analysisResult.chemistry_signal.synergy_missions || []).filter((m: any) => completedMissions.includes(m.id)).reduce((acc: number, m: any) => acc + (m.boost || 0), 0))} />
                                        </motion.span>
                                        <span className="text-xs font-bold uppercase tracking-widest text-slate-400">{t('destinyEnergy')}</span>
                                      </div>
                                    </div>

                                    <div className="flex-1">
                                      <div className="mb-6 relative">
                                        <div className="absolute top-0 left-0 w-1.5 h-full rounded-full" style={{ background: getElementTheme(analysisResult.dominant_element).accent }}></div>
                                        <div className="pl-6 py-1">
                                          <h4 className="text-2xl font-black text-white mb-2">{analysisResult.chemistry_signal.idol_name} {t('youLabel')}</h4>
                                          <p className="text-slate-400 text-sm font-medium leading-loose">
                                            {analysisResult.chemistry_signal.synergy}
                                          </p>
                                        </div>
                                      </div>

                                      <div className="flex flex-wrap gap-2">
                                        {(() => {
                                          const score = analysisResult.chemistry_signal.base_synergy_score;
                                          let levelKey = 'levelStart';
                                          if (score >= 95) levelKey = 'levelDestiny';
                                          else if (score >= 90) levelKey = 'levelSoulmate';
                                          else if (score >= 85) levelKey = 'levelDeepBond';
                                          else if (score >= 80) levelKey = 'levelResonance';
                                          else if (score >= 70) levelKey = 'levelInterest';

                                          return (
                                            <div className="px-4 py-2 bg-white/5 rounded-full border border-white/10 flex items-center gap-2">
                                              <Sparkles className="h-3.5 w-3.5" style={{ color: getElementTheme(analysisResult.dominant_element).accent }} />
                                              <span className="text-xs font-black text-white tracking-wide uppercase">{t(levelKey)}</span>
                                            </div>
                                          );
                                        })()}
                                        <div className="px-4 py-2 bg-white/5 rounded-full border border-white/10 flex items-center gap-2">
                                          <BrainCircuit className="h-3.5 w-3.5 text-k-blue" />
                                          <span className="text-xs font-black text-white tracking-wide uppercase">{analysisResult.chemistry_signal.idol_mbti}</span>
                                        </div>
                                      </div>
                                    </div>
                                  </div>

                                  <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
                                    {/* 좌측: 상대방 성향 & 관계 Deep Dive */}
                                    <div className="bg-slate-900/40 p-4 sm:p-6 rounded-2xl border border-slate-600/50 backdrop-blur-sm">
                                      <div className="flex items-center gap-2 mb-4">
                                        <Sparkles className="h-5 w-5 text-k-pink" />
                                        <span className="font-black text-white text-lg">{t('idolTraits')}</span>
                                      </div>

                                      <div className="space-y-5">
                                        {/* 관계 개요 (1-2문장) */}
                                        <div className="p-4 sm:p-5 bg-k-purple/10 rounded-xl border border-k-purple/20">
                                          <p className="text-sm text-slate-200 font-semibold leading-loose sm:leading-relaxed break-keep whitespace-pre-wrap">
                                            {analysisResult.chemistry_signal.relationship}
                                          </p>
                                        </div>

                                        {/* 본질 및 특징 (3-4문장) */}
                                        <div className="space-y-2">
                                          <p className="text-sm text-slate-300 leading-loose pl-4 border-l-2 border-k-pink/50 py-1 break-keep whitespace-pre-wrap">
                                            {analysisResult.chemistry_signal.bias}
                                          </p>
                                          <p className="text-[11px] text-slate-400 leading-loose italic pl-4 break-keep whitespace-pre-wrap">
                                            {analysisResult.chemistry_signal.tmi}
                                          </p>
                                        </div>

                                        {/* 시너지 원인 분석 (New) */}
                                        {analysisResult.chemistry_signal.synergyWhy && (
                                          <div className="pt-3 mt-3 border-t border-slate-700/30">
                                            <p className="text-[11px] text-k-blue font-bold italic">
                                              ✨ {analysisResult.chemistry_signal.synergyWhy}
                                            </p>
                                          </div>
                                        )}
                                      </div>
                                    </div>

                                    {/* 우측: 최근 운세 및 꿀팁 */}
                                    <div className="bg-slate-900/50 rounded-2xl p-4 sm:p-6 border border-slate-600/50">
                                      <div className="flex items-center gap-2 mb-4">
                                        <TrendingUp className="h-5 w-5 text-k-green" />
                                        <p className="text-lg font-black text-white">{t('recentFortune')}</p>
                                      </div>

                                      <div className="space-y-4">
                                        <p className="text-sm text-slate-300 bg-slate-800/60 p-4 sm:p-5 rounded-xl border border-slate-700/50 leading-loose sm:leading-relaxed font-medium break-keep whitespace-pre-wrap">
                                          {analysisResult.chemistry_signal.recentFortune}
                                        </p>

                                        <div className="pt-2">
                                          <p className="text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2 px-1">{t('attackTips') || 'Strategy'}</p>
                                          <ul className="grid grid-cols-1 gap-3 sm:gap-4">
                                            {analysisResult.chemistry_signal.tips?.map((tip: string, idx: number) => (
                                              <li key={idx} className="text-[11px] sm:text-xs text-slate-300 bg-slate-800/40 p-4 sm:p-5 rounded-lg border border-slate-700/50 flex items-start gap-3 shadow-sm">
                                                <span className="text-k-pink mt-0.5">•</span>
                                                <span className="leading-loose sm:leading-relaxed break-keep whitespace-pre-wrap">{tip}</span>
                                              </li>
                                            ))}
                                          </ul>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </motion.div>

                              {/* Missions Section */}
                              {analysisResult.chemistry_signal.synergy_missions && (
                                <div className="mt-8">
                                  <h3 className="text-lg font-black text-white mb-4 flex items-center gap-2">
                                    <div className="w-8 h-8 rounded-lg bg-k-pink/10 flex items-center justify-center">
                                      <Sparkles className="h-5 w-5 text-k-pink" />
                                    </div>
                                    {t('missionTitle')}
                                  </h3>
                                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                    {analysisResult.chemistry_signal.synergy_missions.map((mission: any) => {
                                      const isCompleted = completedMissions.includes(mission.id);
                                      return (
                                        <motion.div
                                          key={mission.id}
                                          whileHover={{ y: -5 }}
                                          onClick={() => {
                                            if (isCompleted) {
                                              setCompletedMissions(prev => prev.filter(id => id !== mission.id));
                                            } else {
                                              setCompletedMissions(prev => [...prev, mission.id]);
                                            }
                                          }}
                                          className={`p-5 rounded-2xl border transition-all cursor-pointer group ${isCompleted ? 'bg-emerald-500/10 border-emerald-500/40' : 'bg-slate-800/60 border-slate-700/50 hover:border-k-pink/40'}`}
                                        >
                                          <div className="flex items-start justify-between mb-3">
                                            <div className={`w-10 h-10 rounded-xl flex items-center justify-center font-black transition-colors ${isCompleted ? 'bg-emerald-500 text-white' : 'bg-slate-900/50 text-k-pink'}`}>
                                              {isCompleted ? '✓' : `+${mission.boost}`}
                                            </div>
                                            {isCompleted && <ThumbsUp className="h-5 w-5 text-emerald-400 fill-emerald-400" />}
                                          </div>
                                          <h5 className={`text-sm font-black mb-1 leading-snug transition-colors ${isCompleted ? 'text-emerald-300 line-through' : 'text-white group-hover:text-k-pink'}`}>
                                            {mission.label}
                                          </h5>
                                          <p className="text-[10px] text-slate-500 font-bold uppercase tracking-tight mb-3">{mission.reason || t('missionDesc')}</p>

                                          {/* Sub-Tasks 3x3 Structure */}
                                          <div className="space-y-2 pt-1">
                                            {(mission.tasks || []).map((task: string, tIdx: number) => (
                                              <div
                                                key={tIdx}
                                                className={`flex items-start gap-2 p-2 rounded-lg border transition-all ${isCompleted ? 'bg-emerald-500/5 border-emerald-500/10' : 'bg-slate-900/40 border-slate-700/30 group-hover:border-k-pink/20'}`}
                                              >
                                                <div className={`mt-0.5 h-3.5 w-3.5 rounded-full border flex items-center justify-center text-[8px] flex-shrink-0 ${isCompleted ? 'border-emerald-500/40 text-emerald-400' : 'border-slate-600 text-slate-500'}`}>
                                                  {isCompleted ? '✓' : tIdx + 1}
                                                </div>
                                                <span className={`text-[11px] leading-tight ${isCompleted ? 'text-emerald-500/60 line-through' : 'text-slate-400 font-medium'}`}>
                                                  {task}
                                                </span>
                                              </div>
                                            ))}
                                          </div>
                                        </motion.div>
                                      );
                                    })}
                                  </div>
                                </div>
                              )}

                              <motion.button
                                whileHover={{ scale: 1.02 }}
                                whileTap={{ scale: 0.98 }}
                                onClick={handleShare}
                                className="w-full py-4 bg-white text-slate-900 rounded-2xl font-black text-lg hover:bg-slate-100 transition-all flex items-center justify-center gap-2 shadow-xl mb-12"
                              >
                                <Share2 className="h-5 w-5" /> {t('shareResult')}
                              </motion.button>

                              {analysisResult && (
                                <SoulCommunity
                                  comments={comments}
                                  onPostComment={handlePostComment}
                                  onDeleteComment={handleDeleteComment}
                                  isAdmin={isAdmin}
                                  isPosting={isPostingComment}
                                  commentText={commentText}
                                  setCommentText={setCommentText}
                                  t={t}
                                />
                              )}
                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>
                    </motion.div>
                  )}
                </motion.div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <AnimatePresence>
        {showMBTIQuiz && (
          <QuickMBTI
            lang={lang}
            onClose={() => setShowMBTIQuiz(false)}
            onComplete={(mbti: string) => {
              if (mbtiTarget === 'user') {
                setUserMBTI(mbti);
              } else if (mbtiTarget === 'idol') {
                setIdolData((prev: any) => ({ ...prev, mbti: mbti }));
              }
              setShowMBTIQuiz(false);
            }}
          />
        )}
      </AnimatePresence>
      {/* Footer Stats */}
      <div className="max-w-xl mx-auto px-4 mt-8 pb-12 border-t border-slate-800/50 pt-10">
        <div className="flex flex-col sm:flex-row justify-center gap-4 sm:gap-8 mb-8">
          <div className="flex-1 flex flex-col items-center bg-slate-800/50 px-6 sm:px-8 py-5 rounded-2xl border border-slate-700/50 hover:bg-slate-700/50 transition-colors shadow-lg">
            <p className="text-[11px] font-black text-white uppercase tracking-[0.2em] mb-3 opacity-90">{t('visitorsToday')}</p>
            <p className="text-3xl sm:text-4xl font-black text-k-blue drop-shadow-[0_0_10px_rgba(30,144,255,0.3)]">{stats.today_challengers}</p>
          </div>
          <div className="flex-1 flex flex-col items-center bg-slate-800/50 px-6 sm:px-8 py-5 rounded-2xl border border-slate-700/50 hover:bg-slate-700/50 transition-colors shadow-lg">
            <p className="text-[11px] font-black text-white uppercase tracking-[0.2em] mb-3 opacity-90">{t('visitorsTotal')}</p>
            <p className="text-3xl sm:text-4xl font-black text-k-purple drop-shadow-[0_0_10px_rgba(168,85,247,0.3)]">{stats.total_visitors}</p>
          </div>
        </div>
        <p className="text-center text-[11px] font-bold text-slate-300 tracking-widest drop-shadow-sm">
          {t('footer')}
        </p>
      </div>
    </div>
  );
};

export default App;
