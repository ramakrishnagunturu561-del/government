from database import get_db_connection
import requests
from config import EXOTEL_CONFIG

def send_voice_call(beneficiary_id, call_type):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT name, mobile_number, scheme_name FROM beneficiaries WHERE beneficiary_id=%s",
        (beneficiary_id,)
    )
    user = cursor.fetchone()

    if not user:
        conn.close()
        return

    cursor.execute(
        "INSERT INTO call_logs (beneficiary_id, mobile_number, call_type) VALUES (%s,%s,%s)",
        (beneficiary_id, user["mobile_number"], call_type)
    )

    conn.commit()
    conn.close()

    # REAL EXOTEL INTEGRATION (uncomment with real credentials)
    # url = f"https://api.exotel.com/v1/Accounts/{EXOTEL_CONFIG['SID']}/Calls/connect"
    # payload = {
    #     "From": user["mobile_number"],
    #     "CallerId": EXOTEL_CONFIG["CALLER_ID"],
    #     "Url": "https://your-server/ivr/pension.xml"
    # }
    # requests.post(
    #     url,
    #     data=payload,
    #     auth=(EXOTEL_CONFIG["SID"], EXOTEL_CONFIG["TOKEN"])
    # )

    # DEMO MODE (for presentation)
    print("📞 VOICE CALL")
    print(f"To: {user['mobile_number']}")
    print(f"Message Type: {call_type}")
    print("From: CM Karyalayam")
