# NBA Data Engineering Pipeline Project

## 📚 Overview
An end-to-end data engineering pipeline that automates daily NBA game data ingestion from the [balldontlie.io](https://www.balldontlie.io) API, streams data through AWS Kinesis, stores it in S3, and sends daily summary emails with dynamic ESPN recap links.

## 🔗 Architecture Overview
- **NBA API Producer**: Python script that fetches daily NBA game data and pushes it to AWS Kinesis.
- **Kinesis Consumer**: Consumes game data from Kinesis shards and writes it into S3 buckets in JSON format.
- **AWS Lambda (nbaDataToS3Notifier)**: Automatically retrieves game data, stores it in S3, and sends an email summary with scores, ESPN recap links, and a JSON download link.

## 🚀 Tech Stack
- AWS Kinesis
- AWS S3
- AWS Lambda
- AWS SES
- Python 3.12
- boto3, requests
- Terraform for infrastructure provisioning

## 📂 Project Structure
```
├── data_ingestion
│   ├── nba_api_producer.py
│   ├── kinesis_consumer_to_s3.py
├── lambda_nba_function
│   ├── lambda_function.py
│   ├── requests/ (dependencies)
├── terraform
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── README.md
```

## ⚙️ How to Use
### 1. Run Producer
```bash
cd data_ingestion
python nba_api_producer.py
```
### 2. Run Consumer
```bash
python kinesis_consumer_to_s3.py
```
### 3. Deploy Lambda
- Package dependencies and upload as a zip file.
- Set environment variables in AWS Lambda console.
- Trigger manually or schedule with CloudWatch Events.

## ✅ Features
- Automated daily NBA game ingestion.
- Streaming via Kinesis and storage in S3.
- Timestamped JSON storage.
- SES emails with:
  - Game scores
  - Dynamic ESPN recaps
  - JSON data download links.

## 🚀 Potential Enhancements
- Add Slack notifications.
- Visualize data in Power BI or Tableau.
- Store historical records in AWS Redshift or RDS.

## 👨🏾‍💻 Author
Obinna Okonkwo

## 📜 License
This project is licensed under the MIT License.
