# 에이전트 작업 로그 동기화 스크립트
# 시스템 내부 브레인 폴더의 최신 문서를 프로젝트의 docs/agent_logs로 복사합니다.

$SourcePath = "C:\Users\pc1\.gemini\antigravity\brain\d64370ba-7db7-4720-bdb4-440d2de7350b"
$DestPath = "c:\InsuranceProject\Sajuapp\docs\agent_logs"

if (Test-Path $SourcePath) {
    if (-not (Test-Path $DestPath)) {
        New-Item -ItemType Directory -Path $DestPath -Force
    }
    
    # 불필요한 메타데이터와 시스템 파일을 제외하고 복사
    Copy-Item "$SourcePath\*" $DestPath -Force -Recurse -Exclude *.metadata.json, *.resolved, *.resolved.*, *.system_generated, *.tempmediaStorage
    Write-Host "✅ [$(Get-Date)] 작업 로그 동기화 완료: $DestPath"
}
else {
    Write-Warning "⚠️ 브레인 폴더를 찾을 수 없습니다: $SourcePath"
}
