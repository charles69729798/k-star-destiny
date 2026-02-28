import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Configuration
REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDOLS_FILE = os.path.join(os.path.dirname(__file__), "idols.json")
OWNER_EMAIL = "hyjt01234@gmail.com"

# Email credentials (To be configured in .env)
# 💡 사장님이 .env 파일에 EMAIL_USER와 EMAIL_PASSWORD(App Password)를 설정해야 합니다.
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email_notification(subject, body):
    if not EMAIL_USER or not EMAIL_PASSWORD:
        print("⚠️ [Warning] Email credentials not found in environment variables. Skipping notification.")
        return False
    
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = OWNER_EMAIL
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"📧 Notification email sent to {OWNER_EMAIL}")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def push_to_git(new_idols_count):
    try:
        # 1. Git Status Check
        os.chdir(REPO_PATH)
        
        # 변경 사항이 있는지 확인
        status = subprocess.check_output(["git", "status", "--porcelain", IDOLS_FILE]).decode("utf-8")
        
        if not status and new_idols_count == 0:
            print("ℹ️ No changes detected in idols.json. Skipping Git push.")
            subject = "✅ [K-Destiny] 무인 갱신 봇: 이상 없음 (최신 상태)"
            body = f"""안녕하세요, 사장님!

웹 서버의 데이터 봇이 업무를 마쳤습니다.

- 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 결과: 현재 모든 데이터가 최신 상태입니다. 추가된 정보가 없어 Git 동기화를 건너뛰었습니다.

안심하고 서비스를 이용해 주세요.
감사합니다."""
            send_email_notification(subject, body)
            return True

        # 2. Git Add
        subprocess.run(["git", "add", IDOLS_FILE], check=True)
        
        # 3. Git Commit (변경된 내용이 있을 때만 실행)
        commit_msg = f"📊 [Auto-Bot] Updated idols.json with {new_idols_count} new entries ({datetime.now().strftime('%Y-%m-%d %H:%M')})"
        # --allow-empty를 쓰거나, 위에서 status 체크를 이미 했으므로 안전함
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        
        # 4. Git Push
        subprocess.run(["git", "push"], check=True)
        
        print("✅ Git Push successful.")
        
        # 5. Email Notification
        subject = f"✅ [K-Destiny] 무인 갱신 봇: 아이돌 {new_idols_count}명 추가 완료"
        body = f"""안녕하세요, 사장님!

웹 서버의 데이터 봇이 업무를 완료했습니다.

- 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 추가된 아이돌 수: {new_idols_count}명
- 결과: Git 창고(GitHub)에 성공적으로 업데이트되었습니다.

로컬 PC에서 'git pull'을 실행하여 최신 데이터를 받아주시기 바랍니다.

감사합니다.
K-Destiny AI Bot 드림
"""
        send_email_notification(subject, body)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")
        error_subject = "⚠️ [K-Destiny] 무인 갱신 봇: 업데이트 실패 알림"
        error_body = f"데이터 봇 작업 중 Git 연동 오류가 발생했습니다.\n\n오류 내용: {str(e)}"
        send_email_notification(error_subject, error_body)
        return False
    except Exception as e:
        print(f"❌ Unknown error during Sync: {e}")
        return False

if __name__ == "__main__":
    # Test call
    push_to_git(0)
