def risk_level(
    score: int,
):

    if score >= 80:
        return "excellent"

    if score >= 60:
        return "good"

    if score >= 40:
        return "moderate"

    return "poor"