import re
import unicodedata

from utils.logger import get_logger
from utils.exceptions import TranscriptError

logger = get_logger("preprocessing")


def clean_text(text: str) -> str:

    logger.info("Starting text preprocessing")

    if text is None or text.strip() == "":
        logger.error("Input transcript is empty")
        raise TranscriptError("Transcript is empty.")

    try:
        text = unicodedata.normalize("NFKC", text)
        text = re.sub(r"\s+", " ", text)
        text = text.replace("\\n", "\n")
        text = re.sub(r"[!?]{2,}", "!", text)
        text = text.strip()
        logger.info("Text preprocessing completed")
        return text

    except Exception as e:

        logger.error(f"Preprocessing failed: {str(e)}")

        raise TranscriptError(
            f"Preprocessing failed: {str(e)}"
        )