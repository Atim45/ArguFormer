class ArguformerException(Exception):
    """Base class for exceptions in arguformer."""
    pass
class TranscriptError(ArguformerException):
    """Exception raised for errors in the transcript."""
    pass
class ModelError(ArguformerException):
    """Exception raised for errors in the model."""
    pass
class LanguageError(ArguformerException):
    """Exception raised for errors in language processing."""
    pass
class SegmentationError(ArguformerException):
    """Exception raised for errors in segmentation."""
    pass
