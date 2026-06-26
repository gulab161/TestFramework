# -------------------------------------------------------------
# File Name   : logger.py
# Description : Configures logging for the Test Automation
#               Framework. Creates log file inside logs/
#               directory and records all framework events.
# -------------------------------------------------------------

import os
import logging
from datetime import datetime


class Logger:

    def __init__(self):
        """
        Initializes logger and creates log directory and file.
        """

        # Create logs directory if not exists
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Log file name with date
        log_file = f"logs/framework.log"

        # Configure logging format
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger("TestFramework")

    def info(self, message):
        """
        Log INFO level messages
        """
        self.logger.info(message)

    def error(self, message):
        """
        Log ERROR level messages
        """
        self.logger.error(message)

    def warning(self, message):
        """
        Log WARNING level messages
        """
        self.logger.warning(message)
