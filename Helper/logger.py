import logging
import os
from datetime import date
from config import get_configuration

config = get_configuration()

class Logger:
    def __init__(self):
        # Create the csplit and cvdn folders if they don't exist
        if not os.path.exists(config.log_file_path):
            os.makedirs(config.log_file_path)

        csplit_folder = os.path.join(config.log_file_path, 'csplit')
        if not os.path.exists(csplit_folder):
            os.makedirs(csplit_folder)

        cvdn_folder = os.path.join(config.log_file_path, 'cvdn')
        if not os.path.exists(cvdn_folder):
            os.makedirs(cvdn_folder)

        # Create a formatter
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Get today's date
        today = date.today().strftime('%Y-%m-%d')

        # Set the log file paths
        self.csplit_log_file = os.path.join(csplit_folder, f'{today}.log')
        self.cvdn_log_file = os.path.join(cvdn_folder, f'{today}.log')

        """# Set the log file paths in the configuration
        config.csplit_log_file = csplit_log_file
        config.cvdn_log_file = cvdn_log_file"""

    def csplit_logger(self):
        # Create a logger for csplit
        csplit_logger = logging.getLogger('csplit')
        csplit_logger.setLevel(logging.DEBUG)

        # Create a handler for csplit.log
        csplit_handler = logging.FileHandler(self.csplit_log_file)
        csplit_handler.setLevel(logging.DEBUG)
        csplit_handler.setFormatter(self.formatter)

        # Add the handlers to the logger
        csplit_logger.addHandler(csplit_handler)

        return csplit_logger

    def cvdn_logger(self):
        # Create a logger for cvdn
        cvdn_logger = logging.getLogger('cvdn')
        cvdn_logger.setLevel(logging.DEBUG)

        # Create a handler for cvdn.log
        cvdn_handler = logging.FileHandler(self.cvdn_log_file)
        cvdn_handler.setLevel(logging.DEBUG)
        cvdn_handler.setFormatter(self.formatter)

        # Add the handlers to the logger
        cvdn_logger.addHandler(cvdn_handler)

        return cvdn_logger
