import logging
import os
from me.personal.constant import LOG_FORMAT


logging.basicConfig(filename="../../logs/newfile.log" , format = LOG_FORMAT , level = logging.WARN , filemode="w" )
logger = logging.getLogger(__name__)


def main():

    print("### from main function")
    logger.debug("@@@ from logger.debug method")
    logger.info("@@@ from logger.info method")
    logger.warning("@@@ from logger.warning method")
    logger.error("@@@ from logger.error method")
    logger.critical("@@@ from logger.critical method")


if __name__ == "__main__":
    main()


