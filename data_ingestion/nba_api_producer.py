import requests
import json
from datetime import datetime

# Replace this with your actual RapidAPI credentials or endpoint
conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "f9bf19e726msh44f2985426204aep1d9c49jsn34da4309cf5b",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
}

def fetch_today_games():
    today = datetime.now().strftime("%Y-%m-%d")
    params = {"date": today, "league": "standard", "season": "2024"}  # adjust season if needed

    response = requests.get(API_URL, headers=API_HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Pretty print results

        # Save sample to file for reference
        with open("sample_nba_games.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Sample data saved to sample_nba_games.json")

    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_today_games()
