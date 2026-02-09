def calculate_baseline(costs: list[float]) -> float:
    """
    Calculate average baseline cost.
    """
    if not costs:
        return 0.0

    return sum(costs) / len(costs)


def is_anomalous(current_cost: float, baseline: float, multiplier: float) -> bool:
    """
    Determine if current cost exceeds baseline threshold.
    """
    if baseline == 0:
        return False

    return current_cost > (baseline * multiplier)
