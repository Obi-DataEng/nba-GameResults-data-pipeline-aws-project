import boto3
import requests
import json
import datetime
import time
import os

# AWS Kinesis setup
kinesis_client = boto3.client('kinesis', region_name='us-east-1')
stream_name = ''  # make sure this matches your Kinesis stream name

# Your BallDontLie API key
API_KEY = 'API Key'
API_URL = 'https://api.balldontlie.io/v1/games'

# Function to fetch yesterday's games
def get_yesterdays_games():
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    print(f"Fetching games for {yesterday}...")
    params = {
        'start_date': yesterday,
        'end_date': yesterday,
        'per_page': 100
    }
    headers = {'Authorization': API_KEY}

    try:
        response = requests.get(API_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"Other error occurred: {err}")
        return []

# Function to send data to Kinesis
def send_to_kinesis(game_data):
    for game in game_data:
        json_data = json.dumps(game)
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json_data,
            PartitionKey=str(game['id'])
        )
        print(f"Sent game ID {game['id']} to Kinesis with response: {response}")

if __name__ == "__main__":
    games = get_yesterdays_games()
    if games:
        send_to_kinesis(games)
        print(f"✅ Sent {len(games)} games to Kinesis!")
    else:
        print("❌ No games found or failed to fetch.")
