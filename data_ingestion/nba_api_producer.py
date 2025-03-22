import requests
import json
from datetime import datetime

# Replace with your actual RapidAPI credentials
conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "f9bf19e726msh44f2985426204aep1d9c49jsn34da4309cf5b",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
}

def fetch_today_games():
    today = datetime.now().strftime("%Y-%m-%d")
    params = {
        "date": today,
        "league": "standard",
        "season": "2023"  # or adjust based on current season year
    }

    response = requests.get(API_URL, headers=API_HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Pretty print results

        with open("sample_nba_games.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved to sample_nba_games.json")

    else:
        print(f"API call failed with status: {response.status_code}, reason: {response.text}")

if __name__ == "__main__":
    fetch_today_games()
