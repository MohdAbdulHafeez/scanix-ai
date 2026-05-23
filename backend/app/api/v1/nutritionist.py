from fastapi import APIRouter

from services.external.openfoodfacts import (
    openfoodfacts,
)

from services.external.openfoodfacts_mapper import (
    normalize_product,
)

from modules.explainer.gemini_service import (
    explain_ai,
)

from modules.voice.service import (
    generate_voice,
)


router = APIRouter(
    prefix="/nutritionist",
    tags=["nutritionist"],
)


@router.post("")
async def nutritionist(
    body: dict,
):

    barcode = (
        body["barcode"]
    )

    raw = await (
        openfoodfacts.lookup(
            barcode
        )
    )

    if not raw["found"]:

        return {
            "success": False,
            "message": "Product not found",
        }

    product = (
        normalize_product(
            raw
        )
    )

    explanation = await (
        explain_ai(
            product.name,
            product.ingredients_text
            or "",
            product.nutrition_score
            or "unknown",
        )
    )

    voice = (
        generate_voice(
            explanation
        )
    )

    return {

        "success": True,

        "product": (
            product.model_dump()
        ),

        "explanation": (
            explanation
        ),

        "voice": voice,
    }