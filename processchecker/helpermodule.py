import argparse, sys, logging, os
from logging.handlers import RotatingFileHandler
 
if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_formatter = logging.Formatter('%(message)s')
file_handler = RotatingFileHandler('logs/processchecker.log', maxBytes=2000, backupCount=10)
file_handler.setFormatter(file_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def logInfo(text_to_display):
    logger.info('{}'.format(text_to_display))

def check_positive(value):
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive numeric value" % value)
        return ivalue
    except:
        raise argparse.ArgumentTypeError("%s is an invalid numeric value" % value)
    