def suggest(
    score,
    nutrition_score,
    processing_level,
):

    items = []

    if score <= 25:

        items.extend(

            [

                {
                    "title":
                    "Choose lower sugar version",

                    "reason":
                    "High sugar detected",
                },

                {
                    "title":
                    "Prefer minimally processed option",

                    "reason":
                    "Processing too high",
                },

                {
                    "title":
                    "Reduce serving size",

                    "reason":
                    "Overall nutrition poor",
                },

            ]

        )

    elif score <= 60:

        items.extend(

            [

                {
                    "title":
                    "Prefer protein-rich alternative",

                    "reason":
                    "Improve balance",
                },

                {
                    "title":
                    "Choose lower calorie variant",

                    "reason":
                    "Moderate quality",
                },

            ]

        )

    else:

        items.append(

            {

                "title":
                "Current option looks acceptable",

                "reason":
                "Good overall profile",

            }

        )

    if (
        nutrition_score
        and str(
            nutrition_score
        ).lower()
        == "e"
    ):

        items.append(

            {

                "title":
                "Improve nutrition grade",

                "reason":
                "Current nutrition grade low",

            }

        )

    if (
        processing_level
        and processing_level >= 4
    ):

        items.append(

            {

                "title":
                "Choose less processed product",

                "reason":
                "Ultra processed",

            }

        )

    return items[:5]