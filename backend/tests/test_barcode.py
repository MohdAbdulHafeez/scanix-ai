from modules.ingredients.verifier import (
    verify,
)


def test_verify():

    result = verify(
        "Sugar, Palm Oil"
    )

    assert (
        len(
            result
        )
        > 0
    )