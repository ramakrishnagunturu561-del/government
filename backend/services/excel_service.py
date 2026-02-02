import pandas as pd
from database import get_db_connection

def upload_excel(file_path):
    df = pd.read_excel(file_path)
    conn = get_db_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO beneficiaries
            (name, mobile_number, scheme_name, amount, delivery_mode, delivery_date, status, updated_by)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    conn.commit()
    conn.close()
