from flask import request
from markupsafe import escape
from flask_jwt_extended import create_access_token
from datetime import datetime, date, timedelta


from app.user import bp
from app.user.functions import verify_user, validate_user_update
from app.extensions import to_dict, Engine
from app.functions_sql import run_query, build_insert, validate_insert_data, check_conn, build_update, validate_query
from app.functions.functions_auth import hash_value, generate_salt, encrypt_data
from app.auth.functions import authenicate_user, build_authed_user

from app.models.user import USERS, user_keys, user_not_null
from app.models.user_auth import USER_AUTH, auth_keys
from app.models.facility import validate_facility 

from config import Config

# GET ALL USERS OR CREATE A NEW USER
@bp.route('/', methods=['GET', 'POST'])
def users_all(config_class=Config):
  if request.method == 'GET':
    select_keys = '"USERNAME", "FIRST_NAME", "LAST_NAME", "EMAIL", "USER_GENDER", "PLAYER_TYPE", "NATIONALITY"'
    query = f"""SELECT {select_keys} FROM USERS
      ORDER BY "LAST_NAME", "FIRST_NAME";"""

    try:
      mapping = run_query(query).mappings().all()
      res = to_dict(mapping)
      return res, 200
    except Exception:
      return 'Error loading all users', 500
  elif request.method ==  'POST':
    conn = Engine.connect()
    conn.begin()

    # define data from request
    data = request.json
    print(data)

    # verify a new user
    user_new = verify_user(data['USERNAME'], data['EMAIL'])
    if len(user_new) > 0:
      return 'ERROR - Cannot create new user, email or username already exist', 400

    # validate the user data and build query for insert
    user = validate_insert_data(data, user_keys, user_not_null)
    user['HOME_FACILITY'] = validate_facility(user['HOME_FACILITY'])
    if user['HOME_FACILITY'].isdigit() == False:
      return 'Error validating Home Course', 400
    
    user_query = build_insert(user, user_keys, 'USERS','"USER_ID"')
    user_id = run_query(user_query, conn).mappings().all()
    user_id = user_id[0]['USER_ID']
    # user_id = 8 # testing

    if check_conn(conn) == 'error':
      return 'Error creating user: Error adding data to USERS table', 400

    # create authentication row
    auth_dict = {
      'USER_ID': user_id,
      'SALT': generate_salt().decode(),  # randomly generated and encrytped at row creation
      'GUID_TOKEN': encrypt_data(generate_salt(), config_class).decode(),   # randomly generated and encrytped at row creation
    }

    auth_dict['PASSWORD_HASH'] =  hash_value(user['PASSWORD'] + auth_dict['SALT']) + config_class.PEPPER  # hashed value passed in by the request

    auth_query = build_insert(auth_dict, auth_keys, 'USER_AUTH')
    run_query(auth_query, conn)

    if check_conn(conn) == 'error':
      return 'Error creating user: Error adding data to USERS table', 400

    conn.commit()
    conn.close()

    access_token = create_access_token(identity=user_id)
    user = build_authed_user(user_id)
    print(user)

    return {'message': 'User Successfully Created', 'access_token': access_token, 'user': user[0]}, 201


