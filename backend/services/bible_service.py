import requests

def search_verses(theme):
    response = requests.get(f"https://bible-api.com/{theme}?translation=kjv")
    if response.status_code == 200:
        data = response.json()
        if 'text' in data:
            return [{"reference": data.get("reference", "N/A"), "verse": data.get("text", "")}]
    return [{"reference": "Not found", "verse": "No verse found for this theme."}]
