from transformers import pipeline

from utils.logger import get_logger
from utils.config_loader import load_config

logger = get_logger("fallacy_transformer")
config = load_config()


class FallacyTransformerModel:
    def __init__(self):
        logger.info("Loading transformer model")
        self.pipe = pipeline(
            "text-classification",
            model=config["models"]["fallacy"])
        logger.info("Transformer model loaded")

    def predict(self, sentence: str):
        logger.info("Running transformer prediction")
        result = self.pipe(sentence)[0]
        return {
            "model": "transformer",
            "prediction": result["label"],
            "confidence": round(float(result["score"]), 3)}