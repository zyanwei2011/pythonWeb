from app.config.base_config import BaseConfig


class DevConfig(BaseConfig):
    DEBUG = True


config = DevConfig()
