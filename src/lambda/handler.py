from config import (
    MODE,
    DAYS_BACK,
    DYNAMODB_TABLE,
    ANOMALY_MULTIPLIER,
    BASELINE_DAYS,
    TEST_SPIKE_MULTIPLIER
)
from cost_explorer import get_cost_data
from storage import store_daily_cost, get_recent_costs
from anomaly_detector import calculate_baseline, is_anomalous
from ai_explainer import generate_explanation
from config import AI_ENABLED


def lambda_handler(event, context):
    print(f"Cost Anomaly Finder running in {MODE} mode")

    results = get_cost_data(DAYS_BACK)

    if not results:
        return {"status": "no_data"}

    # Find latest day with cost data
    latest_day = None
    for day in reversed(results):
        if day.get("Groups"):
            latest_day = day
            break

    if not latest_day:
        return {"status": "no_data"}

    date = latest_day["TimePeriod"]["Start"]

    total_cost = 0.0
    breakdown = {}

    for group in latest_day["Groups"]:
        service = group["Keys"][0]
        amount = float(group["Metrics"]["UnblendedCost"]["Amount"])
        breakdown[service] = amount
        total_cost += amount

    # Test spike injection
    if MODE == "test":
        print("Injecting artificial test spike")
        total_cost *= TEST_SPIKE_MULTIPLIER
        breakdown["TEST_SPIKE"] = total_cost

    # Store today's cost
    store_daily_cost(
        table_name=DYNAMODB_TABLE,
        date=date,
        total_cost=total_cost,
        breakdown=breakdown
    )

    # Fetch baseline data
    recent_costs = get_recent_costs(
        table_name=DYNAMODB_TABLE,
        days=BASELINE_DAYS
    )

    baseline_costs = recent_costs[1:]
    baseline = calculate_baseline(baseline_costs)   
    #baseline = calculate_baseline(recent_costs)
    anomalous = is_anomalous(total_cost, baseline, ANOMALY_MULTIPLIER)

    print(f"Baseline: {baseline}, Current: {total_cost}, Anomalous: {anomalous}")

    explanation = None

    if anomalous and AI_ENABLED:
        explanation = generate_explanation(
            date=date,
            total_cost=total_cost,
            baseline=baseline,
            breakdown=breakdown
        )

    return {
        "status": "success",
        "date": date,
        "total_cost": round(total_cost, 2),
        "baseline": round(baseline, 2),
        "anomalous": anomalous,
        "explanation": explanation
    }