# SINGLE USER - GET a single User, POST an updated password record UPDATE user profile information, or DELETE a user
@bp.route('/<int:user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_single(user_id, config_class=Config):
  if request.method == 'GET':
    query = f"""SELECT "USER_ID", "USERNAME", "FIRST_NAME", "LAST_NAME", "EMAIL", "USER_GENDER", "NATIONALITY", "PLAYER_TYPE", "UNITS", "HOME_FACILITY", "DOB" FROM USERS
      WHERE "USER_ID" = '{escape(user_id)}';"""

    mapping = run_query(query).mappings().all()
    user = to_dict(mapping)

    if len(user) != 1:
      return 'Error - Unable to load the user', 400

    return user
  elif request.method == 'POST':
    # validate user
    res = validate_query('USER_ID', user_id, 'USERS')
    if res == 'Error':
      return {'message': 'Error retrieving User'}, 500
    if len(res) != 1:
      return {'message': 'User not found'}, 404

    # create new password dict
    auth_dict = {
      'USER_ID': user_id,
      'SALT': generate_salt().decode(),  # randomly generated and encrytped at row creation
      'GUID_TOKEN': encrypt_data(generate_salt(), config_class).decode(),   # randomly generated and encrytped at row creation
    }

    auth_dict['PASSWORD_HASH'] =  hash_value(request.json['PASSWORD'] + auth_dict['SALT']) + config_class.PEPPER  # hashed value passed in by the request

    # validate new password cant be the same as the last 5 or last year - Need additional thought on this one
    # check_password = f"""SELECT AUTH."SALT" FROM USER_AUTH AUTH
    #   WHERE AUTH."USER_ID" IN (SELECT AUTH1."USER_ID" FROM USER_AUTH AUTH1
    #         WHERE AUTH1."USER_ID" = AUTH."USER_ID"
    #         ORDER BY AUTH1."UPDATED_AT" DESC
    #         LIMIT 5) 
    #       OR AUTH."UPDATED_AT" > ((NOW()) - INTERVAL '1 YEAR');"""
    # res = run_query(check_password).mappings().all()
    # for row in res:
    #   if hash_value(request.json['PASSWORD'] + row['SALT']) + config_class.PEPPER == auth_dict['PASSWORD_HASH']:
    #     return "Invalid Password, cannot be one of your last 5 passwords, or a password used in the last year", 400
    # print("valid new password")

    # create new password record
    conn = Engine.connect()
    conn.begin()

    new_password = build_insert(auth_dict, auth_keys, 'USER_AUTH', '"AUTH_ID"')
    auth_id = run_query(new_password, conn).mappings().all()
    auth_id = auth_id[0]['AUTH_ID']

    if check_conn(conn) == 'error':
      return {'message': 'Error creating new password: Error adding data to USERS table'}, 400
    
    # inactivate old rows
    update_where = f""" AUTH."USER_ID" = {user_id}
      AND AUTH."AUTH_ID" = (SELECT MAX(AUTH1."AUTH_ID") FROM USER_AUTH AUTH1 
          WHERE AUTH1."USER_ID" = AUTH."USER_ID"
            AND AUTH1."AUTH_ID" < {auth_id})"""
    inactivate_query = build_update({'ACTIVE': 'I'}, 'USER_AUTH AUTH', update_where)

    run_query(inactivate_query, conn)

    if check_conn(conn) == 'error':
      return {'message': 'Error updating password: Error adding data to USERS_AUTH table'}, 400

    conn.commit()
    conn.close()

    return {'message': 'Password Successfully updated'}, 200
  elif request.method == 'PUT':
    if request.json == {}:
      print('No Data')
      return {'message': 'No Data to Update'}, 400

    # validate user
    res = validate_query('USER_ID', user_id, 'USERS')
    if res == 'Error':
      return {'message': 'Error retrieving User'},  500
    if len(res) != 1:
            return {'message': 'User not found'},  404

    # validate data for update
    data = validate_user_update(request.json, user_id)
    # return
    if data['Error'] != None:
      return data['Error']
    else:
      data = data['data']

    # create connection 
    conn = Engine.connect()
    conn.begin()

    #build and run update
    where_clause = f'"USER_ID" = {escape(user_id)}'
    update_query = build_update(request.json, 'USERS', where_clause)
    run_query(update_query, conn)
    if check_conn(conn) == 'error':
      return {'message': 'Error updating User'}, 400

    conn.commit()
    conn.close()

    user = build_authed_user(user_id)

    return {'message': 'User updated successfully', 'user': user[0]}, 200
  elif request.method == 'DELETE':
    # create delete query
    query = f"""
    DELETE FROM USERS
	  WHERE "USER_ID" = {escape(user_id)};
    """

    conn = Engine.connect()
    conn.begin()

    # run delete query
    run_query(query, conn)
    if check_conn(conn) == 'error':
      return f'Error deleting user', 400

    conn.commit()
    conn.close()

    return 'User Data Deleted.'
  
# ALL USERS FROM A SINGLE FACILITY
@bp.route('/facility/<int:facility_id>', methods=['GET'])
def user_at_facility(facility_id, config_class=Config):
  if request.method == 'GET':
    select_keys = '"USERNAME", "FIRST_NAME", "LAST_NAME", "USER_GENDER", "PLAYER_TYPE", "NATIONALITY"'
    query = f"""SELECT {select_keys} FROM USERS
      WHERE "HOME_FACILITY" = {facility_id}
      ORDER BY "LAST_NAME", "FIRST_NAME";"""

    try:
      mapping = run_query(query).mappings().all()
      res = to_dict(mapping)
      return res, 200
    except Exception:
      return 'Error loading all users', 500
