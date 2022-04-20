from flask import Blueprint
from flask import current_app

from ..extensions import db
from ..models.models import User

api = Blueprint('api', __name__)

@api.route('/user/<name>')
def create_user(name):
    current_app.logger.info("looked for user")
    # user = User.query.filter_by(name='Anthony').first()
    current_app.logger.info("looked for user")
    return {'user': name}