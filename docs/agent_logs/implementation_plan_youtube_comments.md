# [Goal] 유튜브 스타일 '소울 커뮤니티' 댓글 시스템 구현

사주 분석 결과가 단순한 텍스트 전달에 그치지 않고, 사용자들끼리 자신의 운명을 공유하고 소통할 수 있도록 유튜브 댓글 UI를 완벽하게 재현한 인터랙티브 섹션을 구축합니다.

## Proposed UI/UX Design

### 1. 헤더 (Header)
- **댓글 수 표시**: "495 Comments"와 같이 실시간 느낌의 댓글 수 출력.
- **정렬 기능**: "Sort by (Newest / Top)" 아이콘 버튼 제공.

### 2. 입력창 (Input Area)
- **사용자 아바타**: 기본 프로필 아이콘 또는 사주 오행별 동물 아이콘 배치.
- **Add a Comment...**: 클릭 시 확장되며 '취소' 및 '작성' 버튼 노출.

### 3. 댓글 리스트 (Comment List)
- **핸들 및 시간**: `@UserName` 형식의 핸들과 `1 hour ago` 등의 상대 시간 표시.
- **본문**: 사용자가 작성한 소감 또는 운명 시그널 내용.
- **액션 바**: 좋아요(ThumbsUp), 싫어요(ThumbsDown), 답글(Reply) 버튼.
- **모의 데이터**: 초기 활성화를 위해 각 언어별 MZ 감성의 모의 댓글(Lore) 주입.

## Proposed Changes

### Frontend: [App.tsx](file:///c:/InsuranceProject/Sajuapp/frontend/src/App.tsx)
- `CommentSection` 섹션 추가 (분석 결과 카드 내부 하단).
- `comments` 상태 관리 (작성 기능 포함).
- 유튜브 스타일의 디자인 토큰(CSS) 반영.
- 다국어 번역 키 추가: `totalComments`, `sortBy`, `reply`, `commentPlaceholder`.

## Verification Plan

### Manual Verification
- 언어별(KO, EN, ES, PT) 댓글 리스트 현지화 확인.
- 댓글 입력 및 좋아요 버튼 애니메이션 작동 여부 검토.
- 모바일 환경에서의 댓글 가독성 확보 여부 체크.
