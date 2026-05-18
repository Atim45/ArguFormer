import yaml

from utils.logger import get_logger

logger = get_logger("config")


def load_config(path="configs/default.yaml"):

    logger.info(f"Loading config from {path}")

    with open(path, "r") as file:
        config = yaml.safe_load(file)

    logger.info("Configuration loaded successfully")

    return config