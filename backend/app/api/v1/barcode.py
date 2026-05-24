from fastapi import APIRouter


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


@router.get(
    "/{barcode}"
)
async def scan_barcode(
    barcode: str,
):

    raw = await (
        openfoodfacts.lookup(
            barcode
        )
    )

    if (
        not raw[
            "found"
        ]
    ):

        return raw

    return (
        normalize_product(
            raw
        )
    )