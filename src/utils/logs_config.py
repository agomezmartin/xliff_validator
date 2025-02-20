import logging
import os
import sys
from datetime import datetime

# LOG types:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# Create a logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Generate a timestamped log filename
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_log.log")
log_filepath = os.path.join(log_dir, log_filename)

# Configure INFO logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Configure DEBUG logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Configure WARNING logging
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Configure ERROR logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Configure CRITIAL logging
logging.basicConfig(
    level=logging.CRITICAL,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)
