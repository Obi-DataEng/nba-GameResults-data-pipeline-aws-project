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
