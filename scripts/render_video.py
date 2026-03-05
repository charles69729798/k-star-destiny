import os
import glob
import subprocess
import urllib.request
import imageio_ffmpeg

# 1. 렌더링 원본 파일 (V4 기반)
video_dir = os.path.join(os.getcwd(), "marketing_videos")
target_video = os.path.join(video_dir, "raw_marketing_v4.webm")

if not os.path.exists(target_video):
    print(f"❌ 녹화된 비디오를 찾을 수 없습니다! ({target_video})")
    exit(1)

print(f"🎬 원본 비디오 감지: {target_video}")

# 2. 마케팅 대본 SRT 생성 (V4: 몰입형 가상유저 시나리오)
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
00:00:11,600 --> 00:00:14,500
Nivel superado! Sube tu química en el link 👇
"""

srt_path = os.path.join(video_dir, "marketing_subs_v4.srt")
with open(srt_path, "w", encoding="utf-8") as f:
    f.write(srt_content)
    
print(f"📝 자막 파일(SRT) 생성 완료: {srt_path}")

# 2.5 무료 BGM 오디오 다운로드 연동
bgm_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
bgm_path = os.path.join(video_dir, "bgm.mp3")

if not os.path.exists(bgm_path):
    print("🎵 무료 BGM 다운로드 중... (임시)")
    try:
        urllib.request.urlretrieve(bgm_url, bgm_path)
        print("✅ BGM 다운로드 완료!")
    except Exception as e:
        print(f"⚠️ BGM 다운로드 실패: {e}")

# 3. FFmpeg 구동 및 자막/오디오 합성
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
output_mp4 = "FINAL_Marketing_V4_Shorts.mp4"

working_dir = video_dir.replace("\\", "/")
in_video = os.path.basename(target_video)
in_srt = "marketing_subs_v4.srt"
in_bgm = "bgm.mp3"

cmd = [
    ffmpeg_exe,
    "-y",
    "-stream_loop", "-1",   # 오디오 파일이 짧아도 영상 길이에 맞게 무한 반복
    "-i", in_video,         # 0:v (원본 영상 웹엠)
    "-i", in_bgm,           # 1:a (다운받은 BGM)
    "-vf", f"subtitles={in_srt}:force_style='FontSize=16,PrimaryColour=&H00FFFF,Bold=1,MarginV=60,Alignment=8,OutlineColour=&H40000000,BorderStyle=3,Shadow=2'",
    "-map", "0:v:0",        # 영상의 비디오 스트림 매핑
    "-map", "1:a:0?",       # BGM 오디오 스트림 매핑 (옵셔널)
    "-c:v", "libx264",      # 렌더링 코덱
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",            # 가장 짧은 스트림(영상) 길이에 맞춰 최종 파일 자르기
    output_mp4
]

print("⏳ FFmpeg 자막 + BGM 오디오 믹싱 렌더링 중... (최대 1~2분 소요)")
try:
    result = subprocess.run(cmd, cwd=video_dir, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"🎉 렌더링(V5) 성공! 최종 영상: {os.path.join(video_dir, output_mp4)}")
    else:
        print("❌ 렌더링 실패!")
        print(result.stderr)
except Exception as e:
    print(f"❌ 오류 발생: {e}")
