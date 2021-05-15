import os

_env = os.getenv("FLASK_ENV", os.getenv("ENV", "dev")).lower()
if _env in ["prod", "production"]:
    FLASK_ENV = "prod"

elif _env in ["dev", "development"]:
    FLASK_ENV = "dev"
else:
    FLASK_ENV = _env


class BaseConfig():
    APP_ROOTDIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = bool(os.getenv("DEBUG", False))


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = False


class ProductionConfig(BaseConfig):
    DEBUG = False


Config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)[FLASK_ENV]
