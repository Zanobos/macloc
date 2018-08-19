from app import app, db

def make_shell_context():
    return {'db': db}