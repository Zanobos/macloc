from app.api import bp

@bp.route('/walls/<int:wallid>', methods=['GET'])
def get_wall(wallid):
    pass

@bp.route('/walls', methods=['GET'])
def get_walls():
    pass

@bp.route('/walls', methods=['POST'])
def create_wall():
    pass

@bp.route('/walls/<int:wallid>', methods=['PUT'])
def update_wall(wallid):
    pass