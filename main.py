from core.preprocessing import clean_text

from cli.args import get_args

from utils.logger import get_logger
from utils.config_loader import load_config

from models.fallacy_lr import FallacyLRModel
from models.fallacy_transformer import FallacyTransformerModel

from core.comparator import compare_models


logger = get_logger("main")

logger.info("Initializing ArguFormer V2")

args = get_args()

config = load_config()


try:

    logger.info(f"Loading transcript from {args.input}")

    with open(args.input, "r", encoding="utf-8") as file:
        debate = file.read()

    cleaned_debate = clean_text(debate)

    # TEST MODELS
    lr_model = FallacyLRModel()

    transformer_model = FallacyTransformerModel()

    sentence = "You are stupid so your argument is invalid"

    comparison_result = compare_models(
        sentence,
        lr_model,
        transformer_model
    )

    print(comparison_result)

except Exception as e:

    logger.error(f"Pipeline failed: {str(e)}")