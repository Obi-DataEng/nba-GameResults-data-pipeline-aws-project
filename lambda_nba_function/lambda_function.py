import boto3
import os
import json
import datetime
import requests

s3_client = boto3.client('s3')
ses_client = boto3.client('ses', region_name='us-east-1')

api_key = os.environ['API_KEY']
s3_bucket_name = os.environ['BUCKET_NAME']
sender_email = os.environ['SES_EMAIL_FROM']
receiver_email = os.environ['SES_EMAIL_TO']

headers = {"Authorization": api_key}

def fetch_nba_games():
    today = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    url = f"https://api.balldontlie.io/v1/games?start_date={today}&end_date={today}&per_page=100"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['data']

def generate_google_search_link(game):
    home = game['home_team']['full_name'].replace(' ', '+')
    visitor = game['visitor_team']['full_name'].replace(' ', '+')
    date = datetime.datetime.strptime(game['date'][:10], '%Y-%m-%d').strftime('%B+%d+%Y')
    return f"https://www.google.com/search?q={visitor}+vs+{home}+{date}+NBA+recap"

def upload_to_s3(data):
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"nba_games_{timestamp}.json"
    s3_client.put_object(
        Bucket=s3_bucket_name,
        Key=filename,
        Body=json.dumps(data)
    )
    return filename

def send_email(subject, body):
    try:
        response = ses_client.send_email(
            Source=sender_email,
            Destination={'ToAddresses': [receiver_email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Html': {'Data': body}}
            }
        )
        print(f"Email sent! Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"Error sending email: {e}")

def lambda_handler(event, context):
    print("Fetching NBA games...")
    games = fetch_nba_games()

    if not games:
        print("No games found.")
        return {"statusCode": 200, "body": "No NBA games found yesterday."}

    file_name = upload_to_s3(games)

    email_body = f"<h2>NBA Game Summaries for Yesterday</h2>"
    for game in games:
        home_team = game['home_team']['full_name']
        visitor_team = game['visitor_team']['full_name']
        home_score = game['home_team_score']
        visitor_score = game['visitor_team_score']
        google_link = generate_google_search_link(game)

        email_body += f"<p><strong>{visitor_team} vs. {home_team}</strong> — {visitor_score} - {home_score}<br>"
        email_body += f"<a href='{google_link}'>Read Recap</a></p>"

    s3_link = f"https://s3.amazonaws.com/{s3_bucket_name}/{file_name}"
    email_body += f"<p>📥 <a href='{s3_link}'>Download Full Game JSON Data</a></p>"

    send_email("Daily NBA Games Recap and Data File", email_body)

    return {"statusCode": 200, "body": f"Successfully stored {len(games)} games to S3 and sent email."}
