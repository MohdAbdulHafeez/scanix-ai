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

    question = body.get(
        "question",
        ""
    )

    barcode = body.get(
        "barcode"
    )

    # -----------------
    # NORMAL CHAT MODE
    # -----------------

    if not barcode:

        explanation = await (
            explain_ai(
                question,
                "",
                "unknown",
            )
        )

        voice = (
            generate_voice(
                explanation
            )
        )

        return {

            "success": True,

            "question": question,

            "answer": explanation,

            "voice": voice,
        }

    # -----------------
    # PRODUCT MODE
    # -----------------

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

        "answer": explanation,

        "voice": voice,
    }