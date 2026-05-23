from modules.scoring.scanix_score import (
    compute,
)


def test_score():

    result = compute(
        "e",
        4,
    )

    assert (
        result[
            "scanix_score"
        ]
        >= 0
    )