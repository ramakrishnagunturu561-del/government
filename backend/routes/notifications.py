from flask import Blueprint, jsonify
from database import get_db_connection

notifications_bp = Blueprint("notifications", __name__)

@notifications_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Notification service active"})

@notifications_bp.route("/logs", methods=["GET"])
def get_logs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM call_logs")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)
