from flask import Blueprint, request, jsonify
from database import get_db_connection
from services.voice_service import send_voice_call

pension_bp = Blueprint("pension", __name__)

@pension_bp.route("/deliver", methods=["POST"])
def deliver_pension():
    data = request.json
    beneficiary_id = data["beneficiary_id"]
    delivery_date = data["delivery_date"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Check beneficiary details first
    cursor.execute(
        "SELECT scheme_name, status FROM beneficiaries WHERE beneficiary_id=%s",
        (beneficiary_id,)
    )
    beneficiary = cursor.fetchone()
    
    if not beneficiary:
        conn.close()
        return jsonify({"message": "Beneficiary not found"}), 404
    
    # Event-based validation: Only allow Pension + Pending
    if beneficiary["scheme_name"] != "Pension" or beneficiary["status"] != "Pending":
        conn.close()
        return jsonify({"message": "Only pending pension schemes can be delivered"}), 400
    
    # Update status
    cursor.execute("""
        UPDATE beneficiaries
        SET status='Delivered', delivery_date=%s
        WHERE beneficiary_id=%s
    """, (delivery_date, beneficiary_id))
    conn.commit()
    conn.close()

    # Event-based: Automatically trigger notification
    send_voice_call(beneficiary_id, "PENSION_DELIVERED")

    return jsonify({"message": "Pension marked as delivered"})

@pension_bp.route("/schedule", methods=["POST"])
def set_schedule():
    data = request.json
    day = data["delivery_day"]

    # (store this in DB / config – simplified here)
    return jsonify({"message": f"Pension scheduled on {day}st"})
