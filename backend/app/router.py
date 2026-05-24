from fastapi import APIRouter


# ROOT ROUTER
router = APIRouter(
    prefix="/api/v1"
)


# IMPORT WORKING ENDPOINTS
from app.api.v1.barcode import router as barcode_router
from app.api.v1.nutritionist import router as nutritionist_router


# NEW
from modules.ingredients.router import (
    router as ingredients_router
)


router.include_router(
    barcode_router
)

router.include_router(
    nutritionist_router
)

router.include_router(
    ingredients_router
)