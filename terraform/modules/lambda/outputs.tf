output "lambda_name" {
  description = "Lambda function name"
  value       = aws_lambda_function.cost_analyzer.function_name
}
