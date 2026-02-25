# FAIR DISCOVERY INSTALLATION GUIDE 🚀

Follow these steps to protect your ad budget and monitor human engagement.

### 1. CONFIGURATION
Open 'js/engagement.js' and edit the CONFIG section:
- COMPANY_NAME: Put your brand name here.
- PIXELS: Paste your IDs for Facebook, Google, LinkedIn, and TikTok.

### 2. PRIVACY
Open 'index.html' and look for 'ACCESS_CODE'. Change "1234" to your own private password. [cite: 6, 9]

### 3. DATA SETUP
Open 'discovery.json' and update:
- "site": Your URL
- "whatsapp": Your contact number for the directory. [cite: 9]

### 4. INSTALLATION
1. Upload this entire folder to your server via cPanel. [cite: 5, 6]
2. Add this line to your website's footer (before </body>):
   <script src="/fair-discovery/js/engagement.js"></script> 

### 5. SECURITY (Honeypot)
The system automatically creates an invisible 'honeypot' field. If a bot fills it, all tracking is disabled immediately for that session.
