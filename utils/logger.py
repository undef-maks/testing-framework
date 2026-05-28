import logging
import sys
from config.config import settings

def setup_logger():
    logger = logging.getLogger("framework_logger")
    
    if not logger.handlers:
        logger.setLevel(settings.LOG_LEVEL)
        
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger

logger = setup_logger()
