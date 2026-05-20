from transformers import pipeline

from utils.logger import get_logger

logger = get_logger("fallacy_transformer")


class FallacyTransformerModel:

    def __init__(self):

        logger.info("Loading transformer model")

        self.pipe = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )

        self.labels = [
            "Ad Hominem",
            "Appeal to Emotion",
            "Strawman",
            "False Dilemma",
            "Slippery Slope",
            "Circular Reasoning",
            "Hasty Generalization",
            "Red Herring"
        ]

        logger.info("Transformer model loaded")

    def predict(self, sentence: str):

        logger.info("Running transformer prediction")

        result = self.pipe(
            sentence,
            candidate_labels=self.labels
        )

        prediction = result["labels"][0]

        confidence = result["scores"][0]

        return {
            "model": "transformer",
            "prediction": prediction,
            "confidence": round(float(confidence), 3)
        }