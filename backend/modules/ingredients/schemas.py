from pydantic import BaseModel


class IngredientRow(
    BaseModel,
):

    name: str

    level: str

    reason: str



class IngredientResponse(
    BaseModel,
):

    ingredients: list[IngredientRow]

    score: int

    summary: str

    verdict: str