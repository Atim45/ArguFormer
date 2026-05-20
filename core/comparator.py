from utils.logger import get_logger
logger = get_logger("comparator")

def compare_models(sentence, lr_model, transformer_model):
    logger.info("Running model comparison")
    
    lr_result = lr_model.predict([sentence])
    transformer_result = transformer_model.predict(sentence)

    agreement = (lr_result("prediction") == transformer_result("prediction"))
    
    if transformer_result("confidence") > lr_result("confidence"):
        prefered = transformer_result
    else:
        prefered = lr_result
    logger.info("Comparison completed | Agreement : {agreement}")
    return {
        "sentence": sentence,
        "agreement": agreement,
        "lr_prediction": lr_result,
        "transformer_prediction": transformer_result,
        "prefered_prediction": prefered,

    }
