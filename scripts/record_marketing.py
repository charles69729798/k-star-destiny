import time
import os
import shutil
from playwright.sync_api import sync_playwright

def record_marketing_video():
    video_dir = os.path.join(os.getcwd(), "marketing_videos")
    os.makedirs(video_dir, exist_ok=True)
    
    with sync_playwright() as p:
        print("🎬 브라우저 실행 및 녹화 준비 중 (V3)...")
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(
            viewport={'width': 390, 'height': 844},
            record_video_dir=video_dir,
            record_video_size={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        )
        page = context.new_page()

        print("🌐 http://localhost 접속...")
        try:
            page.goto("http://localhost")
            
            # 정보 입력을 초고속으로 세팅
            page.get_by_text("ES", exact=True).click()
            page.wait_for_timeout(500)
            
            # 리액트 상태(onChange)가 완벽히 먹히게끔 fill()대신 type() 및 blur 처리
            date_input = page.locator("input[type='date']")
            if date_input.count() > 0:
                # 사용자가 요청한 가상유저 설정 생일: 2010-01-01
                date_input.focus()
                date_input.fill("2010-01-01")
                date_input.press("Enter")
                date_input.blur() 
            page.wait_for_timeout(500)
            
            # 라벨명(스페인어 등 다국어)에 의존하지 않고 HTML value 값으로 확실히 선택
            # 사용자 요청: Female(여성)
            gender_select = page.locator("select").nth(0)
            gender_select.select_option(value="female")
            gender_select.blur()
            page.wait_for_timeout(500)
            
            # 사용자 요청: ENTP
            mbti_select = page.locator("select").nth(1)
            mbti_select.select_option(value="ENTP")
            mbti_select.blur()
            page.wait_for_timeout(500)

            # === 녹화 실질적 시작 포인트 (사용자에게 "내 정보가 채워졌다"는 맥락 1.5초 노출) ===
            print("👤 세팅된 내 프로필(2010-01-01, F, ENTP) 1.5초 노출...")
            page.wait_for_timeout(1500)

            print("🌟 타겟 아이돌 선택을 위해 살짝 스크롤 다운...")
            page.mouse.wheel(0, 300)
            page.wait_for_timeout(800)
            
            # 송강 클릭: React 상태 기반으로 라우팅이 원활하게 넘어가도록 wait 추가
            song_kang_card = page.get_by_text("Song Kang")
            song_kang_card.hover()
            page.wait_for_timeout(300)
            song_kang_card.click()
            
            print("⏳ 로딩 중... 결과창 준비!")
            page.wait_for_timeout(5500)

            print("🚀 매칭 결과창 진입 (83점 노출 1.5초)!")
            page.wait_for_timeout(1500)

            print("🏃‍♂️ 미션 영역으로 폭풍 스크롤다운")
            page.mouse.wheel(0, 800)
            page.wait_for_timeout(800)
            page.mouse.wheel(0, 400)
            page.wait_for_timeout(1000)

            print("✅ 미션 체크박스 다이나믹 클릭 (Gamification)!")
            checkboxes = page.locator("input[type='checkbox']")
            if checkboxes.count() >= 2:
                # 빠른 템포로 2개 체크
                checkboxes.nth(0).check()
                page.wait_for_timeout(800)
                checkboxes.nth(1).check()
                page.wait_for_timeout(800)
                
                print("🌟 줌업! 점수 상승 확인을 위해 위로 화면 스크롤!")
                page.mouse.wheel(0, -1200) # 단번에 상단으로
                page.wait_for_timeout(2500) # 높아진 점수 감상

            print("🎉 V3 영상 녹화 흐름 종료!")
            video_path = page.video.path()
            
        except Exception as e:
            print(f"❌ 녹화 중 에러 발생: {e}")
            video_path = None
            
        finally:
            page.close()
            context.close()
            browser.close()
            
            time.sleep(2)
            if video_path and os.path.exists(video_path):
                dest_path = os.path.join(video_dir, "raw_marketing_v4.webm")
                shutil.copy(video_path, dest_path)
                print(f"🎬 비디오(V4) 성공적 저장: {dest_path}")
            else:
                print("❌ 비디오 파일을 물리적으로 찾을 수 없습니다!")

if __name__ == "__main__":
    record_marketing_video()
