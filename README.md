<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NBA Data Engineering Pipeline Project</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Roboto', sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        header { background: #24292e; color: white; padding: 20px; text-align: center; }
        section { padding: 40px; max-width: 900px; margin: auto; background: white; margin-top: 20px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        h1, h2 { color: #333; }
        a { color: #0366d6; text-decoration: none; }
        a:hover { text-decoration: underline; }
        footer { text-align: center; padding: 20px; color: #777; }
    </style>
</head>
<body>

<header>
    <h1>NBA Data Engineering Pipeline Project</h1>
    <p>By Obinna Okonkwo</p>
</header>

<section>
    <h2>📚 Overview</h2>
    <p>This end-to-end pipeline ingests daily NBA game data from <a href="https://www.balldontlie.io" target="_blank">balldontlie.io</a>, streams it to AWS Kinesis, stores it in S3, and sends daily summaries with ESPN links via email.</p>

    <h2>🔗 Architecture Diagram</h2>
    <img src="https://user-images.githubusercontent.com/your-diagram-link-here.png" alt="Architecture Diagram" width="100%">

    <h2>🚀 Tech Stack</h2>
    <ul>
        <li>AWS Kinesis, S3, Lambda, SES</li>
        <li>Python 3.12 (Requests, Boto3)</li>
        <li>Terraform for infrastructure</li>
    </ul>

    <h2>📂 Key Features</h2>
    <ul>
        <li>Automated daily NBA game ingestion</li>
        <li>Real-time Kinesis streaming</li>
        <li>Storage to timestamped S3 JSON files</li>
        <li>Dynamic ESPN recap links in email notifications</li>
        <li>Fully deployed with Terraform</li>
    </ul>

    <h2>📧 Example Email Output</h2>
    <img src="https://user-images.githubusercontent.com/your-email-screenshot-link.png" alt="Email Example" width="100%">

    <h2>📁 <a href="https://github.com/YourUsername/nba-data-pipeline" target="_blank">View the full code on GitHub</a></h2>

</section>

<footer>
    <p>Made with ❤️ by Obinna Okonkwo</p>
</footer>

</body>
</html>
