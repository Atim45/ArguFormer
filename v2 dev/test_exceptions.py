from utils.exceptions import TranscriptError
from core.speaker_segmentation import segment

try:
    segment("")
except TranscriptError as e:
    print(f"Caught expected exception: {e}")
try:
    segment(None)
except TranscriptError as e:
    print(f"Caught expected exception: {e}")