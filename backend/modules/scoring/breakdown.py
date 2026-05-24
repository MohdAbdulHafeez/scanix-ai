def build(
    nutrition_score,
    processing_level,
    ingredients,
):

    breakdown = {}

    nutrition_map = {

        "a": 0,
        "b": -10,
        "c": -25,
        "d": -40,
        "e": -55,
    }

    grade = (
        (
            nutrition_score
            or ""
        )
        .lower()
    )

    breakdown[
        "nutrition_grade"
    ] = (
        nutrition_map.get(
            grade,
            -20,
        )
    )

    breakdown[
        "processing"
    ] = -(
        (
            processing_level
            or 0
        )
        * 5
    )

    ingredient_penalty = 0

    for item in ingredients:

        risk = (
            item.get(
                "risk"
            )
        )

        if risk == "high":

            ingredient_penalty -= 10

        elif risk == "medium":

            ingredient_penalty -= 5

    breakdown[
        "ingredient_risk"
    ] = (
        ingredient_penalty
    )

    breakdown[
        "final_score"
    ] = max(
        0,
        100
        + sum(
            breakdown.values()
        )
    )

    return breakdown