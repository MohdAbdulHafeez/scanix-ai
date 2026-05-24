from modules.ingredients.verifier import (
    verify,
)

from modules.ingredients.ingredient_verifier import (
    verify_claims,
)


def evaluate(
    ingredients,
    ingredients_text,
):

    parsed = (
        verify(
            ingredients_text
        )
    )

    return (
        verify_claims(
            parsed
        )
    )