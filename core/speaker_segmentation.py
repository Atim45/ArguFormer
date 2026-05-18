import re
from utils.exceptions import SegmentationError, TranscriptError
from utils.logger import get_logger
logger = get_logger()

def segment_speakers(text):
    pattern = r"(Speaker\s[A-Z]):\s*(.*)"
    return re.findall(pattern, text)

def segment(transcript):
    logger.info("Running speaker segmentation")

    if transcript is None or transcript.strip() == "":
        raise TranscriptError("Transcript is empty or None.")
    try:
        segments = segment_speakers(transcript)

        logger.info(f"Found {len(segments)} speaker segments")

        if len(segments) == 0:
            raise SegmentationError("No speaker segments found in the transcript.")
        return segments
    except SegmentationError:
        logger.error("SegmentationError occurred.")
        raise
    except Exception as e:
        logger.error(f"An error occurred during segmentation: {str(e)}")
        raise SegmentationError(f"An error occurred during segmentation: {str(e)}")