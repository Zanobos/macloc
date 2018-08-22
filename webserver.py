from app import create_app, db, socketio
from app.models import Wall, Climb, User, Hold, HistoricHold, HistoricWall, Record
from app.utils.worker import WorkerThread
from app.utils.rabbitmq import Publisher, Receiver

app = create_app()

if __name__ == '__main__':
    socketio.run(app)

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Wall': Wall,
        'Climb': Climb,
        'User': User,
        'Hold': Hold,
        'HistoricWall': HistoricWall,
        'HistoricHold': HistoricHold,
        'Record': Record,
        'WorkerThread': WorkerThread,
        'Publisher': Publisher,
        'Receiver': Receiver
        }
