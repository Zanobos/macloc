from app import db

class Wall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float)
    width = db.Column(db.Float)

    def __repr__(self):
        return '<Wall {}, h={}, w={}>' .format(self.id, self.height, self.weight)

    def to_dict(self):
        data = {
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return data
