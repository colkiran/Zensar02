
import logging

# create a custom logger
logger = logging.getLogger(__name__)


# create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("mylog2.log")
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

#Create formatters
c_format = logging.Formatter("%(name)s  -   %(levelname)s   -   %(message)s")
f_format = logging.Formatter("%(asctime)s   -   %(name)s    -   %(levelname)s   -   %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("This is a warning message")
logger.error("This is an error message")

