from flask import Flask, send_file
from flask_cors import CORS
from routes.beneficiaries import beneficiaries_bp
from routes.pension import pension_bp
from routes.notifications import notifications_bp
from routes.webhook import webhook_bp
from services.scheduler_service import start_scheduler

app = Flask(__name__)
CORS(app)

app.register_blueprint(beneficiaries_bp, url_prefix="/api/beneficiaries")
app.register_blueprint(pension_bp, url_prefix="/api/pension")
app.register_blueprint(notifications_bp, url_prefix="/api/notify")
app.register_blueprint(webhook_bp, url_prefix="/webhook")

@app.route("/")
def home():
    return {"status": "Welfare Notification System Running"}

@app.route("/ivr/pension.xml")
def pension_ivr():
    return send_file("ivr/pension.xml", mimetype="text/xml")

# Start the scheduler
start_scheduler()

if __name__ == "__main__":
    app.run(debug=True)
