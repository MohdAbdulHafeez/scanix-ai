def health_score(
    nutrition_score: str | None,
    processing_level: int | None,
):

    score = 100

    mapping = {
        "a": 0,
        "b": 10,
        "c": 25,
        "d": 40,
        "e": 55,
    }

    score -= (
        mapping.get(
            (
                nutrition_score
                or ""
            ).lower(),
            20,
        )
    )

    if processing_level:

        score -= (
            processing_level
            * 5
        )

    return max(
        0,
        min(
            score,
            100,
        ),
    )