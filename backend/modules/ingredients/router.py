from fastapi import APIRouter

from modules.ingredients.ingredient_verifier import (
    verify_ingredients,
)


router = APIRouter(

    prefix="/ingredients",

    tags=["ingredients"],

)


@router.post("")
async def verify(
    body: dict,
):

    text = (

        body.get(
            "ingredients",
            ""
        )

    )


    result = await verify_ingredients(
        text
    )


    return {

        "success": True,

        "ingredients":

        result.get(
            "ingredients",
            []
        ),

        "score":

        result.get(
            "score",
            0,
        ),

        "summary":

        result.get(
            "summary",
            "",
        ),

        "verdict":

        result.get(
            "verdict",
            "",
        ),

    }