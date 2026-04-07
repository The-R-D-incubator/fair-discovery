import json
import datetime
import requests

def check_for_holidays():
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Using a free public API to check for global holidays
    # Countries to monitor: US, UK, India, Brazil, China
    countries = ['US', 'GB', 'IN', 'BR', 'CN']
    active_holiday = "None"
    reason = "Standard Operations"
    multiplier = 1
    confetti = False

    for country in countries:
        try:
            response = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/2026/{country}")
            holidays = response.json()
            for h in holidays:
                if h['date'] == today:
                    active_holiday = h['name']
                    reason = f"Global Celebration in {country}"
                    multiplier = 2  # Double the credits
                    confetti = True
                    break
            if active_holiday != "None": break
        except:
            continue

    # Create the promo data
    promo_data = {
        "active_holiday": active_holiday,
        "reason": reason,
        "multiplier": multiplier,
        "confetti": confetti,
        "last_update": today
    }

    # Write to the global config
    with open('global_promo.json', 'w') as f:
        json.dump(promo_data, f, indent=2)
    
    print(f"Sync Complete: Today is {active_holiday}")

if __name__ == "__main__":
    check_for_holidays()
