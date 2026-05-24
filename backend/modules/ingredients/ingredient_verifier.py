CLAIMS = {

    "No Palm Oil": {
        "keywords": [
            "palm",
            "huile de palme",
        ],
        "icon": "🌴",
    },

    "No Added Sugar": {
        "keywords": [
            "sugar",
            "sucre",
            "syrup",
        ],
        "icon": "🍬",
    },

    "Dairy Free": {
        "keywords": [
            "milk",
            "lait",
            "whey",
            "cheese",
        ],
        "icon": "🥛",
    },

    "Gluten Free": {
        "keywords": [
            "wheat",
            "gluten",
        ],
        "icon": "🌾",
        "invert": True,
    },

    "No Nuts": {
        "keywords": [
            "nut",
            "hazelnut",
            "noisette",
        ],
        "icon": "🥜",
    },

}


def verify_claims(
    ingredients,
):

    text = (
        " ".join(

            [
                x[
                    "name"
                ]

                for x

                in ingredients
            ]

        )
    ).lower()

    positives = []

    negatives = []

    for claim, rule in CLAIMS.items():

        found = any(

            k in text

            for k

            in rule[
                "keywords"
            ]

        )

        invert = (
            rule.get(
                "invert",
                False,
            )
        )

        passed = (
            not found
            if not invert
            else found
        )

        item = {

            "claim": claim,

            "icon": (
                rule[
                    "icon"
                ]
            ),

            "status": (
                "PASS"
                if passed
                else "FAIL"
            ),

        }

        if passed:

            positives.append(
                item
            )

        else:

            negatives.append(
                item
            )

    return {

        "positives": positives,

        "negatives": negatives,
    }