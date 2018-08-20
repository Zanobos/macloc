from app import create_app, db
from app.models import Wall, Climb, User, Hold

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Wall': Wall, 'Climb': Climb, 'User': User, 'Hold': Hold}
