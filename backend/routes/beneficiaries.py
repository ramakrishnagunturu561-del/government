from flask import Blueprint, request, jsonify
from database import get_db_connection
from services.excel_service import upload_excel
import os

beneficiaries_bp = Blueprint("beneficiaries", __name__)

@beneficiaries_bp.route("/", methods=["GET"])
def get_all_beneficiaries():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM beneficiaries")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@beneficiaries_bp.route("/upload", methods=["POST"])
def upload_beneficiaries():
    file = request.files["file"]
    path = f"../uploads/{file.filename}"
    file.save(path)
    upload_excel(path)
    return jsonify({"message": "Excel uploaded successfully"})
