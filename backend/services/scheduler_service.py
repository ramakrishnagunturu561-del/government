from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from services.voice_service import send_voice_call
from database import get_db_connection
import calendar

def advance_notification():
    today = datetime.today()
    tomorrow = today + timedelta(days=1)

    if tomorrow.weekday() == 6:  # Sunday
        message_type = "SUNDAY_DELAY"
    else:
        message_type = "TOMORROW_PENSION"

    # send to all pending pension users
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT beneficiary_id FROM beneficiaries WHERE scheme_name='Pension' AND status='Pending'"
    )

    for b in cursor.fetchall():
        send_voice_call(b["beneficiary_id"], message_type)

    conn.close()

def start_scheduler():
    scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
    scheduler.add_job(advance_notification, 'cron', hour=17)
    scheduler.start()
