from flask import request
from markupsafe import escape
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

from app.auth import bp
from app.auth.functions import authenicate_user, build_authed_user
from app.extensions import jwt, cors

from config import Config


# Authenicate a user for log in
@bp.route('/login', methods=['POST'])
# @cross_origin()
def user_login(config_class=Config):
  if request.method == 'POST':
    # authenticate user to get the user_id
    user_id = authenicate_user(request.headers['USERNAME'], request.headers['PASSWORD'], config_class)
    
    if user_id == 'Error':
      return {'message': 'Unable to authenticate user based on username/email and password combination'}, 401
    
    access_token = create_access_token(identity=user_id)
    user = build_authed_user(user_id)

    return {'message': 'Login Success', 'access_token': access_token, 'user': user[0]}

# JWT protected route for to get an id
@bp.route('/user', methods=['POST'])
@jwt_required()
def get_user(config_class=Config):
  if request.method == 'POST':
    # print(cors)
    user_id = get_jwt_identity()

    # build user
    user = build_authed_user(user_id)

    if len(user) != 1:
      return "Unable to retrieve user", 500

    return user[0]

# Reset a password

