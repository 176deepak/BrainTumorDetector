import os
import logging
from datetime import datetime

LOGS_DIR = os.path.join(os.getcwd(), 'LOGS')

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

log_filename = f"{datetime.now().strftime('%Y_%m_%d %H_%M_%S')}.log"
LOGS_PATH = os.path.join(LOGS_DIR, log_filename)

with open(LOGS_PATH, 'w') as f:
    pass

logging.basicConfig(
    filename=LOGS_PATH, 
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)