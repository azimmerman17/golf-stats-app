from app.functions_sql import run_query
from app.extensions import to_dict

# authenicate a user
def authenicate_user(user_name, password, config):
  from app.functions.functions_auth import hash_value
  # get user_id and salt from user_name data
  id_query = f"""SELECT USERS."USER_ID", AUTH."SALT", AUTH."PASSWORD_HASH" FROM USERS , USER_AUTH AUTH 
  WHERE USERS."USER_ID" = AUTH."USER_ID"
    AND AUTH."ACTIVE" = 'A'
    AND (USERS."USERNAME" = '{user_name}'
      OR USERS."EMAIL" = '{user_name}');"""

  try:
    res = run_query(id_query).mappings().all()
    res = to_dict(res)

    # can only return 1 valid row, if multiple or 0 rows are returned, cannot authenticate user
    if len(res) != 1:
      return 'Error'
    
    user_salt = res[0]['SALT']
    user_id = res[0]['USER_ID']
    password_hash = res[0]['PASSWORD_HASH']

    # hash inputted password
    hased_password = hash_value(password + user_salt) + config.PEPPER

    if hased_password != password_hash:
      return 'Error'
    
  except Exception as error:
    print('ERROR', error)
    return 'Error'

  return user_id

def build_authed_user(user_id):
  print(user_id)
  user_query = f"""SELECT "USER_ID", "USERNAME", "FIRST_NAME", "LAST_NAME", "EMAIL", "USER_GENDER", "DOB", "PLAYER_TYPE", "HOME_FACILITY", "NATIONALITY", "UNITS", "ROLE" FROM USERS
    WHERE "USER_ID" = {user_id};"""

  res = run_query(user_query).mappings().all()
  res = to_dict(res)

  return res