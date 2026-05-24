def compute(
    ingredients,
    allergens,
):

    score = 50

    score += min(
        len(
            ingredients
        )
        * 5,
        30,
    )

    score += min(
        len(
            allergens
        )
        * 3,
        15,
    )

    score = min(
        score,
        100,
    )

    label = (
        "high confidence"
        if score >= 85
        else (
            "medium confidence"
            if score >= 65
            else "low confidence"
        )
    )

    return {
        "score": score,
        "label": label,
    }