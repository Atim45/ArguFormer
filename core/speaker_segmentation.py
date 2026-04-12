import re

def segment_speakers(text):
    pattern = r"(Speaker\s[A-Z]):\s*(.*)"
    return re.findall(pattern, text)