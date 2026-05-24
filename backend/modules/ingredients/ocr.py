import easyocr
import tempfile
from pathlib import Path


reader = easyocr.Reader(
    ["en"],
    gpu=False,
)


async def extract_ingredients_text(
    file,
):

    suffix = Path(
        file.filename
    ).suffix


    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp:

        temp.write(
            await file.read()
        )

        temp_path = temp.name


    result = reader.readtext(
        temp_path,
        detail=0,
    )


    text = "\n".join(
        result
    )


    return text