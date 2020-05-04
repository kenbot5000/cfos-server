class Config(object) :
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config) :
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@127.0.0.1:5432/cfos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '@z4-ci8!v1ty1ais#uy@du=bgl^@d2-13-$_5u3qzns@5^t79z'

