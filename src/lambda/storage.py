import boto3
from decimal import Decimal
from datetime import datetime

dynamodb = boto3.resource("dynamodb")

def store_daily_cost(table_name: str, date: str, total_cost: float, breakdown: dict):
    table = dynamodb.Table(table_name)

    table.put_item(
        Item={
            "date": date,
            "total_cost": Decimal(str(total_cost)),
            "service_breakdown": {
                k: Decimal(str(v)) for k, v in breakdown.items()
            },
            "created_at": datetime.utcnow().isoformat()
        }
    )
