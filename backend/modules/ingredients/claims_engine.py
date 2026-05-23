from modules.ingredients.health_claims import (
    default_claims,
)

from modules.ingredients.verifier import (
    verify,
)


def evaluate(
    ingredients,
    ingredients_text,
):

    claims = (
        default_claims()
    )

    parsed = (
        verify(
            ingredients_text
        )
    )

    positives = []

    negatives = []

    for claim in claims:

        lower = (
            claim.lower()
        )

        failed = False

        for item in parsed:

            value = (
                item[
                    "name"
                ].lower()
            )

            if (
                lower == "no palm oil"
                and "palm"
                in value
            ):
                failed = True

            if (
                lower == "no added sugar"
                and (
                    "sugar"
                    in value
                    or "sucre"
                    in value
                )
            ):
                failed = True

        target = (
            negatives
            if failed
            else positives
        )

        target.append(
            {
                "claim": claim,
                "verdict": (
                    "FAIL"
                    if failed
                    else "PASS"
                ),
            }
        )

    return {

        "positives": positives,

        "negatives": negatives,

        "all": (
            positives
            + negatives
        ),
    }