import os
import subprocess
import urllib.request
import imageio_ffmpeg

def render_user_video():
    video_dir = os.path.join(os.getcwd(), "marketing_videos")
    # 사용자님이 직접 촬영하신 영상 파일명 지정
    target_video = os.path.join(video_dir, "2026-03-01 144545.mp4")

    if not os.path.exists(target_video):
        print(f"❌ 사용자 촬영 비디오를 찾을 수 없습니다! ({target_video})")
        return

    print(f"🎬 사용자 직접 녹화 원본 감지: {target_video}")

    # 마케팅 팀이 엄선한 V4 틱톡 감성 대본 SRT 생성 (15~20초 분량 대응)
    # 타이밍은 기획안의 "입력완료 -> 타겟선택 -> 매칭 -> 점수상승" 평균 속도에 맞게 넉넉히 배분
    srt_content = """1
00:00:00,500 --> 00:00:02,500
Mi perfil listo 📝

2
00:00:03,000 --> 00:00:05,500
Vamos por Song Kang! 😍

3
00:00:07,000 --> 00:00:10,000
Increíble puntuación! Nada mal... 😘

4
00:00:10,500 --> 00:00:13,500
Pero voy por el 100 con misiones! 🔥

5
00:00:14,000 --> 00:00:30,000
Nivel superado! Sube tu química en el link 👇
"""

    srt_path = os.path.join(video_dir, "marketing_subs_user.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
        
    print(f"📝 사용자 커스텀 자막(SRT) 생성 완료: {srt_path}")

    # BGM 오디오 연동 (신나는 무료 비트)
    bgm_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    bgm_path = os.path.join(video_dir, "bgm.mp3")

    if not os.path.exists(bgm_path):
        print("🎵 무료 BGM 다운로드 중...")
        try:
            urllib.request.urlretrieve(bgm_url, bgm_path)
            print("✅ BGM 다운로드 완료!")
        except Exception as e:
            print(f"⚠️ BGM 다운로드 실패: {e}")

    # FFmpeg 구동
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    output_mp4 = "FINAL_UserCustom_Marketing_Shorts.mp4"
    output_path = os.path.join(video_dir, output_mp4)

    in_video = os.path.basename(target_video)
    in_srt = "marketing_subs_user.srt"
    in_bgm = "bgm.mp3"

    # FFmpeg 옵션: 비디오는 자체 영상(0:v), 오디오는 자체 오디오 제거 후 BGM(1:a) 입히기
    # FontSize=16, 상단 중앙 (Alignment=8), 여백(MarginV=60) 로 모바일 세로 영상에 이쁘게 안착
    cmd = [
        ffmpeg_exe,
        "-y",
        "-stream_loop", "-1",   # BGM이 짧아도 영상 길이만큼 자동 반복
        "-i", in_video,         # 0:v
        "-i", in_bgm,           # 1:a
        "-vf", f"subtitles={in_srt}:force_style='FontSize=16,PrimaryColour=&H00FFFF,Bold=1,MarginV=60,Alignment=8,OutlineColour=&H40000000,BorderStyle=3,Shadow=3'",
        "-map", "0:v:0",        # 사용자의 깨끗한 원본 화면 가져오기
        "-map", "1:a:0?",       # BGM 오디오 올리기
        "-c:v", "libx264",      # 렌더링 안정성 코덱
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",            # 영상 길이에 맞춰서 자르기
        output_mp4
    ]

    print("⏳ [사용자 원본 영상 + BGM + 스페인어 마케팅 자막] 렌더링 중... (최대 1~3분 소요)")
    try:
        result = subprocess.run(cmd, cwd=video_dir, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"🎉 사용자 맞춤 렌더링 완벽 성공! 최종 숏폼: {output_path}")
        else:
            print("❌ 렌더링 실패!")
            print(result.stderr)
    except Exception as e:
        print(f"❌ 프로세스 오류 발생: {e}")

if __name__ == "__main__":
    render_user_video()
