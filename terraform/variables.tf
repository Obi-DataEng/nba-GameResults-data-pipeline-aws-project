variable "aws_region" {
  description = "The AWS region to deploy resources in."
  type        = string
  default     = "us-east-1"
}

variable "kinesis_stream_name" {
  description = "The name of the Kinesis stream."
  type        = string
  default     = "nba-game-stream"
}

variable "kinesis_shard_count" {
  description = "Number of shards for the Kinesis stream."
  type        = number
  default     = 4
}

variable "s3_bucket_name" {
  description = "The name of the S3 bucket for storing NBA game data."
  type        = string
  default     = "nba-kinesis-consumer-bucket-ookon-2025"
}

variable "lambda_function_name" {
  description = "The name of the Lambda function."
  type        = string
  default     = "nbaDataToS3Notifier"
}

variable "ses_email_from" {
  description = "Verified SES email address to send from."
  type        = string
}

variable "ses_email_to" {
  description = "Email address to send notifications to."
  type        = string
}

variable "api_key" {
  description = "API Key for accessing the NBA API."
  type        = string
}
