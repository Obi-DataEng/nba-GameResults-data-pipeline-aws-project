🚀 Tech Stack

AWS Kinesis (Data Streaming)

AWS S3 (Storage)

AWS Lambda (Orchestration + Email Trigger)

AWS SES (Email Service)

Python 3.12

requests, boto3 libraries

Terraform (Infrastructure as Code)

🛠 AWS Setup

Kinesis Stream: nba-game-stream with 4 shards.

S3 Bucket: nba-kinesis-consumer-bucket-ookon-2025.

Lambda Environment Variables:

API_KEY: Your NBA API Key

BUCKET_NAME: Your S3 bucket name

SES_EMAIL_FROM: Verified SES sender email

SES_EMAIL_TO: Recipient email

⚙️ How to Run

1. Run Producer

cd data_ingestion
python nba_api_producer.py

2. Run Consumer

python kinesis_consumer_to_s3.py

3. Trigger Lambda (Manually or on schedule)

Upload zipped Lambda function package.

Test from AWS Lambda console or set up CloudWatch Event trigger.

📧 Email Format

Subject: NBA Game Summaries for Yesterday

Game summaries with scores and ESPN Recap links.

Direct link to download the JSON from S3.

✅ Features

Real-time data ingestion.

Batch consumption from multiple shards.

JSON file storage with timestamp naming.

Automated SES emails with scores and recaps.

ESPN recap links generated dynamically.
