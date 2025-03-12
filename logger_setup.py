import logging

def setup_logger():
    logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s")
    

    return logging.getLogger("logger")