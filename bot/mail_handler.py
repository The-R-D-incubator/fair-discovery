import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/forge-request', methods=['POST'])
def handle_request():
    data = request.form
    email = data.get('email')
    message = data.get('message')

    # --- SMTP CONFIGURATION ---
    sender = "bot@fairdiscovery.org"
    receiver = "jarrit@forgevertical.com"
    
    msg = MIMEText(f"NEW CUSTOM FORGE REQUEST\n\nFrom: {email}\n\nDetails: {message}")
    msg['Subject'] = "🛠️ CUSTOM FORGE INCOMING"
    msg['From'] = sender
    msg['To'] = receiver

    try:
        # Update with your mail server details (Gmail, Outlook, or Private)
        with smtplib.SMTP("smtp.yourserver.com", 587) as server:
            server.starttls()
            server.login("your_user", "your_password")
            server.sendmail(sender, receiver, msg.as_string())
        return jsonify({"status": "Success"}), 200
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
