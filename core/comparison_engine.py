import pandas as pd

from core.speaker_segmentation import segment_speakers
from core.traditional_model import traditional_fallacy
from core.transformer_model import transformer_analysis


def analyze_debate(debate):

    segments = segment_speakers(debate)

    results = []

    for speaker, sentence in segments:

        fallacy_v1 = traditional_fallacy(sentence)

        sentiment_v2, toxicity_v2, fallacy_v2, score = transformer_analysis(sentence)

        if fallacy_v1 == fallacy_v2:
            final = fallacy_v2
            confidence = "High (models agree)"
        else:
            final = fallacy_v2
            confidence = "Medium (transformer preferred)"

        results.append({
            "Speaker": speaker,
            "Sentence": sentence,
            "Sentiment": sentiment_v2,
            "Toxicity": toxicity_v2,
            "Traditional_Fallacy": fallacy_v1,
            "Transformer_Fallacy": fallacy_v2,
            "Confidence_Score": score,
            "Final_Judgement": final,
            "Agreement": confidence
        })

    df = pd.DataFrame(results)

    df.to_csv("outputs/debate_analysis.csv", index=False)

    return df