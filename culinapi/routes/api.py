from flask import Blueprint
from flask import current_app
from flask_cognito import cognito_auth_required, current_cognito_jwt

from ..extensions import db
from ..models.models import User

api = Blueprint("api", __name__)


@api.route("/user/<name>")
@cognito_auth_required
def create_user(name):
    current_app.logger.info("looked for user")
    # user = User.query.filter_by(name="Anthony").first()
    print(current_cognito_jwt)
    print("hahshshhas")
    current_app.logger.info("looked for user")
    return {"user": name}