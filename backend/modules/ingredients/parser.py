import re


def parse_ingredients(
    text: str | None,
):

    if not text:

        return []

    cleaned = (
        text.lower()
        .replace("[", "")
        .replace("]", "")
    )

    parts = re.split(
        r"[;,()]",
        cleaned,
    )

    ingredients = []

    for item in parts:

        value = (
            item.strip()
        )

        if len(value) > 2:

            ingredients.append(
                value
            )

    return list(
        dict.fromkeys(
            ingredients
        )
    )