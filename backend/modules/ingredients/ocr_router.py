from fastapi import (
    APIRouter,
    UploadFile,
    File,
)

from modules.ingredients.ocr import (
    extract_ingredients_text,
)


router = APIRouter(

    prefix="/ingredients",

    tags=["ingredients"],

)


@router.post(
    "/image"
)
async def verify_image(
    image: UploadFile = File(...)
):

    text = await extract_ingredients_text(
        image
    )


    return {

        "success": True,

        "ingredients_text":
        text,

    }