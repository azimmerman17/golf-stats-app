
# run a query
def run_query(query):
  from app.extensions import Engine, db
  conn = Engine.connect()

  conn.begin()
  # run the query
  try:
    conn.execute(db.text(query))
  except Exception as error:
    print('Exception', error)
    conn.rollback()

  print('SQL QUERY:', query)
  conn.commit()
  

# build a select query


# build a insert query
def build_insert(data, keys, table):
  values = ''

  i = 0 
  for key in keys:
    if data[key] is None:
      values = values + f"{ ',' if i != 0 else ''} null"
    else:
      values = values + f"{ ',' if i != 0 else ''} '{data[key]}'"
    i += 1
  
  query = f"""INSERT INTO {table} ("{'", "'.join(keys)}")
    VALUES ({values})"""

  return query

# validate inserted data
def validate_insert_data(data, keys, not_null):
  for key in keys:
    # if key is "not null" and does not exist raise error
    if key not in data.keys() and key in not_null:
      print(f'Not null key, {key}, is not defined')
      raise ValueError(f'Not null key, {key}, is not defined')
    elif key not in data.keys():
      if key == 'METERS' and 'YARDS' in data.keys():
        data[key] = int(round(data['YARDS'] / 1.09361, 0))
      elif key == 'YARDS' and 'METERS' in data.keys():
        data[key] = int(round(data['METERS'] * 1.09361, 0))
      else:
        data[key] = None
  
  return data



# build an update query


# build a delete query