HIGH = {
    "sugar",
    "sucre",
    "high fructose",
    "palm oil",
    "huile de palme",
}

MEDIUM = {
    "lecithin",
    "lecithines",
    "vanillin",
    "vanilline",
}


def score(
    ingredient: str,
):

    value = (
        ingredient.lower()
    )

    for x in HIGH:

        if x in value:

            return (
                "high",
                "Reduce intake",
            )

    for x in MEDIUM:

        if x in value:

            return (
                "medium",
                "Consume moderately",
            )

    return (
        "low",
        "Generally acceptable",
    )