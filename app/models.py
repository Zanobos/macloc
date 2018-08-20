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

# Remember, user can be referenced with relationship, but
# holds and walls must be copied because they can change
# For this reason I store wall information as attributes
class Climb(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    historic_wall = db.relationship('HistoricWall', uselist=False, backref='used_on')

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

class Hold(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    can_id = db.Column(db.Integer)
    dist_from_sx = db.Column(db.Float)
    dist_from_bot = db.Column(db.Float)
    holdType = db.Column(db.String(30))
    wall_id = db.Column(db.Integer, db.ForeignKey('wall.id'))

    def __repr__(self):
        return '<Hold {}, can_id={} ({},{}) t={}>'.format(self.id, self.can_id, self.dist_from_sx, \
                self.dist_from_bot, self.holdType)

    def to_dict(self):
        data = {
            'id': self.id,
            'can_id': self.can_id,
            'dist_from_sx': self.dist_from_sx,
            'dist_from_bot': self.dist_from_bot,
            'holdType': self.holdType
        }
        return data

    def from_dict(self, data):
        for field in ['can_id', 'dist_from_sx', 'dist_from_bot', 'holdType']:
            setattr(self, field, data[field])

    def to_historic_hold(self):
        hh = HistoricHold()
        return hh.from_dict(self.to_dict())

class HistoricWall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float)
    width = db.Column(db.Float)
    holds = db.relationship('HistoricHold', backref='mounted_on', lazy='dynamic')
    climb_id = db.Column(db.Integer, db.ForeignKey('climb.id'))

    def __repr__(self):
        return '<HistoricWall {}, h={}, w={}>' .format(self.id, self.height, self.width)

    def to_dict(self):
        data = {
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return data

class HistoricHold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    can_id = db.Column(db.Integer)
    dist_from_sx = db.Column(db.Float)
    dist_from_bot = db.Column(db.Float)
    holdType = db.Column(db.String(30))
    wall_id = db.Column(db.Integer, db.ForeignKey('historic_wall.id'))
    records = db.relationship('Record', backref='of_hold', lazy='dynamic')

    def __repr__(self):
        return '<HistoricHold {}, can_id={} ({},{}) t={}>'.format(self.id, self.can_id, \
                self.dist_from_sx, self.dist_from_bot, self.holdType)

    def to_dict(self):
        data = {
            'id': self.id,
            'can_id': self.can_id,
            'dist_from_sx': self.dist_from_sx,
            'dist_from_bot': self.dist_from_bot,
            'holdType': self.holdType
        }
        return data

    def from_dict(self, data):
        for field in ['can_id', 'dist_from_sx', 'dist_from_bot', 'holdType']:
            setattr(self, field, data[field])

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    can_id = db.Column(db.Integer)
    #missing the three forces
    hold_id = db.Column(db.Integer, db.ForeignKey('historic_hold.id'))
    #missing timestamp

    def __repr__(self):
        return '<Record {}, can_id={}>'.format(self.id, self.can_id)

    def to_dict(self):
        data = {
            'id': self.id,
            'can_id': self.can_id,
            'hold_id': self.hold_id
        }
        return data

    def to_ws_dict(self):
        pass
