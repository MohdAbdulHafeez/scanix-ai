from fastapi import APIRouter

from modules.barcode.schemas import (
    BarcodeRequest,
)

from services.external.openfoodfacts import (
    openfoodfacts,
)

from services.external.openfoodfacts_mapper import (
    normalize_product,
)


router = APIRouter(
    prefix="/barcode",
    tags=["barcode"],
)


@router.post("")
async def scan_barcode(
    body: BarcodeRequest,
):

    raw = await (
        openfoodfacts.lookup(
            body.barcode
        )
    )

    if not raw["found"]:

        return raw

    return normalize_product(
        raw
    )