import httpx

from core.settings import settings


class OpenFoodFacts:

    BASE = (
        settings.OPENFOODFACTS_BASE_URL
    )

    async def lookup(
        self,
        barcode: str,
    ):

        url = (
            f"{self.BASE}/api/v2/product/{barcode}.json"
        )

        async with httpx.AsyncClient(
            timeout=15
        ) as client:

            res = await client.get(
                url
            )

            data = res.json()

            return {
                "found": (
                    data.get(
                        "status"
                    )
                    == 1
                ),
                "barcode": barcode,
                "product": data.get(
                    "product"
                ),
            }


openfoodfacts = (
    OpenFoodFacts()
)