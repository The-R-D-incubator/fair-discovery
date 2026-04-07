import os
import firebase_admin
from firebase_admin import credentials, firestore
import sendgrid
from sendgrid.helpers.mail import Mail

# 1. Setup Firebase (Using a Secret Key from GitHub)
# We'll get this JSON key from your Firebase Settings
service_account_info = json.loads(os.environ['FIREBASE_SERVICE_ACCOUNT'])
creds = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(creds)
db = firestore.client()

# 2. Fetch Leads
leads_ref = db.collection('leads')
docs = leads_ref.stream()
email_list = [doc.to_dict()['email'] for doc in docs]

# 3. Craft the "Intel" News
newsletter_content = """
<h1>Fair Discovery // Weekly Intel Report</h1>
<p>Our bots have detected new "Sketchy Brief" patterns in the wild.</p>
<p><strong>SPECIAL OFFER:</strong> Use Sentinel-Scrub today for a 50% Credit Bonus.</p>
<a href="https://fairdiscovery.org/sentinel-scrub.html">Access Node</a>
"""

# 4. Dispatch via SendGrid
sg = sendgrid.SendGridAPIClient(api_key=os.environ['SENDGRID_API_KEY'])

for recipient in email_list:
    message = Mail(
        from_email='intel@fairdiscovery.org',
        to_emails=recipient,
        subject='[INTEL] Weekly Forensic Update',
        html_content=newsletter_content
    )
    try:
        sg.send(message)
    except Exception as e:
        print(f"Error sending to {recipient}: {e}")
