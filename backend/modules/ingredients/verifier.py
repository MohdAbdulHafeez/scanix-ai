from modules.ingredients.parser import (
    parse_ingredients,
)

from modules.ingredients.risk_engine import (
    score,
)


def verify(
    text: str,
):

    result = []

    parsed = (
        parse_ingredients(
            text
        )
    )

    for item in parsed:

        risk, explanation = (
            score(
                item
            )
        )

        result.append(
            {
                "name": item,
                "risk": risk,
                "explanation": explanation,
            }
        )

    return result