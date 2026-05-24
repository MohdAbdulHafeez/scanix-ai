from pathlib import Path
from uuid import uuid4

from gtts import gTTS


# -------------------------
# STORAGE
# -------------------------

VOICE_DIR = Path(
    "generated/voice"
)

VOICE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# -------------------------
# GENERATE VOICE
# -------------------------

def generate_voice(
    text: str,
):

    try:

        if (
            not text
            or
            not text.strip()
        ):

            return None


        filename = (
            f"{uuid4()}.mp3"
        )


        filepath = (
            VOICE_DIR
            /
            filename
        )


        tts = gTTS(

            text=text,

            lang="en",

            slow=False,

        )


        tts.save(
            str(filepath)
        )


        return {

            "filename":
            filename,

            # PUBLIC URL
            # frontend audio src uses this

            "path":
            f"/generated/voice/{filename}",

        }


    except Exception as e:

        print(
            "\nVOICE ERROR\n",
            e,
            "\n",
        )

        return {

            "filename":
            None,

            "path":
            None,

        }