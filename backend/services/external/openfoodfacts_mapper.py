from modules.ingredients.verifier import verify

from modules.scoring.scanix_score import (
    compute,
)

from schemas.product import (
    ProductSchema,
    NutritionSchema,
)


def normalize_product(
    payload: dict,
):

    product = (
        payload.get(
            "product"
        )
        or {}
    )

    nutriments = (
        product.get(
            "nutriments"
        )
        or {}
    )

    ingredients_text = (
        product.get(
            "ingredients_text"
        )
        or ""
    )

    score = compute(
        product.get(
            "nutriscore_grade"
        ),
        product.get(
            "nova_group"
        ),
    )

    return ProductSchema(

        barcode=(
            payload.get(
                "barcode"
            )
        ),

        name=(
            product.get(
                "product_name"
            )
            or "Unknown Product"
        ),

        brand=(
            product.get(
                "brands"
            )
        ),

        category=(
            product.get(
                "categories"
            )
        ),

        quantity=(
            product.get(
                "quantity"
            )
        ),

        image_url=(
            product.get(
                "image_url"
            )
        ),

        ingredients_text=(
            ingredients_text
        ),

        ingredients=[
            {
                "name": x["name"],
                "risk": x["risk"],
                "explanation": x["explanation"],
            }
            for x in verify(
                ingredients_text
            )
        ],

        allergens=(
            product.get(
                "allergens_tags"
            )
            or []
        ),

        nutrition_score=(
            product.get(
                "nutriscore_grade"
            )
        ),

        eco_score=(
            product.get(
                "ecoscore_grade"
            )
        ),

        processing_level=(
            product.get(
                "nova_group"
            )
        ),

        country=(
            product.get(
                "countries"
            )
        ),

        tags=[
            *(
                product.get(
                    "_keywords"
                )
                or []
            ),

            f"scanix:{score['scanix_score']}",

            f"risk:{score['risk_level']}",
        ],

        nutrition=NutritionSchema(

            energy_kcal=(
                nutriments.get(
                    "energy-kcal_100g"
                )
            ),

            proteins=(
                nutriments.get(
                    "proteins_100g"
                )
            ),

            carbohydrates=(
                nutriments.get(
                    "carbohydrates_100g"
                )
            ),

            sugars=(
                nutriments.get(
                    "sugars_100g"
                )
            ),

            fat=(
                nutriments.get(
                    "fat_100g"
                )
            ),

            saturated_fat=(
                nutriments.get(
                    "saturated-fat_100g"
                )
            ),

            fiber=(
                nutriments.get(
                    "fiber_100g"
                )
            ),

            sodium=(
                nutriments.get(
                    "sodium_100g"
                )
            ),

        ),
    )