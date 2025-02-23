# this bluebrint controls db trasactions with the Facility Models
from flask import request
from markupsafe import escape

from app.facility import bp
from app.extensions import to_dict, Engine
from app.models.facility import facility_keys, facility_not_null 
from app.models.course import COURSE, course_keys, course_not_null
from app.models.tee import tee_keys, tee_not_null
from app.models.rating import rating_keys, rating_not_null
from app.models.hole import hole_keys, hole_not_null
from app.functions_sql import run_query, build_insert, validate_insert_data, check_conn, build_update
from app.facility.functions import translate_ghin
from config import Config

# GET ALL FACILITIES
@bp.route('/', methods=['GET'])
def facility_all(config_class=Config):
  if request.method == 'GET':
    select_keys = '"FACILITY_ID", "NAME", "HANDLE", "COURSE_COUNT", "ESTABLISHED", "CLASSIFICATION", "CITY", "STATE", "COUNTRY", "GEO_LAT", "GEO_LON"'
    query = f"""SELECT {select_keys} FROM FACILITY
      ORDER BY "NAME", "FACILITY_ID";"""

    try:
      mapping = run_query(query).mappings().all()
      res = to_dict(mapping)
      return res, 200
    except Exception:
      return 'Error loading the facilities', 500

# GET SINGLE FACILITY, POST NEW COURSE TO EXISTING FACILITY, UPDATE FACILITY DATA, DELETE FACILTY AND ALL ITS CHILD DATA
@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def facility_one(id, config_class=Config):
  if request.method == 'GET':
    facility_select_keys = '"FACILITY_ID", "NAME", "HANDLE", "CLASSIFICATION", "COURSE_COUNT", "ESTABLISHED", "WEBSITE", "ADDRESS", "CITY", "STATE", "COUNTRY", "GEO_LAT", "GEO_LON"'
    facility_query = f"""SELECT {facility_select_keys} FROM FACILITY
      WHERE "FACILITY_ID" = '{escape(id)}';"""
    facility_mapping = run_query(facility_query).mappings().all()
    facility = to_dict(facility_mapping)[0]

    course_select_keys = '"COURSE_ID", "FACILITY_ID", "NAME", "HOLE_COUNT", "ESTABLISHED", "ARCHITECT"'
    course_query = f"""SELECT {course_select_keys} FROM COURSE
      WHERE "FACILITY_ID" = {escape(id)};"""

    try:
      course_mapping = run_query(course_query).mappings().all()
      course = to_dict(course_mapping)
    except Exception:
      return 'Error loading facility', 500

    return {
      'FACILITY': facility,
      'COURSES': course
    }, 200
  elif request.method == 'POST':
    # check if facility exists
    facility_query = f"""SELECT * FROM FACILITY
      WHERE "FACILITY_ID" = '{escape(id)}';"""
    
    # run facility query
    try:
      facility_mapping = run_query(facility_query).mappings().all()
      facility = to_dict(facility_mapping)
    except Exception:
      return 'Error retrieving Facility', 500

    # check if there is data returned in facility query
    if len(facility) == 0:
      return 'Facility not found', 404
    else: 
      request.json['OVERRIDE']['FACILITY'] = facility[0]

    # create connection 
    conn = Engine.connect()
    conn.begin()

    # check if data, is a "data dump" from GHIN and translate is to data that can be uploaded
    if request.json['GHIN'] == True:
      data = translate_ghin(request.json)
    
    for n in range(len(data['COURSE'])):
      # Define course and attach the facility id 
      course = data['COURSE'][n]
      course['FACILITY_ID'] = escape(id)

      # validate the course data and build query for insert
      course = validate_insert_data(course, course_keys, course_not_null)
      course_query = build_insert(course, course_keys, 'COURSE')
      run_query(course_query, conn)
      if check_conn(conn) == 'error':
        return f'Error creating facility: Error adding data to COURSE table - COURSE: {course['NAME']}', 400

      # INSERT INTO TEE
      # Loop for the course's list of tee sets
      for m in range(len(course['TEES'])):
        # Define tee and attach the course id 
        tee = course['TEES'][m]
        tee['COURSE_ID'] = course['COURSE_ID']

        # validate the course data and build query for insert
        tee = validate_insert_data(tee, tee_keys, tee_not_null)
        tee_query = build_insert(tee, tee_keys, 'TEE')
        run_query(tee_query, conn)
        if check_conn(conn) == 'error':
          return f'Error creating facility: Error adding data to TEE table - COURSE: {course['NAME']}, TEE: {tee['NAME']}', 400

        # INSERT INTO RATING
        # Loop for the tee set's list of ratings
        for o in range(len(tee['RATINGS'])):
          # Define rating and attach the tee id 
          rating = tee['RATINGS'][o]
          rating['TEE_ID'] = tee['TEE_ID']

          # validate the rating data and build query for insert
          rating = validate_insert_data(rating, rating_keys, rating_not_null)
          rating_query = build_insert(rating, rating_keys, 'RATING')
          run_query(rating_query, conn)
          if check_conn(conn) == 'error':
            return f'Error creating facility: Error adding data to RATING table - COURSE: {course['NAME']}, TEE: {tee['NAME']}, RATING: {rating['NAME']} - {rating['GENDER']}', 400

      
        # INSERT INTO HOLE
        # Loop for the tee set's list of holes
        for p in range(len(tee['HOLES'])):
          # Define hole and attach the tee id 
          hole = tee['HOLES'][p]
          hole['TEE_ID'] = tee['TEE_ID']

          # validate the hole data and build query for insert
          hole = validate_insert_data(hole, hole_keys, hole_not_null)
          hole_query = build_insert(hole, hole_keys, 'HOLE')
          run_query(hole_query, conn)
          if check_conn(conn) == 'error':
            return f'Error creating facility: Error adding data to TEE table - COURSE: {course['NAME']}, TEE: {tee['NAME']}, HOLE: {hole['NUMBER']}', 400

    conn.commit()
    conn.close()

    return 'Course Insert Completed', 201
  elif request.method == 'PUT':
    # check if facility exists
    facility_query = f"""SELECT 'x' FROM FACILITY
      WHERE "FACILITY_ID" = '{escape(id)}';"""
    
    # run query
    try:
      facility_mapping = run_query(facility_query).mappings().all()
      facility = to_dict(facility_mapping)
    except Exception:
      return 'Error retrieving Facility', 500

    # ensure facility exists
    if len(facility) == 0:
      return 'Facility not found', 404
    
    # create connection 
    conn = Engine.connect()
    conn.begin()

    # create and run update query
    where_clause = f'"FACILITY_ID" = {escape(id)}'
    update_query = build_update(request.json, 'FACILITY', where_clause)
    run_query(update_query, conn)
    if check_conn(conn) == 'error':
      return f'Error updating Facility', 400

    conn.commit()
    conn.close()
    return 'Facility successfully updated', 200
  elif request.method == 'DELETE':
    # create delete query
    query = f"""
    DELETE FROM FACILITY
	  WHERE "FACILITY_ID" = {escape(id)};
    """

    conn = Engine.connect()
    conn.begin()

    # run delete query
    run_query(query, conn)
    if check_conn(conn) == 'error':
      return f'Error deleting facility', 400

    conn.commit()
    conn.close()

    return 'Facility and all related Course, Tee, Rating, and Hole Data Deleted.'

