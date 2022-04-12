import configparser

class Config:
    config = None

    @staticmethod
    def load(filepath):
        Config.config = configparser.ConfigParser()
        Config.config.read(filepath)

    @staticmethod
    def get(section, key):
        return Config.config.get(section, key)