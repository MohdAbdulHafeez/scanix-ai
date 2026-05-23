from fastapi import APIRouter

from modules.explainer.schemas import (
    ExplainRequest,
)

from modules.explainer.gemini_service import (
    explain_ai,
)


router = APIRouter(
    prefix="/explain",
    tags=["ai"],
)


@router.post("")
async def explain_food(
    body: ExplainRequest,
):

    result = await explain_ai(

        body.product_name,

        body.ingredients_text,

        body.nutrition_score
        or "unknown",
    )

    return {
        "success": True,
        "explanation": result,
    }