# function to verify if a user exists  - uses tables unique values of username and email and returns the id
def verify_user(username, email):
  from app.functions_sql import run_query
  query = f""" SELECT "USER_ID" FROM USERS
      WHERE "USERNAME" = '{username}'
        OR "EMAIL" = '{email}';"""
    
  ids = run_query(query).mappings().all()

  return ids

  