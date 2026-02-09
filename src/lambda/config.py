import os

MODE = os.getenv("MODE", "test")
DAYS_BACK = int(os.getenv("DAYS_BACK", "7"))
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")

# Anomaly detection config
ANOMALY_MULTIPLIER = float(os.getenv("ANOMALY_MULTIPLIER", "1.5"))
BASELINE_DAYS = int(os.getenv("BASELINE_DAYS", "7"))

AI_ENABLED = os.getenv("AI_ENABLED", "false").lower() == "true"
AI_PROVIDER = os.getenv("AI_PROVIDER", "mock")

TEST_SPIKE_MULTIPLIER = float(os.getenv("TEST_SPIKE_MULTIPLIER", "2"))

