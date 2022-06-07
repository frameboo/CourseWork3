import logging


def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    logger_api = logging.getLogger("basic")
    logger_api.setLevel("DEBUG")

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("logs/basic.txt")

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    console_handler_api = logging.StreamHandler()
    file_handler_api = logging.FileHandler("logs/api.txt")

    logger.addHandler(file_handler_api)
    logger.addHandler(console_handler_api)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    file_handler.setFormatter(formatter)
    file_handler_api.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    console_handler_api.setFormatter(formatter)

