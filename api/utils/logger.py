import logging


def setup_logger(name: str = None):
    """
    Sets up a logger with a specific format that includes time, filename,
    error level, and the message, separated by pipes.

    Args:
        name (str): The name of the logger. Defaults to None for the root logger.

    Returns:
        logging.Logger: Configured logger.
    """
    # Define log format
    log_format = "%(asctime)s | %(filename)s | %(levelname)s | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Create a logger
    logger = logging.getLogger(name)

    # Set the default log level
    logger.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it to the handler
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger
