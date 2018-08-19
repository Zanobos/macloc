import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    VAR = os.environ.get('VAR') or 'EXAMPLE_VAR'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqllite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
