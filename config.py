
class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "Culosucio"

    DB_NAME = "cicd"
    DB_USERNAME = "root"
    DB_PASSWORD = "Culosucio"

    UPLOADS = "/home/lucasca95/FlaskUploads"

    SESSION_COOKIE_CACHE = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Culosucio@localhost/cicd'

class DevelopmentConfig(Config):
    DEBUG = False
    SESSION_COOKIE_CACHE = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

class TestingConfig(Config):
    TESTING=True
    SESSION_COOKIE_CACHE = False
