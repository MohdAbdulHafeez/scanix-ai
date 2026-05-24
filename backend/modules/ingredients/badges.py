def build(
    confidence,
):

    badges = [

        "AI Verified",

        "Ingredient Checked",
    ]

    if (
        confidence
        >= 85
    ):

        badges.append(
            "High Confidence"
        )

    return badges