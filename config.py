import os

basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.abspath(os.path.join('H:\Tutorials\Minor Project\part1\Essentia_data'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shivam118!'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MIRmL_MAIL_SUBJECT_PREFIX = '[MIRmL]'
    MIRmL_MAIL_SENDER = 'MIRmL Admin <shivam.srivastava31093@gmail.com>'
    MIRmL_ADMIN = os.environ.get('MIRmL_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
