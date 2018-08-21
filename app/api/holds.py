from app import db
from app.api import bp
from app.models import Hold
from app.api.errors import bad_request, unauthorized
from flask import request, jsonify, url_for

@bp.route('/holds/<int:holdid>', methods=['GET'])
def get_hold(holdid):
    return jsonify(Hold.query.get_or_404(holdid).to_dict())

@bp.route('/holds', methods=['GET'])
def get_holds():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 5, type=int), 20)
    wall_id = request.args.get('wall_id', None, type=int)
    query = Hold.query if wall_id is None else Hold.query.filter(Hold.wall_id == wall_id)
    data = Hold.to_collection_dict(query, page, per_page, 'api.get_holds')
    return jsonify(data)

@bp.route('/holds', methods=['POST'])
def create_hold():
    data = request.get_json() or {}
    if 'dist_from_sx' not in data or 'dist_from_bot' not in data:
        return bad_request('must include dist_from_sx and dist_from_bot')
#    wall_id = request.args.get('wall_id', None, type=int)
#    wall = Wall.query.get(wall_id) if wall_id is not None else None
#    hold = Hold(mounted_on=wall)
    hold = Hold()
    hold.from_dict(data)
    db.session.add(hold)
    db.session.commit()
    response = jsonify(hold.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_hold', holdid=hold.id)
    return response

@bp.route('/holds/<int:holdid>', methods=['PUT'])
def update_hold(holdid):
    hold = Hold.query.get_or_404(holdid)
    data = request.get_json() or {}
    hold.from_dict(data)
    db.session.commit()
    return jsonify(hold.to_dict())

@bp.route('/holds/<int:holdid>', methods=['DELETE'])
def delete_hold(holdid):
    hold = Hold.query.get_or_404(holdid)
    db.session.delete(hold)
    db.session.commit()
    return jsonify(hold.to_dict())

@bp.route('/holds', methods=['DELETE'])
def delete_holds():
    auth = request.args.get('auth', 'notme', type=str)
    if auth != 'me':
        return unauthorized('wrong auth')
    number_items = db.session.query(Hold).delete()
    db.session.commit()
    return jsonify(number_items)
