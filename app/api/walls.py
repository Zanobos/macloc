from app.api import bp

@bp.route('/walls/<int:id>', methods=['GET'])
def get_wall(id):
    pass

@bp.route('/walls', methods=['GET'])
def get_walls(id):
    pass

@bp.route('/walls', methods=['POST'])
def create_wall(id):
    pass

@bp.route('/walls/<int:id>', methods=['PUT'])
def update_wall(id):
    pass