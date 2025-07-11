import logging

formatter = "%(process)d - %(asctime)s - %(name)s - NotesManager - %(pathname)s - " \
                "%(module)s - %(funcName)s - %(lineno)d- %(levelname)s - %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("employees.log")
file_handler.setFormatter(logging.Formatter(formatter))
logger.addHandler(file_handler)