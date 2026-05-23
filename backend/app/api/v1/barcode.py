from fastapi import APIRouter

from modules.barcode.schemas import (
    BarcodeRequest,
)

from services.external.openfoodfacts import (
    openfoodfacts,
)


router = APIRouter(
    prefix="/barcode",
    tags=["barcode"],
)


@router.post("")
async def scan_barcode(
    body: BarcodeRequest,
):

    return await (
        openfoodfacts.lookup(
            body.barcode
        )
    )