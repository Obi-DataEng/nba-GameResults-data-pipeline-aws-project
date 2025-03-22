import boto3
import json
from datetime import datetime

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def push_to_kinesis(stream_name, data):
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey="nba"
    )
    print(f"Pushed to Kinesis: {response}")

if __name__ == "__main__":
    # Load the JSON data you already saved
    with open("sample_nba_games.json", "r") as f:
        game_data = json.load(f)
    
    stream_name = 'nba-live-data-stream'  # Make sure this matches what you named it on AWS

    # Send the entire JSON to Kinesis (or loop through responses to stream each game individually)
    for game in game_data["response"]:
        push_to_kinesis(stream_name, game)
