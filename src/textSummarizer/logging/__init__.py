import os
import sys
import logging

from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH ,
    #format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    format = logging_str,
    level = logging.INFO,
    # handler=[
    #     logging.FileHandler(LOG_FILE_PATH),
    #     logging.StreamHandler(sys.stdout)
    # ]
)

logger = logging.getLogger("textSummarizerLogger")
