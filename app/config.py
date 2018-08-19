import os

class Config(object):
    VAR = os.environ.get('VAR') or 'EXAMPLE_VAR'