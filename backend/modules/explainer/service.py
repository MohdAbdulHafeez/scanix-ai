from modules.explainer.schemas import (
    ExplainResponse,
)


def explain(
    product_name: str,
    ingredients_text: str,
    nutrition_score: str | None,
    processing_level: int | None,
):

    score = (
        nutrition_score
        or "unknown"
    )

    processing = (
        processing_level
        or "unknown"
    )

    summary = (
        f"{product_name} contains "
        f"ingredients including "
        f"{ingredients_text[:120]}. "
        f"It has nutrition grade "
        f"{score.upper()} and "
        f"processing level "
        f"{processing}."
    )

    recommendation = (
        "Consume occasionally."
        if score in ["d", "e"]
        else "Generally acceptable."
    )

    return ExplainResponse(
        summary=summary,
        recommendation=recommendation,
    )