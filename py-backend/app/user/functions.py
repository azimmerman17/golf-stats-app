# function to verify if a user exists  - uses tables unique values of username and email and returns the id
def verify_user(username, email):
  from app.functions_sql import run_query
  query = f""" SELECT "USER_ID" FROM USERS
      WHERE "USERNAME" = '{username}'
        OR "EMAIL" = '{email}';"""
    
  ids = run_query(query).mappings().all()

  return ids

# vailidates datea the user is updating
def validate_user_update(data, user_id):
  from datetime import datetime, date
  from app.functions_sql import run_query, validate_query
  for key in data.keys():
    if key == 'EMAIL' or key == 'USERNAME':
      res = validate_query(key, data[key], 'USERS', True, user_id) 
      if res != []:
        return {'Error': f'The value for {key} is not valid'}
    elif key == 'HOME_FACILITY':
      res = validate_query('FACILITY_ID', data[key], 'FACILITY') 
      if res == [] or res == 'Error':
        return {'Error': 'The home facility does not exists'}
    elif key == 'DOB':
      new_date = data[key].split(',')[0]
      if datetime.strptime(new_date, '%m/%d/%Y').date() > datetime.now().date():
        return {'Error': 'Invalid Date of Birth, it cannot be future dated'}
    elif (key == "PLAYER_TYPE" and data[key] not in ['A','C','P','TP']) or (key == "USER_GENDER" and data[key] not in ['M','F','N','P']) or (key == "UNITS" and data[key] not in ['M','Y']):
      return  {'Error': f'Invalid value for {key}'}
  return {'data': data, 'Error': None}