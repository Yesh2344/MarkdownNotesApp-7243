import logging
import os

def get_logger(name: str):
    """
    Get a logger.

    Args:
        name (str): Logger name.

    Returns:
        logger: Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    return logger