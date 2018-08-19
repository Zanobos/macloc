from app import db

class Wall(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    def __repr__(self):
        return '<Wall {}, h={}, w={}>' .format(self.id, self.height, self.weight)
        