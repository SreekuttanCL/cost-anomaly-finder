resource "aws_lambda_function" "cost_analyzer" {
  function_name = "${var.project_name}-analyzer"
  role          = var.lambda_role_arn
  handler       = "handler.lambda_handler"
  runtime       = "python3.11"

  filename         = "cost_analyzer.zip"
  source_code_hash = filebase64sha256("cost_analyzer.zip")

  environment {
    variables = {
      ENVIRONMENT        = var.environment
      MODE               = "test"
      DYNAMODB_TABLE     = "${var.project_name}-cost-history"
      DAYS_BACK          = "14"
      AI_ENABLED         = "false"
      ANOMALY_MULTIPLIER = "1.5"
    }
  }
}
