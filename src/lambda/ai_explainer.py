def generate_explanation(date, total_cost, baseline, breakdown):
    """
    Mock AI explanation for cost anomaly.
    """
    top_services = sorted(
        breakdown.items(), key=lambda x: x[1], reverse=True
    )[:3]

    drivers = ", ".join(
        f"{svc} (${amt:.2f})" for svc, amt in top_services
    )

    return {
        "summary": f"Unusual increase in daily AWS spend detected on {date}.",
        "details": (
            f"Total cost ${total_cost:.2f} exceeded the baseline of "
            f"${baseline:.2f}. The main contributors were: {drivers}."
        ),
        "recommendations": [
            "Review recent infrastructure changes or deployments",
            "Check for unintentionally running resources",
            "Apply cost allocation tags for better visibility",
        ]
    }
