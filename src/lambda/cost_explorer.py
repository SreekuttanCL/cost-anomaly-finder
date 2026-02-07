import boto3
from datetime import datetime, timedelta

ce = boto3.client("ce")


def get_cost_data(days_back: int):
    """
    Fetch AWS cost data for the past N days, grouped by service.
    """
    end = datetime.utcnow().date()
    start = end - timedelta(days=days_back)

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start.strftime("%Y-%m-%d"),
            "End": end.strftime("%Y-%m-%d")
        },
        Granularity="DAILY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }
        ]
    )

    return response.get("ResultsByTime", [])
