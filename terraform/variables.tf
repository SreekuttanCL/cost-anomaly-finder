variable "aws_region" {
  description = "AWS REgion"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "cost-anomaly-finder"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}
