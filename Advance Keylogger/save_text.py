import logging

def savText(message):
    log_dir = ""
    logging.basicConfig(filename=(log_dir + "mamoon.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    logging.info(str(message))
