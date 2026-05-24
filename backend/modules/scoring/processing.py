def describe(
    level,
):

    labels = {

        1: (
            "Minimally Processed"
        ),

        2: (
            "Processed"
        ),

        3: (
            "Highly Processed"
        ),

        4: (
            "Ultra Processed"
        ),
    }

    return {

        "level": level,

        "label": (
            labels.get(
                level,
                "Unknown",
            )
        ),
    }