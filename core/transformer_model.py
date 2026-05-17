from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

toxicity_model = pipeline(
    "text-classification",
    model="unitary/toxic-bert"
)

fallacy_model = pipeline(
    "text-classification",
    model="q3fer/distilbert-base-fallacy-classification"
)

def transformer_analysis(sentence):

    sentiment = sentiment_model(sentence)[0]["label"]
    toxicity = toxicity_model(sentence)[0]["label"]

    fallacy_result = fallacy_model(sentence)[0]
    fallacy = fallacy_result["label"]
    score = fallacy_result["score"]

    return sentiment, toxicity, fallacy, score