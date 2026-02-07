from config import MODE, DAYS_BACK, DYNAMODB_TABLE
from cost_explorer import get_cost_data
from storage import store_daily_cost


def lambda_handler(event, context):
    print(f"Cost Anomaly Finder running in {MODE} mode")

    results = get_cost_data(DAYS_BACK)

    if not results:
        print("Cost Explorer returned no results")
        return {
            "status": "no_data",
            "message": "No cost data returned from Cost Explorer"
        }

    # Find the most recent day with cost data
    latest_day = None
    for day in reversed(results):
        if day.get("Groups"):
            latest_day = day
            break

    if not latest_day:
        print("No cost data available yet for any day")
        return {
            "status": "no_data",
            "message": "Cost Explorer returned empty cost groups"
        }

    date = latest_day["TimePeriod"]["Start"]

    total_cost = 0.0
    breakdown = {}

    for group in latest_day["Groups"]:
        service = group["Keys"][0]
        amount = float(group["Metrics"]["UnblendedCost"]["Amount"])

        breakdown[service] = amount
        total_cost += amount

    # 🔧 Inject artificial spike
