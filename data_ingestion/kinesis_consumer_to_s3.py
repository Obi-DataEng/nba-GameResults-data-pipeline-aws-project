import boto3
import json
import time
import os
from datetime import datetime

kinesis_client = boto3.client('kinesis')
s3_client = boto3.client('s3')

stream_name = 'nba-live-data-stream'
s3_bucket = 'nba-kinesis-consumer-bucket-ookon-2025'

def get_all_shards(stream_name):
    response = kinesis_client.describe_stream(StreamName=stream_name)
    return response['StreamDescription']['Shards']

def consume_from_shard(shard_id, stream_name):
    records = []
    shard_iterator = kinesis_client.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='LATEST'  # Start fresh and only read new records
    )['ShardIterator']

    while True:
        response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=100)
        shard_iterator = response['NextShardIterator']

        if response['Records']:
            for record in response['Records']:
                payload = json.loads(record['Data'])
                records.append(payload)
        else:
            break

        time.sleep(1)  # slight delay to avoid throttling
    return records

def write_records_to_s3(records):
    if records:
        # Deduplicate by game_id
        unique_records = {rec['id']: rec for rec in records}
        unique_records_list = list(unique_records.values())

        timestamp = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'nba_games_{timestamp}.json'

        with open(file_name, 'w') as f:
            json.dump(unique_records_list, f, indent=4)

        s3_client.upload_file(file_name, s3_bucket, file_name)
        os.remove(file_name)
        print(f'✅ Written {len(unique_records_list)} unique records to {file_name} in {s3_bucket}')
    else:
        print('✅ No new records to write.')

if __name__ == "__main__":
    print("Starting consumer and waiting for new records...")

    try:
        while True:
            all_records = []
            shards = get_all_shards(stream_name)
            for shard in shards:
                shard_id = shard['ShardId']
                print(f"Consuming from shard: {shard_id}")
                shard_records = consume_from_shard(shard_id, stream_name)
                all_records.extend(shard_records)

            write_records_to_s3(all_records)
            print("Waiting 15 seconds before checking again...")
            time.sleep(15)

    except KeyboardInterrupt:
        print("Stopped continuous consumer.")
