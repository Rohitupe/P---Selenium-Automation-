import logging


def test_logging():
    # 1. __name__ will get the file name for which this logged message is printed
    logger = logging.getLogger(__name__)

    # 3. to specify the actual file we use filehandler
    file = logging.FileHandler("logfile.log")

    # 4. in What format it should write it in the log file that we will specify here
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    """ Date : Error Type :  Test Case Name : Message"""
    file.setFormatter(formatter)  # tell file to use this format for logging

    # 5. add all these log messages in file for this we use addHandler
    logger.addHandler(file)

    # 2. Different logging messages #
    logger.setLevel(logging.INFO)  # logs after info will be shown

    # a. this is will be printed when
    logger.debug("This is debug message")
    logger.info("This is info message")

    # b. this will be printed on console
    logger.warning("This is warning message")
    logger.error("This is error message")
    logger.critical("This is critical message")
