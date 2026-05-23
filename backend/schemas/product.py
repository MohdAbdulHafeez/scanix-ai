from typing import List, Optional

from pydantic import BaseModel, Field


class NutritionSchema(BaseModel):
    energy_kcal: Optional[float] = None
    proteins: Optional[float] = None
    carbohydrates: Optional[float] = None
    sugars: Optional[float] = None
    fat: Optional[float] = None
    saturated_fat: Optional[float] = None
    fiber: Optional[float] = None
    sodium: Optional[float] = None


class IngredientSchema(BaseModel):
    name: str
    risk: str = "unknown"
    explanation: Optional[str] = None


class ProductSchema(BaseModel):
    barcode: str

    name: str

    brand: Optional[str] = None

    category: Optional[str] = None

    quantity: Optional[str] = None

    image_url: Optional[str] = None

    ingredients_text: Optional[str] = None

    ingredients: List[IngredientSchema] = []

    allergens: List[str] = []

    nutrition: NutritionSchema

    nutrition_score: Optional[str] = None

    eco_score: Optional[str] = None

    processing_level: Optional[int] = None

    country: Optional[str] = None

    tags: List[str] = []

    source: str = "openfoodfacts"

    confidence: float = Field(
        default=0.99,
        ge=0,
        le=1
    )