import requests
import json
from datetime import datetime

# Replace this with your actual RapidAPI credentials
API_URL = "https://api-nba-v1.p.rapidapi.com/games"
API_HEADERS = {
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",  # <-- Add your API key here
    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

def fetch_today_games():
    today = datetime.now().strftime("%Y-%m-%d")
    params = {
        "date": today,
        "league": "standard",
        "season": "2023"  # You can adjust this for the current season
    }

    response = requests.get(API_URL, headers=API_HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Pretty-print the result

        # Save sample JSON for reference
        with open("sample_nba_games.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Sample data saved to sample_nba_games.json")

    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_today_games()
