from google import genai

from core.settings import settings


client = None

if settings.GEMINI_API_KEY:

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )


MODEL = "gemini-2.5-flash"


async def ask_ai(
    prompt: str,
):

    if not client:

        return (
            "Gemini not configured."
        )

    response = (
        client.models.generate_content(
            model=MODEL,
            contents=prompt,
        )
    )

    return response.text