resource "aws_dynamodb_table" "cost_table" {
  name         = "${var.project_name}-cost-history"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "date"

  attribute {
    name = "date"
    type = "S"
  }

  tags = {
    Name        = var.project_name
    Environment = var.environment
  }
}
