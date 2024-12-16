from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/facility')

from app.facility import routes
