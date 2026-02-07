output "lambda_role_arn" {
  description = "IAM Role ARN for Lambda"
  value       = aws_iam_role.lambda_role.arn
}
