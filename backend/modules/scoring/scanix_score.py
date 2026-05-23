from modules.scoring.health_score import (
    health_score,
)

from modules.scoring.nutrition_score import (
    risk_level,
)


def compute(
    nutrition_score,
    processing_level,
):

    score = health_score(
        nutrition_score,
        processing_level,
    )

    return {
        "scanix_score": score,
        "risk_level": (
            risk_level(
                score
            )
        ),
    }