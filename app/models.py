from app import db
from flask import url_for

class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page, **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page, **kwargs)
                        if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page, **kwargs)
                        if resources.has_prev else None
            }
        }
        return data

class Wall(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float)
    width = db.Column(db.Float)
    holds = db.relationship('Hold', backref='mounted_on', lazy='dynamic')

    def __repr__(self):
        return '<Wall {}, h={}, w={}>' .format(self.id, self.height, self.width)

    def to_dict(self):
        data = {
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return data

    def from_dict(self, data):
        for field in ['height', 'width']:
            setattr(self, field, data[field])

class User(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    nickname = db.Column(db.String(20), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    climbs = db.relationship('Climb', backref='climber', lazy='dynamic')

    def __repr__(self):
        return '<User {} ({})>'.format(self.name, self.nickname)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'email': self.email,
            'height': self.height,
            'weight': self.weight
        }
        return data

    def from_dict(self, data):
        for field in ['name', 'nickname', 'email', 'height', 'weight']:
            setattr(self, field, data[field])

#Remember, user can be referenced with relationship, but
# holds and walls must be copied because they can change
class Climb(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Climb {}, grade={}>'.format(self.id, self.grade)

    def to_dict(self):
        data = {
            'id': self.id,
            'grade': self.grade
        }
        return data

    def from_dict(self, data):
        for field in ['grade']:
            setattr(self, field, data[field])

class Hold(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dist_from_sx = db.Column(db.Float)
    dist_from_bot = db.Column(db.Float)
    holdType = db.Column(db.String(30))
    wall_id = db.Column(db.Integer, db.ForeignKey('wall.id'))

    def __repr__(self):
        return '<Hold {} ({},{}) t={}>'.format(self.id, self.dist_from_sx, \
                self.dist_from_bot, self.holdType)

    def to_dict(self):
        data = {
            'id': self.id,
            'dist_from_sx': self.dist_from_sx,
            'dist_from_bot': self.dist_from_bot,
            'holdType': self.holdType
        }
        return data

    def from_dict(self, data):
        for field in ['dist_from_sx', 'dist_from_bot', 'holdType']:
            setattr(self, field, data[field])
