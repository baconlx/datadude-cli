import logging

class Log():
    @staticmethod
    def init(level=logging.INFO):
        logging.basicConfig(encoding='utf-8', level=level)

    @staticmethod
    def debug(value):
        logging.debug(" " + value)

    @staticmethod
    def info(value):
        logging.info(" " + value)

    @staticmethod
    def warning(value):
        logging.warning(" " + value)

    @staticmethod
    def error(value):
        logging.error(" " + value)