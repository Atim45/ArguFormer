import logging
from logging.handlers import RotatingFileHandler
import os

from transformers import logger   

os.mkdir('logs', exist_ok=True)

def get_logger(name : str) -> logging.logger:
    logger = logging.getLogger(name)

    if logging.handlers:
        return logger
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                    datefmt='%Y-%m-%d %H:%M:%S')
    app_handler = RotatingFileHandler('logs/app.log', maxBytes=2_000_000, backupCount=3)
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(formatter)

    error_handler = RotatingFileHandler('logs/error.log', maxBytes=2_000_000, backupCount=3)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    bench_handler = RotatingFileHandler('logs/benchmark.log', maxBytes=2_000_000, backupCount=3)
    bench_handler.setLevel(logging.DEBUG)
    bench_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(bench_handler)
    logger.addHandler(console_handler)

    return logger
