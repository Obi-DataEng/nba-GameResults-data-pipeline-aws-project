output "kinesis_stream_name" {
  description = "Name of the Kinesis stream"
  value       = aws_kinesis_stream.nba_stream.name
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.nba_data_bucket.bucket
}

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.nba_lambda.function_name
}

output "ses_email_identity" {
  description = "SES email identity used for sending emails"
  value       = aws_ses_email_identity.ses_email.id
}
