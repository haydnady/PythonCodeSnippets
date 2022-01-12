
from os.path import expanduser
from datetime import datetime
import logging
import os


fileName = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + " - log.txt"
logFileName = os.path.join(expanduser("~") + "\Desktop", fileName)


def _generateLog(logFileName=logFileName):
    """
    Create a logger object
    @param path Path of the log file.
    @return Logger object.

    Log level numeric values: `50=CRITICAL`, `40=ERROR`, `30=WARNING`, `20=INFO`, `10=DEBUG`, `0=NOTSET`.
    https://docs.python.org/3/library/logging.html#logging-levels
    """

    # Create a logger and set the level.
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create file handler, log format and add the format to file handler
    fileHandler = logging.FileHandler(logFileName, mode="a")

    # See https://docs.python.org/3/library/logging.html#logrecord-attributes
    # for log format attributes.
    logFormat = "%(asctime)s -  Line: %(lineno)d - Module: %(name)s - %(levelname)s - %(message)s \n"
    formatter = logging.Formatter(logFormat)
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger


def hello():
    logger.debug("Hello World!")


if __name__ == "__main__":
    logger = _generateLog()  # Initialize logging object.
    logger.info("Program started.")

    hello()

    logger.info("Program ended.")