import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_PATH = os.path.join("logs", LOG_FILE)

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


logging.basicConfig(
    filename=LOG_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)