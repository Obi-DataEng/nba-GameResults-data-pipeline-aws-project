import boto3
import json

# Initialize Kinesis client (using the region where your stream is)
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def push_to_kinesis(stream_name, data):
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey="nba"
    )
    print(f"Pushed record to Kinesis with sequence number: {response['SequenceNumber']}")

if __name__ == "__main__":
    # Load your previously saved JSON file
    with open("sample_nba_games.json", "r") as f:
        game_data = json.load(f)

    stream_name = 'nba-live-data-stream'  # Make sure this matches your AWS stream name

    # Stream each game as a separate record
    for game in game_data["response"]:
        push_to_kinesis(stream_name, game)
