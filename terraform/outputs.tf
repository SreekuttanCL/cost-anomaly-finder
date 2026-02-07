output "lambda_name" {
  value = module.lambda.lambda_name
}

output "dynamodb_table" {
  value = module.dynamodb.table_name
}

output "sns_topic_arn" {
  value = module.sns.topic_arn
}
