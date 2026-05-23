from modules.explainer.prompts import (
    SYSTEM_PROMPT,
)

from services.ai.gemini import (
    ask_ai,
)


async def explain_ai(
    product_name: str,
    ingredients_text: str,
    nutrition_score: str,
):

    prompt = f"""
{SYSTEM_PROMPT}

Product:
{product_name}

Ingredients:
{ingredients_text}

Nutrition:
{nutrition_score}

Explain.
"""

    return await ask_ai(
        prompt
    )