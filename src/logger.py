import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# if __name__ == "__main__":
#     #logger = setup_logger(__name__)
#     logging.info("Logger has been set up successfully.")

# def setup_logger(name: str, level=logging.INFO) -> logging.Logger:
#     """
#     Set up a logger with the specified name and level.

#     Args:
#         name (str): The name of the logger.
#         level: The logging level (default is logging.INFO).

#     Returns:
#         logging.Logger: Configured logger instance.
#     """
#     logger = logging.getLogger(name)
#     logger.setLevel(level)

#     # Create console handler and set level
#     ch = logging.StreamHandler()
#     ch.setLevel(level)

#     # Create formatter and add it to the handlers
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     ch.setFormatter(formatter)

#     # Add the handlers to the logger
#     if not logger.hasHandlers():
#         logger.addHandler(ch)

#     return logger