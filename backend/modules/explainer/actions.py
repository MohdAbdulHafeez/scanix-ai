def recommend(
    score,
):

    if score <= 25:

        return [

            "Consume occasionally",

            "Reduce portion",

            "Prefer lower sugar alternatives",
        ]

    if score <= 60:

        return [

            "Moderate consumption",

            "Pair with protein",
        ]

    return [

        "Suitable for regular intake",
    ]