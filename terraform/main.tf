# main.tf
provider "aws" {
  region = var.aws_region
}

resource "aws_kinesis_stream" "nba_stream" {
  name             = var.kinesis_stream_name
  shard_count      = 4
  retention_period = 24
  shard_level_metrics = ["IncomingBytes", "OutgoingBytes"]
}

resource "aws_s3_bucket" "nba_bucket" {
  bucket = var.s3_bucket_name
  force_destroy = true
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "lambda_s3_full_access" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

resource "aws_iam_role_policy_attachment" "lambda_kinesis_full_access" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonKinesisFullAccess"
}

resource "aws_iam_role_policy_attachment" "lambda_ses_send_email" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSESFullAccess"
}

resource "aws_lambda_function" "nba_lambda" {
  function_name = var.lambda_function_name
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.12"
  handler       = "lambda_function.lambda_handler"
  filename      = var.lambda_zip_file
  timeout       = 10

  environment {
    variables = {
      API_KEY        = var.nba_api_key
      BUCKET_NAME    = var.s3_bucket_name
      SES_EMAIL_FROM = var.ses_email_from
      SES_EMAIL_TO   = var.ses_email_to
    }
  }
}

# Optionally add CloudWatch trigger, SES verification, or schedule later if needed.
