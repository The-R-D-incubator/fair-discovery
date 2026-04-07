import requests
import random

def get_fresh_proxies():
    # Scaping elite SSL proxies
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=elite"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return [p for p in response.text.split('\r\n') if p]
    except:
        return []

def get_random_mask():
    print("📡 ROTATOR: Harvesting fresh IP masks...")
    proxies = get_fresh_proxies()
    
    if not proxies:
        print("⚠️ ROTATOR: No external proxies found. Defaulting to GitHub Cloud IP.")
        return None

    # Try up to 5 proxies to find one that is actually alive
    for _ in range(5):
        selected = random.choice(proxies)
        proxy_dict = {"http": f"http://{selected}", "https": f"http://{selected}"}
        
        try:
            # Quick 3-second ping to verify the proxy isn't a "ghost"
            requests.get("https://google.com", proxies=proxy_dict, timeout=3)
            print(f"🎭 MASK_VERIFIED: {selected}")
            return proxy_dict
        except:
            print(f"♻️ ROTATOR: {selected} failed validation. Retrying...")
            proxies.remove(selected)
            continue

    print("⚠️ ROTATOR: All harvested proxies failed. Reverting to GitHub IP.")
    return None

if __name__ == "__main__":
    get_random_mask()
