from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from utils.logger import get_logger

logger = get_logger("fallacy_lr")

class FallacyLRModel:
    def __init__(self):
        logger.info("Initializing LR + TF-IDF model")
        self.texts = [
            # Ad Hominem
            "You are stupid so your argument is wrong",
            "Only an idiot would believe that",
            "You are completely dumb",

            # Appeal to Emotion
            "Think about the poor children suffering",
            "If you don't agree, people will get hurt",
            "This will destroy our future if we don't act",

            # Strawman
            "You twisted my argument completely",
            "That's not what I said at all",

            # False Dilemma
            "You're either with us or against us",
            "There are only two options here",

            # Slippery Slope
            "If we allow this, everything will collapse",
            "This small step will lead to disaster",

            # Circular Reasoning
            "It's true because it's correct",
            "This is valid because it's true",

            # Hasty Generalization
            "All politicians are corrupt",
            "Everyone from that place is rude",

            # Red Herring
            "Let's focus on something else instead",
            "This is distracting from the real issue"
        ]

        self.labels = [
            "Ad Hominem",
            "Ad Hominem",
            "Ad Hominem",

            "Appeal to Emotion",
            "Appeal to Emotion",
            "Appeal to Emotion",

            "Strawman",
            "Strawman",

            "False Dilemma",
            "False Dilemma",

            "Slippery Slope",
            "Slippery Slope",

            "Circular Reasoning",
            "Circular Reasoning",

            "Hasty Generalization",
            "Hasty Generalization",

            "Red Herring",
            "Red Herring"
        ]

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            stop_words="english"
        )

        X = self.vectorizer.fit_transform(self.texts)

        self.model = LogisticRegression(max_iter=1000)

        self.model.fit(X, self.labels)

        logger.info("LR model trained successfully")

    def predict(self, sentence: str):

        logger.info("Running LR prediction")

        vector = self.vectorizer.transform([sentence])

        prediction = self.model.predict(vector)[0]

        probabilities = self.model.predict_proba(vector)[0]

        confidence = max(probabilities)

        return {
            "model": "lr",
            "prediction": prediction,
            "confidence": round(float(confidence), 3)
        }