from pydantic import BaseModel


class ExplainRequest(BaseModel):

    product_name: str

    ingredients_text: str

    nutrition_score: str | None = None

    processing_level: int | None = None


class ExplainResponse(BaseModel):

    summary: str

    recommendation: str