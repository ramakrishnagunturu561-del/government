from flask import Blueprint, request, jsonify
from services.voice_service import send_voice_call
from database import get_db_connection

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/pension-update", methods=["POST"])
def pension_update():
    data = request.json

    beneficiary_id = data.get("beneficiary_id")
    status = data.get("status")

    if status != "Delivered":
        return jsonify({"message": "No action required"}), 200

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "UPDATE beneficiaries SET status='Delivered' WHERE beneficiary_id=%s",
        (beneficiary_id,)
    )

    conn.commit()
    conn.close()

    # 🔔 REAL-TIME ACTION
    send_voice_call(beneficiary_id, "PENSION_DELIVERED")

    return jsonify({"message": "Webhook processed successfully"})
