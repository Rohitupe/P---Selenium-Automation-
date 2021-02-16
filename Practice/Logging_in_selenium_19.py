"""
    * what is logging ?
        -- Every activity user do on a website is get logged in to ad file called log file
        -- Use => we can check weather everything is fine with website or not

        --> when we report bug/issue with developer along with screenshot we have to share log file as well
        so developer can try to understand the issue by seeing the log file.

        --> we can also implement this logging mechanism into our automation code

    '''
        * Logging & Log levels -->
            - Logging is very useful tool in a programmer's toolbox. It can help you develop a better
            understanding of the flow of a program and discover scenarios that you might not even have through
            of while developing.
            - Log Levels
                = DEBUG
                = INFO
                = WARNING
                = ERROR
                = CRITICAL
    '''
"""

import logging  # to work with logging (in-built package)

# in which file we want to log errors
logFile = r"C:\Users\rohit\PycharmProjects\Selenium_Automation\Files&Folder\Selenium_Logs\LogFile_19.log"

# 1. One Method
logging.basicConfig(filename=logFile,
                    format='%(asctime)s: %(levelname)s: %(message)s',  # to specify time and date when log added
                    datefmt='%d/%m/%Y %I:%M:%S %p',  # to specify date format
                    level=logging.DEBUG  # to get debug message as well
                    )
"""
 * different levels of logs
    logging.debug("This is debug message")
    logging.info("This is info message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")
"""

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")


# 2. Second Method
logging.basicConfig(filename=logFile,
                    format='%(asctime)s: %(levelname)s: %(message)s',  # to specify time and date when log added
                    datefmt='%d/%m/%Y %I:%M:%S %p'  # to specify date format
                    )
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # to get debug message as well

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")