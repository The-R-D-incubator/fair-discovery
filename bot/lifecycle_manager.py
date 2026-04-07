import json
import time

def check_army_health():
    print("🛡️ LIFECYCLE: Auditing active bot perimeter...")
    
    with open('bot/army_status.json', 'r') as f:
        army = json.load(f)

    for bot_id, status in army.items():
        # If bot hasn't reported in 4 hours, it's likely blocked
        if time.time() - status['last_heartbeat'] > 14400:
            print(f"⚠️ BOT_{bot_id} SILENT. Assuming Blocked. Initializing replacement...")
            replace_bot(bot_id)

def replace_bot(old_id):
    # Logic to trigger a new GitHub Action or local script with new credentials
    new_id = f"NODE_{int(time.time())}"
    print(f"🚀 NEW NODE DEPLOYED: {new_id}. Resuming mission.")
    # Update army_status.json with the new node
