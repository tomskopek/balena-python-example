#! /usr/bin/python3
import time
import schedule
import sys
import numpy as np
import threading
import logging
from datetime import datetime

while True:
    try:
        logging.info('Hello world')
        time.sleep(60 * 5) # every 5 minutes (60s = 1m * 5)
    except (KeyboardInterrupt, SystemExit):
        logging.info('Shut down')
        sys.exit()
