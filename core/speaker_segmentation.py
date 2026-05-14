<<<<<<< HEAD
import re

def segment_speakers(text):
    pattern = r"(Speaker\s[A-Z]):\s*(.*)"
=======
import re

def segment_speakers(text):
    pattern = r"(Speaker\s[A-Z]):\s*(.*)"
>>>>>>> 267031a0ab184a5dbfae0261ca5240bfa5144fda
    return re.findall(pattern, text)