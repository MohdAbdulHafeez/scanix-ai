from pathlib import Path
from uuid import uuid4

from gtts import gTTS


VOICE_DIR = Path(
    "generated/voice"
)

VOICE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def generate_voice(
    text: str,
):

    filename = (
        f"{uuid4()}.mp3"
    )

    path = (
        VOICE_DIR
        / filename
    )

    tts = gTTS(
        text=text,
        lang="en",
    )

    tts.save(
        str(path)
    )

    return {
        "filename": filename,
        "path": str(path),
    }