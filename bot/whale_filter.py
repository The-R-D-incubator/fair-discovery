import csv

def filter_high_stakes():
    print("💎 WHALE_FILTER: Identifying high-value targets...")
    leads = []
    try:
        with open('bot/leads/daily_hitlist.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Logic: If they are on X and have "Ads" or "Business" in their issue, they are a Whale
                if row['stake'] == 'High' or 'Ad' in row['issue']:
                    leads.append(row)
        
        with open('bot/leads/priority_whales.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["user", "platform", "issue", "stake"])
            writer.writeheader()
            writer.writerows(leads)
        print(f"✅ WHALE_FILTER: {len(leads)} high-value targets locked.")
    except FileNotFoundError:
        print("⚠️ No leads found yet. Waiting for Scout.")

if __name__ == "__main__":
    filter_high_stakes()
