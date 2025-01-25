from flask import request
from markupsafe import escape

from app.user import bp
from app.user.functions import verify_user
from app.extensions import to_dict, Engine
from app.functions_sql import run_query, build_insert, validate_insert_data, check_conn, build_update
from app.functions.functions_auth import hash_value, generate_salt, encrypt_data
from app.models.user import USERS, user_keys, user_not_null
from app.models.user_auth import USER_AUTH, auth_keys
from app.models.facility import validate_facility 

from config import Config

# GET ALL USERS OR CREATE A NEW USER
@bp.route('/', methods=['GET', 'POST'])
def users_all(config_class=Config):
  if request.method == 'GET':
    select_keys = '"USERNAME", "FIRST_NAME", "LAST_NAME", "GENDER", "PLAYER_TYPE", "NATIONALITY"'
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
      'GUID_TOKEN': encrypt_data(generate_salt(), Config).decode(),   # randomly generated and encrytped at row creation
    }

    auth_dict['PASSWORD_HASH'] =  hash_value(user['PASSWORD'] + auth_dict['SALT']) + Config.PEPPER  # hashed value passed in by the request

    auth_query = build_insert(auth_dict, auth_keys, 'USER_AUTH')
    run_query(auth_query, conn)

    if check_conn(conn) == 'error':
      return 'Error creating user: Error adding data to USERS table', 400

    conn.commit()
    conn.close()

    return 'User successfully Added'

# SINGLE USER
  # GET
  # CREATE
  # UPDATE
    # PROFILE
    # PASSWORD
    # PSSWORD RESET
  # DELETE 

# ALL USERS FROM A SINGLE FACILITY



