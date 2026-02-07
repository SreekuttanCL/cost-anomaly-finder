output "topic_arn" {
  description = "SNS Topic arn"
  value       = aws_sns_topic.alerts.arn
}
