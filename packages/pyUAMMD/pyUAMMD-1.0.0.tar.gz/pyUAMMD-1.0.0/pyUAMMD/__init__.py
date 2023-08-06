import os
import logging

class CustomFormatter(logging.Formatter):

    white = "\x1b[37;20m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format     = "%(asctime)s - %(name)s - %(levelname)s - %(message)s "
    formatLine = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: white + formatLine + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + formatLine + reset,
        logging.CRITICAL: bold_red + formatLine + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt,datefmt='%d/%m/%Y %H:%M:%S')

        return formatter.format(record)

# Set up logger
logger = logging.getLogger("pyUAMMD")
logger.setLevel(logging.INFO)

clog = logging.StreamHandler()

clog.setFormatter(CustomFormatter())
logger.addHandler(clog)

UAMMD_PATH = None
UAMMD_STRUCTURED_PATH = None

try:
    # Try to import read environment variables UAMMD_PATH and UAMMD_STRUCTURED_PATH

    UAMMD_PATH = os.environ['UAMMD_PATH']
    UAMMD_STRUCTURED_PATH = os.environ['UAMMD_STRUCTURED_PATH']

except:

    logger.warning("UAMMD_PATH and UAMMD_STRUCTURED_PATH environment variables not found.")

from .simulation import simulation