# GET ALL COURSES
@bp.route('/course', methods=['GET'])
def course_all(config_class=Config):
  if request.method == 'GET':
    select_keys = 'F."FACILITY_ID", F."NAME", F."HANDLE", F."CLASSIFICATION", F."CITY", F."STATE", F."COUNTRY", F."GEO_LAT", F."GEO_LON", C."COURSE_ID",C."NAME" as "COURSE_NAME",C."HOLE_COUNT",C."ESTABLISHED",C."ARCHITECT"'
    query = f"""SELECT {select_keys} FROM FACILITY F, COURSE C
      WHERE F."FACILITY_ID" = C."FACILITY_ID"
      ORDER BY F."NAME", F."FACILITY_ID", C."NAME",  C."COURSE_ID";"""

    try:
      mapping = run_query(query).mappings().all()
      res = to_dict(mapping)
    except Exception:
      return 'Error loading the courses', 500

    return res, 200

# GET SINGLE COURSE, POST NEW TEE(S) TO EXISTING COURSE, UPDATE COURSE DATA, DELETE COURSE AND ALL ITS CHILD DATA
@bp.route('/course/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def course_single(id, config_class=Config):
  if request.method == 'GET':
    course_select_keys = '"COURSE_ID", "FACILITY_ID", "NAME", "HOLE_COUNT", "ESTABLISHED", "ARCHITECT"'
    course_query = f"""SELECT {course_select_keys} FROM COURSE
      WHERE "COURSE_ID" = {escape(id)};"""
    try:
      course_mapping = run_query(course_query).mappings().all()
      course = to_dict(course_mapping)[0]
    except Exception:
      return 'Error retrieving Course', 500

    # facility
    facility = facility_one(course['FACILITY_ID'])

    for course in facility[0]['COURSES']:
      if course['COURSE_ID'] == id:
        facility[0]['COURSES'] = course
        break
    
    #tees
    tee_select_keys = '"TEE_ID", "COURSE_ID", "NAME", "YARDS", "METERS", "HOLE_COUNT"'
    tees_query = f"""SELECT {tee_select_keys} FROM TEE
      WHERE "COURSE_ID" = {escape(id)}
      ORDER BY "YARDS" DESC;"""

    try:
      tee_mapping = run_query(tees_query).mappings().all()
      tees = to_dict(tee_mapping)
    except Exception:
      return 'Error retrieving Course', 500

    for tee in tees:
      tee_id = tee['TEE_ID']
      # ratings
      rating_select_keys = '"RATING_ID", "TEE_ID", "NAME", "HOLE_COUNT", "GENDER", "START_HOLE", "COURSE_RATING", "SLOPE", "PAR", "BOGEY_RATING"'
      rating_query = f"""SELECT {rating_select_keys} FROM RATING R
        WHERE "TEE_ID" = {tee_id}
          AND R."EFFECTIVE_DATE" = (SELECT MAX(R_1."EFFECTIVE_DATE") FROM  RATING R_1
            WHERE R."RATING_ID" = R_1."RATING_ID")
        ORDER BY  "GENDER" DESC, "HOLE_COUNT" DESC, "START_HOLE" ASC;"""

      try:
        rating_mapping = run_query(rating_query).mappings().all()
        rating = to_dict(rating_mapping)
      except Exception:
        return 'Error retrieving Course', 500

      tee['RATING'] = rating

      # holes
      hole_select_keys = '"HOLE_ID", "TEE_ID", "NUMBER", "YARDS", "METERS", "PAR_MALE", "SI_MALE", "PAR_FEMALE", "SI_FEMALE"'
      hole_query = f"""SELECT {hole_select_keys} FROM HOLE H
        WHERE "TEE_ID" = {tee_id}
          AND H."EFFECTIVE_DATE" = (SELECT MAX(H_1."EFFECTIVE_DATE") FROM  HOLE H_1
            WHERE H."HOLE_ID" = H_1."HOLE_ID")
        ORDER BY "NUMBER" ASC;"""

      try:
        hole_mapping = run_query(hole_query).mappings().all()
        holes = to_dict(hole_mapping)
      except Exception:
        return 'Error retrieving Course', 500

      tee['HOLES'] = holes

    return {
          'FACILITY': facility[0]['FACILITY'],
          'COURSE': facility[0]['COURSES'],
          'TEES': tees
        }, 200
  elif request.method == 'POST':
    # check if course exists
    course_query = f"""SELECT * FROM COURSE
      WHERE "COURSE_ID" = '{escape(id)}';"""
      
    # run course query
    try:
      course_mapping = run_query(course_query).mappings().all()
      course = to_dict(course_mapping)
    except Exception as error:
      return 'Error retrieving Course', 500

    if len(course) == 0:
      return 'Course not found', 404
    else: 
      request.json["OVERRIDE"]["COURSE"][0] = {
        "HOLE_COUNT": course[0]["HOLE_COUNT"],
			  "ESTABLISHED": course[0]["ESTABLISHED"],
			  "ARCHITECT": course[0]["ARCHITECT"],
			  "EFFECTIVE_DATE": request.json["OVERRIDE"]["COURSE"][0]["EFFECTIVE_DATE"]
      } 

    # move to facility
    facility_query = f"""SELECT * FROM FACILITY
      WHERE "FACILITY_ID" = '{course[0]['FACILITY_ID']}';
    """

    # run facility query
    try:
      facility_mapping = run_query(facility_query).mappings().all()
      facility = to_dict(facility_mapping)
    except Exception:
      return 'Error retrieving Facility', 500

    if len(facility) == 0:
      return 'Facility not found', 404
    else: 
      request.json['OVERRIDE']['FACILITY'] = facility[0]
    
    # check if data, is a "data dump" from GHIN and translate is to data that can be uploaded
    if request.json['GHIN'] == True:
      data = translate_ghin(request.json)
      course = data['COURSE'][0]

    conn = Engine.connect()
    conn.begin()

    # INSERT INTO TEE
    # Loop for the course's list of tee sets
    for m in range(len(course['TEES'])):
      # Define tee and attach the course id 
      tee = course['TEES'][m]
      tee['COURSE_ID'] = course['COURSE_ID']

      # validate the course data and build query for insert
      tee = validate_insert_data(tee, tee_keys, tee_not_null)
      tee_query = build_insert(tee, tee_keys, 'TEE')
      run_query(tee_query, conn)
      if check_conn(conn) == 'error':
        return f'Error creating facility: Error adding data to TEE table - COURSE: {course['NAME']}, TEE: {tee['NAME']}', 400

      # INSERT INTO RATING
      # Loop for the tee set's list of ratings
      for o in range(len(tee['RATINGS'])):
        # Define rating and attach the tee id 
        rating = tee['RATINGS'][o]
        rating['TEE_ID'] = tee['TEE_ID']

        # validate the rating data and build query for insert
        rating = validate_insert_data(rating, rating_keys, rating_not_null)
        rating_query = build_insert(rating, rating_keys, 'RATING')
        run_query(rating_query, conn)
        if check_conn(conn) == 'error':
          return f'Error creating facility: Error adding data to RATING table - COURSE: {course['NAME']}, TEE: {tee['NAME']}, RATING: {rating['NAME']} - {rating['GENDER']}', 400

      # INSERT INTO HOLE
      # Loop for the tee set's list of holes
      for p in range(len(tee['HOLES'])):
        # Define hole and attach the tee id 
        hole = tee['HOLES'][p]
        hole['TEE_ID'] = tee['TEE_ID']

        # validate the hole data and build query for insert
        hole = validate_insert_data(hole, hole_keys, hole_not_null)
        hole_query = build_insert(hole, hole_keys, 'HOLE')
        run_query(hole_query, conn)
        if check_conn(conn) == 'error':
          return f'Error creating facility: Error adding data to TEE table - COURSE: {course['NAME']}, TEE: {tee['NAME']}, HOLE: {hole['NUMBER']}', 400

    conn.commit()
    conn.close()

    return 'Course Insert Completed', 201
  elif request.method == 'PUT':
    # check if facility exists
    course_query = f"""SELECT 'x' FROM COURSE
      WHERE "COURSE_ID" = '{escape(id)}';"""
    
    # run query
    try:
      course_mapping = run_query(course_query).mappings().all()
      course = to_dict(course_mapping)
    except Exception:
      return 'Error retrieving Course', 500

    # ensure facility exists
    if len(course) == 0:
      return 'Course not found', 404
    
    # create connection 
    conn = Engine.connect()
    conn.begin()

    # create and run update query
    where_clause = f'"COURSE_ID" = {escape(id)}'
    update_query = build_update(request.json, 'COURSE', where_clause)
    run_query(update_query, conn)
    if check_conn(conn) == 'error':
      return f'Error updating Course', 400

    conn.commit()
    conn.close()
    return 'Course successfully updated', 200
  elif request.method == 'DELETE':
    # create delete query
    query = f"""
    DELETE FROM COURSE
	  WHERE "COURSE_ID" = {escape(id)};
    """

    conn = Engine.connect()
    conn.begin()

    # run delete query
    run_query(query, conn)
    if check_conn(conn) == 'error':
      return f'Error deleting course', 400

    conn.commit()
    conn.close()

    return 'Course and all related Tee, Rating, and Hole Data Deleted.'

# GET SINGLE TEE, POST NEW RATINGS/HOLES TO EXISTING TEE, UPDATE TEE DATA, DELETE TEE AND ALL ITS CHILD DATA
@bp.route('/tee/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tee_single(id, config_class=Config):
  if request.method == 'GET':
    # SELECT query to get tee info
    tee_select_query = f"""SELECT * FROM TEE WHERE "TEE_ID" = {escape(id)};"""

    try:
      tee_mapping = run_query(tee_select_query).mappings().all()
      tee = to_dict(tee_mapping)[0]
    except Exception:
      return 'Error retrieving Course', 500

    course = course_single(tee['COURSE_ID'])

    for tee in course[0]['TEES']:
      if tee['TEE_ID'] == id:
        course[0]['TEES'] = tee
        break

    # return course
    return {
          'FACILITY': course[0]['FACILITY'],
          'COURSE': course[0]['COURSE'],
          'TEES': course[0]['TEES']
        }, 200
  elif request.method == 'POST':
    # Check if tee exists
    tee_query = f"""SELECT 'x' FROM TEE
      WHERE "TEE_ID" = '{escape(id)}';"""
      
    # run course query
    try:
      tee_mapping = run_query(tee_query).mappings().all()
      tee = to_dict(tee_mapping)
    except Exception as error:
      return 'Error retrieving Course', 500

    if len(tee) == 0:
      return 'Course not found', 404

    # Translate GHIN JSON to readable JSON
    if request.json['GHIN'] == True:
      # write override dicy, to allow GHIN function to run  
      request.json['OVERRIDE'] = {
        'FACILITY' : {
          'COURSE_COUNT': None,  
          'CLASSIFICATION': None,
          'CITY': None, 
          'STATE': None,
          'COUNTRY': None,
          'WEBSITE':  None,
          'ESTABLISHED': None,
          'HANDLE': None
		    },
        'COURSE': [{
          'HOLE_COUNT': None,
          'ESTABLISHED': None,
          'ARCHITECT': None,
          'EFFECTIVE_DATE': request.json['EFFECTIVE_DATE']
        }]
      }

      data = translate_ghin(request.json)
      tees = data['COURSE'][0]['TEES']
      
      # Get tee name
      for tee_name in tees:
        if tee_name['TEE_ID'] == id:
          name = tee_name['NAME']
          break
      return tees
      for tee in tees:
        if tee['NAME'] == name:
          conn = Engine.connect()
          conn.begin()
          # Loop for the tee set's list of ratings
          for o in range(len(tee['RATINGS'])):
            # Define rating and attach the tee id 
            rating = tee['RATINGS'][o]
            rating['TEE_ID'] = tee['TEE_ID']

            # validate the rating data and build query for insert
            rating = validate_insert_data(rating, rating_keys, rating_not_null)
            rating_query = build_insert(rating, rating_keys, 'RATING')
            run_query(rating_query, conn)
            if check_conn(conn) == 'error':
              return f'Error creating TEE: Error adding data to RATING table - TEE: {tee['NAME']}, RATING: {rating['NAME']} - {rating['GENDER']}', 400

          # INSERT INTO HOLE
          # Loop for the tee set's list of holes
          for p in range(len(tee['HOLES'])):
            # Define hole and attach the tee id 
            hole = tee['HOLES'][p]
            hole['TEE_ID'] = tee['TEE_ID']

            # validate the hole data and build query for insert
            hole = validate_insert_data(hole, hole_keys, hole_not_null)
            hole_query = build_insert(hole, hole_keys, 'HOLE')
            run_query(hole_query, conn)
            if check_conn(conn) == 'error':
              return f'Error creating TEE: Error adding data to HOLE table -  TEE: {tee['NAME']}, HOLE: {hole['NUMBER']}', 400
          
          conn.commit()
          conn.close()
          return 'Tee inserted successfully', 201
  elif request.method == 'PUT':
    # check if TEE exists
    tee_query = f"""SELECT 'x' FROM TEE
      WHERE "TEE_ID" = '{escape(id)}';"""
    
    # run query
    try:
      tee_mapping = run_query(tee_query).mappings().all()
      tee = to_dict(tee_mapping)
    except Exception:
      return 'Error retrieving Tee', 500

    # ensure facility exists
    if len(tee) == 0:
      return 'Tee not found', 404
    
    # create connection 
    conn = Engine.connect()
    conn.begin()

    # create and run update query
    where_clause = f'"TEE_ID" = {escape(id)}'
    update_query = build_update(request.json, 'TEE', where_clause)
    run_query(update_query, conn)
    if check_conn(conn) == 'error':
      return f'Error updating Course', 400

    conn.commit()
    conn.close()
    return 'TEE successfully updated', 200
  elif request.method == 'DELETE': 
    # create delete query
    query = f"""
    DELETE FROM TEE
	  WHERE "TEE_ID" = {escape(id)};
    """

    conn = Engine.connect()
    conn.begin()

    # run delete query
    run_query(query, conn)
    if check_conn(conn) == 'error':
      return f'Error deleting course', 400

    conn.commit()
    conn.close()

    return 'Tee and all related Rating and Hole Data Deleted.'

# POST A NEW HOLE
@bp.route('/hole', methods=['POST'])
def hole_create(config_class=Config):
  if request.method == 'POST':
    hole = request.json
    # Ensure Tee exists
    select_query = f"""SELECT 'x' FROM TEE 
      WHERE "TEE_ID" = {hole['TEE_ID']};"""
      
    try:
      tee_mapping = run_query(select_query).mappings().all()
      tee = to_dict(tee_mapping)
    except Exception as error:
      return 'Error retrieving Tee', 500

    if len(tee) == 0:
      return 'Tee not found', 404

    # Add the Hole
    conn = Engine.connect()
    conn.begin()

    hole = validate_insert_data(hole, hole_keys, hole_not_null)
    hole_query = build_insert(hole, hole_keys, 'HOLE')
    res = run_query(hole_query, conn)

    if check_conn(conn) == 'error':
      return f'Error creating HOLE: Error adding data to HOLE table - HOLE: {hole['NUMBER']}\n\nError: {res}', 400

    conn.commit()
    conn.close()
    return 'Hole inserted successfully', 201
 
# UPDATE OR DELETE A HOLE
@bp.route('/hole/<int:id>', methods=['PUT', 'DELETE'])      
def hole_update(id, config_class=Config):
  if request.method == 'PUT':
    # check if HOLE exists
    hole_query = f"""SELECT 'x' FROM HOLE
      WHERE "HOLE_ID" = '{escape(id)}';"""
    
    # run query
    try:
      hole_mapping = run_query(hole_query).mappings().all()
      hole = to_dict(hole_mapping)
    except Exception:
      return 'Error retrieving Tee', 500

    # ensure facility exists
    if len(hole) == 0:
      return 'Tee not found', 404
    
    # create connection 
    conn = Engine.connect()
    conn.begin()

    # create and run update query
    where_clause = f'"HOLE_ID" = {escape(id)}'
    update_query = build_update(request.json, 'HOLE', where_clause)
    run_query(update_query, conn)
    if check_conn(conn) == 'error':
      return f'Error updating Course', 400

    conn.commit()
    conn.close()
    
    return 'Hole successfully updated', 200
  elif request.method == 'DELETE': 
    # create delete query
    query = f"""
    DELETE FROM HOLE
	  WHERE "HOLE_ID" = {escape(id)};
    """

    conn = Engine.connect()
    conn.begin()

    # run delete query
    run_query(query, conn)
    if check_conn(conn) == 'error':
      return f'Error deleting course', 400

    conn.commit()
    conn.close()

    return 'Hole Data Deleted.'

# POST A NEW RATING
@bp.route('/rating', methods=['POST'])
def rating_create(config_class=Config):
  if request.method == 'POST':
    rating = request.json
    # Ensure Tee exists
    select_query = f"""SELECT 'x' FROM TEE 
      WHERE "TEE_ID" = {rating['TEE_ID']};"""
      
    try:
      tee_mapping = run_query(select_query).mappings().all()
      tee = to_dict(tee_mapping)
    except Exception as error:
      return 'Error retrieving Tee', 500

    if len(tee) == 0:
      return 'Tee not found', 404

    # Add the Hole
    conn = Engine.connect()
    conn.begin()

    rating = validate_insert_data(rating, rating_keys, rating_not_null)
    rating_query = build_insert(rating, rating_keys, 'RATING')
    res = run_query(rating_query, conn)

    if check_conn(conn) == 'error':
      return f'Error creating Rating: Error adding data to Rating table - Rating: {rating['NAME']}\n\nError: {res}', 400

    conn.commit()
    conn.close()
    return 'Rating inserted successfully', 201
 
# UPDATE OR DELETE A RATING
@bp.route('/rating/<int:id>', methods=['PUT', 'DELETE'])      
def Rating_update(id, config_class=Config):
  if request.method == 'PUT':
    # check if Rating exists
    rating_query = f"""SELECT 'x' FROM RATING
      WHERE "RATING_ID" = '{escape(id)}';"""
    
    # run query
    try:
      rating_mapping = run_query(rating_query).mappings().all()
      rating = to_dict(rating_mapping)
    except Exception:
      return 'Error retrieving Rating', 500

    # ensure facility exists
    if len(rating) == 0:
      return 'Rating not found', 404
    
    # create connection 
    conn = Engine.connect()
    conn.begin()

    # create and run update query
    where_clause = f'"RATING_ID" = {escape(id)}'
    update_query = build_update(request.json, 'RATING', where_clause)
    run_query(update_query, conn)
    if check_conn(conn) == 'error':
      return f'Error updating Course', 400

    conn.commit()
    conn.close()
    return 'Rating successfully updated', 200
  elif request.method == 'DELETE': 
    # create delete query
    query = f"""
    DELETE FROM RATING
	  WHERE "RATING_ID" = {escape(id)};
    """

    conn = Engine.connect()
    conn.begin()

    # run delete query
    run_query(query, conn)
    if check_conn(conn) == 'error':
      return f'Error deleting course', 400

    conn.commit()
    conn.close()

    return 'Rating Data Deleted.'

# CREATE NEW FACILITY 
@bp.route('/new', methods=['POST'])
def facility_insert(config_class=Config):
  if request.method == 'POST':
    conn = Engine.connect()
    conn.begin()
    # define data from request
    data = request.json

    # check if data, is a "data dump" from GHIN and translate is to data that can be uploaded
    if request.json['GHIN'] == True:
      data = translate_ghin(data)
      # return data

    # INSERT INTO FACILITY
    # validate the facility data and build query for insert
    facility = validate_insert_data(data['FACILITY'], facility_keys, facility_not_null)
    facility_query = build_insert(facility, facility_keys, 'FACILITY')
    run_query(facility_query, conn)
    if check_conn(conn) == 'error':
      return 'Error creating facility: Error adding data to FACILITY table', 400

    # INSERT INTO COURSE
    # Loop for the facility's list of courses
    for n in range(len(data['COURSE'])):
      # Define course and attach the facility id 
      course = data['COURSE'][n]
      course['FACILITY_ID'] = data['FACILITY']['FACILITY_ID']

      # validate the course data and build query for insert
      course = validate_insert_data(course, course_keys, course_not_null)
      course_query = build_insert(course, course_keys, 'COURSE')
      run_query(course_query, conn)
      if check_conn(conn) == 'error':
        return f'Error creating facility: Error adding data to COURSE table - COURSE: {course['NAME']}', 400

      # INSERT INTO TEE
      # Loop for the course's list of tee sets
      for m in range(len(course['TEES'])):
        # Define tee and attach the course id 
        tee = course['TEES'][m]
        tee['COURSE_ID'] = course['COURSE_ID']

        # validate the course data and build query for insert
        tee = validate_insert_data(tee, tee_keys, tee_not_null)
        tee_query = build_insert(tee, tee_keys, 'TEE')
        run_query(tee_query, conn)
        if check_conn(conn) == 'error':
          return f'Error creating facility: Error adding data to TEE table - COURSE: {course['NAME']}, TEE: {tee['NAME']}', 400

        # INSERT INTO RATING
        # Loop for the tee set's list of ratings
        for o in range(len(tee['RATINGS'])):
          # Define rating and attach the tee id 
          rating = tee['RATINGS'][o]
          rating['TEE_ID'] = tee['TEE_ID']

          # validate the rating data and build query for insert
          rating = validate_insert_data(rating, rating_keys, rating_not_null)
          rating_query = build_insert(rating, rating_keys, 'RATING')
          run_query(rating_query, conn)
          if check_conn(conn) == 'error':
            return f'Error creating facility: Error adding data to RATING table - COURSE: {course['NAME']}, TEE: {tee['NAME']}, RATING: {rating['NAME']} - {rating['GENDER']}', 400

      
        # INSERT INTO HOLE
        # Loop for the tee set's list of holes
        for p in range(len(tee['HOLES'])):
          # Define hole and attach the tee id 
          hole = tee['HOLES'][p]
          hole['TEE_ID'] = tee['TEE_ID']

          # validate the hole data and build query for insert
          hole = validate_insert_data(hole, hole_keys, hole_not_null)
          hole_query = build_insert(hole, hole_keys, 'HOLE')
          run_query(hole_query, conn)
          if check_conn(conn) == 'error':
            return f'Error creating facility: Error adding data to TEE table - COURSE: {course['NAME']}, TEE: {tee['NAME']}, HOLE: {hole['NUMBER']}', 400

    conn.commit()
    conn.close()

    return 'Facility Insert Completed', 201

# SEED FACILITY
@bp.route('/seed', methods=['POST'])
def facility_seed(config_class=Config):
  if request.method == 'POST':
    conn = Engine.connect()
    conn.begin()
    
    # from app.seeders.course_seed import course_seed as course_seed
    from app.seeders.course_seed_GHIN import course_seed_GHIN as course_seed

    # check if data, is a "data dump" from GHIN and translate is to data that can be uploaded
    if course_seed['GHIN'] == True:
      course_seed = translate_ghin(course_seed)
      # return course_seed

    # INSERT INTO FACILITY
    # validate the facility data and build query for insert
    facility = validate_insert_data(course_seed['FACILITY'], facility_keys, facility_not_null)
    facility_query = build_insert(facility, facility_keys, 'FACILITY')
    run_query(facility_query, conn)

    # INSERT INTO COURSE
    # Loop for the facility's list of courses
    for n in range(len(course_seed['COURSE'])):

      # Define course and attach the facility id 
      course = course_seed['COURSE'][n]
      course['FACILITY_ID'] = course_seed['FACILITY']['FACILITY_ID']

      # validate the course data and build query for insert
      course = validate_insert_data(course, course_keys, course_not_null)
      course_query = build_insert(course, course_keys, 'COURSE')
      run_query(course_query, conn)

      # INSERT INTO TEE
      # Loop for the course's list of tee sets
      for m in range(len(course['TEES'])):
        # Define tee and attach the course id 
        tee = course['TEES'][m]
        tee['COURSE_ID'] = course['COURSE_ID']

        # validate the course data and build query for insert
        tee = validate_insert_data(tee, tee_keys, tee_not_null)
        tee_query = build_insert(tee, tee_keys, 'TEE')
        run_query(tee_query, conn)

        # INSERT INTO RATING
        # Loop for the tee set's list of ratings
        for o in range(len(tee['RATINGS'])):
          # Define rating and attach the tee id 
          rating = tee['RATINGS'][o]
          rating['TEE_ID'] = tee['TEE_ID']

          # validate the rating data and build query for insert
          rating = validate_insert_data(rating, rating_keys, rating_not_null)
          rating_query = build_insert(rating, rating_keys, 'RATING')
          run_query(rating_query, conn)
      
        # INSERT INTO HOLE
        # Loop for the tee set's list of holes
        for p in range(len(tee['HOLES'])):
          # Define hole and attach the tee id 
          hole = tee['HOLES'][p]
          hole['TEE_ID'] = tee['TEE_ID']

          # validate the hole data and build query for insert
          hole = validate_insert_data(hole, hole_keys, hole_not_null)
          hole_query = build_insert(hole, hole_keys, 'HOLE')
          run_query(hole_query, conn)

    conn.commit()
    conn.close()
      
    return 'Facility Insert Completed', 201

