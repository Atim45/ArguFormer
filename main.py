import sys
from core.comparison_engine import analyze_debate
from core.preprocessing import clean_text
from cli.args import get_args

from utils.logger import get_logger
from utils.config_loader import load_config


logger = get_logger("main")
logger.info("Initializing ArguFormer V2")

args = get_args()
config = load_config()

try:

    logger.info(f"Loading transcript from {args.input}")
    try:
      with open(args.input, "r", encoding="utf-8") as file:
        debate = file.read()

    except FileNotFoundError:
        logger.error(f"Input file not found: {args.input}")
        raise
    
    debate = file.read()
    cleaned_debate = clean_text(debate)

    result = analyze_debate(cleaned_debate)
    logger.info("Debate analysis completed successfully")
    print(result)

except Exception as e:

    logger.error(f"Pipeline failed: {str(e)}")