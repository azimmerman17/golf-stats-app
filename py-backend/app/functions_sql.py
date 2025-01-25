from datetime import datetime

# run a query
def run_query(query, conn=None):
  from app.extensions import db, Engine
  flag = 0
  if conn == None:
    conn = Engine.connect()
    conn.begin()
    flag = 1

  # run the query
  try:
    result = conn.execute(db.text(query))
  except Exception as error:
    print('Exception', error)
    conn.rollback()
    conn.close()
    return error

  print('SQL QUERY:', query)
  if flag == 1:
    conn.commit()
    conn.close()

  return result

# check if connection is open
def check_conn(conn):
  try:
    conn.info
  except Exception as error:
    print(error)
    return 'error'
  
  return 'continue'


# build a select query


# build a insert query
def build_insert(data, keys, table, returning=None):
  values = ''

  i = 0 
  for key in keys:
    if key in ['NAME', 'ADDRESS', 'CITY' 'ARCHITECT']:
      data[key] = data[key].replace("'", "''") if data[key] != None else None

    if data[key] is None:
      values = values + f"{ ',' if i != 0 else ''} null"
    else:
      values = values + f"{ ',' if i != 0 else ''} '{data[key]}'"
    i += 1
  
  query = f"""INSERT INTO {table} ("{'", "'.join(keys)}")
    VALUES ({values})
  {f'RETURNING {returning}' if returning != None else ''}"""

  return query

# validate inserted data
def validate_insert_data(data, keys, not_null):
  for key in keys:
    # if key is "not null" and does not exist raise error
    if key not in data.keys() and key in not_null:
      print(f'Not null key, {key}, is not defined')
      raise ValueError(f'Not null key, {key}, is not defined')
    elif key not in data.keys() or data[key] == None:
      # FACILITY SCHEMA VALIDATION
      if key == 'METERS' and 'YARDS' in data.keys():
        data[key] = int(round(data['YARDS'] / 1.09361, 0))
      elif key == 'YARDS' and 'METERS' in data.keys():
        data[key] = int(round(data['METERS'] * 1.09361, 0))
      elif key == 'EFFECTIVE_DATE':
        data[key] = datetime.today().strftime('%m-%d-%Y')
      # USER SCHEMA VALIDATION
      elif key == 'USER_GENDER':
        if key not in data.keys():
          data[key] = 'P'
        elif data[key] not in ['M','F','N','P']:
          data[key] = 'P'
      elif  key == 'PLAYER_TYPE':
        if key not in data.keys():
          data[key] = 'A'
        elif data[key] not in ['A','C','P','TP']:
          data[key] = 'A'
      elif  key == 'UNITS':
        if key not in data.keys():
          data[key] = 'Y'
        elif data[key] not in ['Y','M']:
          data[key] = 'Y'
      elif  key == 'ROLE':
          data[key] = 'basic'
      else:
        data[key] = None
  return data

# build an update query
def build_update(data, table, where=None):
  values = ''
  for key in data.keys():
    values = f"""{values}{', ' if values != '' else ' '}"{key}"='{data[key]}'"""

  query = f"""UPDATE {table}
    SET {values}
    {'WHERE' if where != None else ''} {where}"""
  
  return query

# build a delete query