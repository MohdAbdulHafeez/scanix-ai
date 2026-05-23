from fastapi import APIRouter

from modules.voice.service import (
    generate_voice,
)


router = APIRouter(
    prefix="/voice",
    tags=["voice"],
)


@router.post("")
async def create_voice(
    body: dict,
):

    result = (
        generate_voice(
            body["text"]
        )
    )

    return {
        "success": True,
        **result,
    }