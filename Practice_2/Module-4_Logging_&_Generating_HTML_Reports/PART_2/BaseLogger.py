import inspect
import logging


class BaseLoggerCode:
    def test_logger(self):
        # to get the name of actual file which is runnig the test
        loggerFileName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerFileName)
        file = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file.setFormatter(formatter)
        logger.addHandler(file)
        return logger
