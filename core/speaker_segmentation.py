import re
from utils.exceptions import SegmentationError, TranscriptError

def segment_speakers(text):
    pattern = r"(Speaker\s[A-Z]):\s*(.*)"
    return re.findall(pattern, text)
def segment(transcript):
    if transcript is None or transcript.strip() == "":
        raise TranscriptError("Transcript is empty or None.")
    try:
        segments = segment_speakers(transcript)
        if len(segments) == 0:
            raise SegmentationError("No speaker segments found in the transcript.")
        return segments
    except SegmentationError:
        raise
    except Exception as e:
        raise SegmentationError(f"An error occurred during segmentation: {str(e)}")