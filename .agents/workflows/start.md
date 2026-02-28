---
description: 포트 정리 후 최신 코드로 서버 재구동
---
규칙(Rules)에 따라 서버를 재구동할 때 다음 단계를 거칩니다:

1. 프론트엔드 환경변수 파일 확립
// turbo
`echo VITE_API_URL=http://localhost/api > frontend/.env.local`

2. 기존 연결된 5173 포트 종료 및 npm run dev 구동 (Force 캐시 무효화)
// turbo
`$p=Get-NetTCPConnection -LocalPort 5173 -ErrorAction SilentlyContinue; if ($p) { Stop-Process -Id $p.OwningProcess -Force -ErrorAction SilentlyContinue }; cd frontend; npm run dev -- --force`