from modules.ingredients.verifier import verify

from modules.ingredients.claims_engine import (
    evaluate,
)

from modules.ingredients.confidence import (
    compute as confidence_score,
)

from modules.ingredients.badges import (
    build as build_badges,
)

from modules.explainer.actions import (
    recommend,
)

from modules.recommendation.alternatives import (
    suggest,
)

from modules.scoring.scanix_score import (
    compute,
)

from modules.scoring.breakdown import (
    build,
)

from modules.scoring.processing import (
    describe,
)

from schemas.product import (
    ProductSchema,
    NutritionSchema,
)


def normalize_product(
    payload: dict,
):

    product = payload.get(
        "product"
    ) or {}

    nutriments = product.get(
        "nutriments"
    ) or {}

    ingredients_text = (
        product.get(
            "ingredients_text"
        )
        or ""
    )

    raw_ingredients = (
        product.get(
            "ingredients"
        )
        or []
    )

    allergens = (
        product.get(
            "allergens_tags"
        )
        or []
    )

    parsed_ingredients = [

        {
            "name": x["name"],
            "risk": x["risk"],
            "explanation": x["explanation"],
        }

        for x in verify(
            ingredients_text
        )
    ]

    claims = evaluate(
        raw_ingredients,
        ingredients_text,
    )

    score = compute(

        product.get(
            "nutriscore_grade"
        ),

        product.get(
            "nova_group"
        ),
    )

    breakdown = build(

        product.get(
            "nutriscore_grade"
        ),

        product.get(
            "nova_group"
        ),

        parsed_ingredients,
    )

    processing = describe(

        product.get(
            "nova_group"
        )
    )

    confidence = (
        confidence_score(
            parsed_ingredients,
            allergens,
        )
    )

    badges = (
        build_badges(
            confidence[
                "score"
            ]
        )
    )

    actions = (
        recommend(
            breakdown[
                "final_score"
            ]
        )
    )

    alternatives = (
        suggest(

            breakdown[
                "final_score"
            ],

            product.get(
                "nutriscore_grade"
            ),

            product.get(
                "nova_group"
            ),
        )
    )

    tags = [

        *(
            product.get(
                "_keywords"
            )
            or []
        ),

        f"scanix:{score['scanix_score']}",

        f"risk:{score['risk_level']}",

        f"good:{len(claims['positives'])}",

        f"bad:{len(claims['negatives'])}",

        f"score:{breakdown['final_score']}",

        f"process:{processing['label']}",

        f"confidence:{confidence['score']}",

        *[
            f"positive:{x['claim']}"
            for x
            in claims[
                "positives"
            ]
        ],

        *[
            f"negative:{x['claim']}"
            for x
            in claims[
                "negatives"
            ]
        ],

        *[
            f"badge:{x}"
            for x
            in badges
        ],

        *[
            f"action:{x}"
            for x
            in actions
        ],

        *[
            f"alternative:{x['title']}"
            for x
            in alternatives
        ],
    ]

    return ProductSchema(

        barcode=payload.get(
            "barcode"
        ),

        name=(
            product.get(
                "product_name"
            )
            or "Unknown Product"
        ),

        brand=product.get(
            "brands"
        ),

        category=product.get(
            "categories"
        ),

        quantity=product.get(
            "quantity"
        ),

        image_url=product.get(
            "image_url"
        ),

        ingredients_text=ingredients_text,

        ingredients=parsed_ingredients,

        allergens=allergens,

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

        tags=tags,

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