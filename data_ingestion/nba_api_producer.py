import requests
import json
from datetime import datetime

# Replace with your actual RapidAPI credentials
API_URL = "https://api-nba-v1.p.rapidapi.com/games"
API_HEADERS = {
    'x-rapidapi-key': "f9bf19e726msh44f2985426204aep1d9c49jsn34da4309cf5b",  # <-- Add your API key here
    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

def fetch_today_games():
    today = datetime.now().strftime("%Y-%m-%d")
    params = {
    "date": "2025-03-21",  # Example date where games definitely occurred
    "league": "standard",
    "season": "2024"
}

    response = requests.get(API_URL, headers=API_HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Pretty print the result

        # Save sample JSON for reference
        with open("sample_nba_games.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Sample data saved to sample_nba_games.json")

    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_today_games()
