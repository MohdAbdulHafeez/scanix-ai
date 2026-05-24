from fastapi import APIRouter


router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
)


@router.post("")
async def verify(
    body: dict,
):

    ingredients = (
        body.get(
            "ingredients",
            ""
        )
    )

    items = [

        x.strip()

        for x in ingredients.split(",")

        if x.strip()

    ]


    result = []

    score = 100


    for item in items:

        lower = item.lower()


        risk = "safe"

        explanation = "Looks okay."


        if "sugar" in lower:

            risk = "high"

            explanation = (
                "High added sugar."
            )

            score -= 25


        elif "palm" in lower:

            risk = "medium"

            explanation = (
                "High saturated fat."
            )

            score -= 15


        elif "cocoa" in lower:

            explanation = (
                "Natural ingredient."
            )


        result.append({

            "name":
            item,

            "risk":
            risk,

            "explanation":
            explanation,

        })


    return {

        "success":
        True,

        "ingredients":
        result,

        "score":
        max(
            score,
            0,
        ),

        "recommendation":

        "Excellent"

        if score >= 80

        else

        "Consume occasionally"

    }