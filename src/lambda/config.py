import os

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
MODE = os.getenv("MODE", "test")  # test | prod

DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE", "cost-anomaly-finder-cost-history")

DAYS_BACK = int(os.getenv("DAYS_BACK", "14"))
