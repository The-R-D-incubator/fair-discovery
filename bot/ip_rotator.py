import requests
import random

def get_fresh_proxies():
    print("📡 ROTATOR: Harvesting fresh IP masks...")
    # Scaping free, high-speed SSL proxy lists
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=elite"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            proxy_list = response.text.split('\r\n')
            # Filter out empty strings
            return [p for p in proxy_list if p]
    except:
        return []

def get_random_mask():
    proxies = get_fresh_proxies()
    if proxies:
        selected = random.choice(proxies)
        print(f"🎭 MASK_ACTIVE: {selected}")
        return {"http": f"http://{selected}", "https": f"http://{selected}"}
    else:
        print("⚠️ ROTATOR: No external proxies found. Defaulting to GitHub Cloud IP.")
        return None

if __name__ == "__main__":
    mask = get_random_mask()
