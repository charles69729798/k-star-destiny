import os
import subprocess
import urllib.request
import imageio_ffmpeg

def render_v3_user_video():
    video_dir = os.path.join(os.getcwd(), "marketing_videos")
    target_video = os.path.join(video_dir, "2026-03-01 144545.mp4")

    if not os.path.exists(target_video):
        print(f"❌ 사용자 촬영 비디오를 찾을 수 없습니다! ({target_video})")
        return

    print(f"🎬 V3 기반 커스텀 원본 비디오 감지: {target_video}")

    # V3 마케팅 대본 SRT 생성 (가상유저 몰입형)
    # 텍스트 내 스페인어 역물음표/역느낌표 제거 적용 완료
    srt_content = """1
00:00:00,500 --> 00:00:02,000
Mi perfil listo 📝

2
00:00:02,100 --> 00:00:04,500
Vamos por Song Kang! 😍

3
00:00:07,000 --> 00:00:09,000
83 puntos! Nada mal...

4
00:00:09,100 --> 00:00:11,500
Pero voy por el 100 con misiones! 🔥

5
00:00:11,600 --> 00:00:14,000
Nivel superado! Sube tu quimica en el link 👇
"""

    srt_path = os.path.join(video_dir, "marketing_subs_v3_user.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
        
    print(f"📝 V3 대본 자막 파일(SRT) 생성 완료: {srt_path}")

    # K-Destiny 분위기에 맞는 BGM 다운로드 (기존 트랙 교체 - 약간 더 영롱/신나는 비트)
    bgm_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    bgm_path = os.path.join(video_dir, "bgm_kdestiny.mp3")

    if not os.path.exists(bgm_path):
        print("🎵 K-Destiny 스타일 BGM 오디오 다운로드 중...")
        try:
            urllib.request.urlretrieve(bgm_url, bgm_path)
            print("✅ BGM 다운로드 완료!")
        except Exception as e:
            print(f"⚠️ BGM 다운로드 실패: {e}")

    # FFmpeg 구동
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    output_mp4 = "FINAL_V3_UserCustom_BottomSubs.mp4"
    output_path = os.path.join(video_dir, output_mp4)

    in_video = os.path.basename(target_video)
    in_srt = "marketing_subs_v3_user.srt"
    in_bgm = "bgm_kdestiny.mp3"

    # 옵션 수정 요약:
    # 1. 자막 배치: 화면 하단(Alignment=2), 여백 40 적용으로 UI와 시선 덜 마주치게 조정
    # 2. 글자 크기: 적절하게 줄이기 (FontSize=15)
    # 3. 그림자/테두리 추가로 화면 아래쪽의 프로필 이미지 등과 겹쳐도 글자가 잘 보이게 방어
    cmd = [
        ffmpeg_exe,
        "-y",
        "-stream_loop", "-1",   
        "-i", in_video,         
        "-i", in_bgm,           
        "-vf", f"subtitles={in_srt}:force_style='FontSize=15,PrimaryColour=&H00FFFF,Bold=1,MarginV=40,Alignment=2,OutlineColour=&H40000000,BorderStyle=3,Shadow=2'",
        "-map", "0:v:0",        
        "-map", "1:a:0?",       
        "-c:v", "libx264",      
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",            
        output_mp4
    ]

    print("⏳ FFmpeg [V3 대본 + 하단 자막 렌더링 + K-Destiny BGM] 합성 중...")
    try:
        result = subprocess.run(cmd, cwd=video_dir, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"🎉 V3 맞춤 렌더링 성공! 최종 영상: {output_path}")
        else:
            print("❌ 렌더링 실패!")
            print(result.stderr)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    render_v3_user_video()
