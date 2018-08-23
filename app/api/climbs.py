from app import db, socketio
from app.api import bp
from app.models import Climb, User, Wall
from app.utils.worker import WorkerThread
from app.api.errors import bad_request, unauthorized
from flask import request, jsonify, url_for

#Ok for dev environment and in order to save on resources
worker_thread = None

@bp.route('/climbs/<int:climbid>', methods=['GET'])
def get_climb(climbid):
    return jsonify(Climb.query.get_or_404(climbid).to_dict())

@bp.route('/climbs', methods=['GET'])
def get_climbs():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 5, type=int), 20)
    user_id = request.args.get('user_id', None, type=int)
    query = Climb.query if user_id is None else Climb.query.filter(Climb.user_id == user_id)
    data = Climb.to_collection_dict(query, page, per_page, 'api.get_climbs')
    return jsonify(data)

@bp.route('/climbs', methods=['POST'])
def create_climb():
    #Create a new Climb, freezing wall and holds status
    user_id = request.args.get('user_id', None, type=int)
    wall_id = request.args.get('wall_id', None, type=int)
    if user_id is None or wall_id is None:
        return bad_request('must include user_id and wall_id')
    user = User.query.get_or_404(user_id)
    wall = Wall.query.get_or_404(wall_id)
    historic_wall = wall.to_historic_wall()
    climb = Climb(climber=user, on_wall=historic_wall, status='ready')
    db.session.add(climb)
    db.session.commit()
    response = jsonify(climb.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_climb', climbid=climb.id)
    return response

@bp.route('/climbs/<int:climbid>', methods=['PUT'])
def update_climb(climbid):
    climb = Climb.query.get_or_404(climbid)
    data = request.get_json() or {}
    global worker_thread
    if data['status'] == 'start':
        climb.start_climb()
        worker_thread = WorkerThread()
        worker_thread.start()
    if data['status'] == 'end':
        climb.end_climb()
        worker_thread.join()
    db.session.commit()
    return jsonify(climb.to_dict())

@bp.route('/climbs/<int:climbid>', methods=['DELETE'])
def delete_climb(climbid):
    climb = Climb.query.get_or_404(climbid)
    db.session.delete(climb)
    db.session.commit()
    return jsonify(climb.to_dict())

@bp.route('/climbs', methods=['DELETE'])
def delete_climbs():
    auth = request.args.get('auth', 'notme', type=str)
    if auth != 'me':
        return unauthorized('wrong auth')
    number_items = db.session.query(Climb).delete()
    db.session.commit()
    return jsonify(number_items)

@socketio.on('connect', namespace='/api/climbs')
def ws_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/api/climbs')
def ws_disconnect():
    print('Client disconnected')

@socketio.on('json', namespace='/api/climbs')
def handle_json(json):
    print('Received:', json)
