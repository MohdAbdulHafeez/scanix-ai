from modules.ingredients.rules import RULES
from modules.ingredients.ingredient_ai import generate_summary


async def verify_ingredients(
    ingredients_text: str,
):

    rows = []

    score = 100


    items = [

        x.strip()

        for x in ingredients_text.split(",")

        if x.strip()

    ]


    for item in items:

        matched = None


        for key in RULES:

            if key in item.lower():

                matched = RULES[key]

                break


        if matched:

            score -= matched["penalty"]

            rows.append({

                "name": item,

                "level": matched["level"],

                "reason": matched["reason"],

            })

        else:

            rows.append({

                "name": item,

                "level": "safe",

                "reason": "No major concerns.",

            })


    score = max(
        score,
        0,
    )


    summary = await generate_summary(
        rows,
        score,
    )


    verdict = (

        "Excellent"

        if score >= 85

        else

        "Good"

        if score >= 65

        else

        "Consume Occasionally"

    )


    return {

        "ingredients": rows,

        "score": score,

        "summary": summary,

        "verdict": verdict,

    }



# compatibility for existing barcode flow
def verify_claims(
    claims=None,
):

    return claims or []