import os
import sys
import logging
import colorlog

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_filepath = os.path.join(log_dir, "running_logs.log")

log_format = "%(log_color)s[%(levelname)s]%(reset)s - %(message)s"


def setup_logger():
    """Sets up and returns a colorized logger."""
    
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_filepath = os.path.join(log_dir, "running_logs.log")

    log_format = "%(log_color)s[%(levelname)s]%(reset)s - %(message)s"

    log_colors = {
        'INFO': 'green',
        'DEBUG': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'magenta'
    }

    console_handler = colorlog.StreamHandler(sys.stdout)
    console_formatter = colorlog.ColoredFormatter(
        log_format, log_colors=log_colors
    )
    console_handler.setFormatter(console_formatter)

    logger = logging.getLogger("TextSummarization-Logger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_filepath)
    file_formatter = logging.Formatter('%(levelname)s %(message)s')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("Logger is set up successfully.")

    return logger


logger = setup_logger()
