from flask import Blueprint

bp = Blueprint('api', __name__)

from . import walls, users, climbs, holds
