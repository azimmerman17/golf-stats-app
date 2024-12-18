# this bluebrint controls db trasactions with the Facility Models
from flask import request
from markupsafe import escape

from app.facility import bp
from app.extensions import to_dict
from app.models.facility import facility_keys, facility_not_null 
from app.models.course import COURSE, course_keys, course_not_null
from app.models.tee import tee_keys, tee_not_null
from app.models.rating import rating_keys, rating_not_null
from app.models.hole import hole_keys, hole_not_null
from app.functions_sql import run_query, build_insert, validate_insert_data
from config import Config


# GET ALL FACILITIES
@bp.route('/', methods=['GET'])
def facility_all(config_class=Config):
  if request.method == 'GET':
    select_keys = '"FACILITY_ID", "NAME", "HANDLE", "CLASSIFICATION", "CITY", "STATE", "COUNTRY", "GEO_LAT", "GEO_LON"'
    query = f"""SELECT {select_keys} FROM FACILITY
      ORDER BY "NAME", "FACILITY_ID";"""

    mapping = run_query(query).mappings().all()
    res = to_dict(mapping)

    return res

# GET SINGLE FACILITY
@bp.route('/<handle>', methods=['GET'])
def facility_one(handle, config_class=Config):
    if request.method == 'GET':
      facility_select_keys = '"FACILITY_ID", "NAME", "HANDLE", "CLASSIFICATION", "COURSE_COUNT", "ESTABLISHED", "WEBSITE", "ADDRESS", "CITY", "STATE", "COUNTRY", "GEO_LAT", "GEO_LON"'
      facility_query = f"""SELECT {facility_select_keys} FROM FACILITY
        WHERE "HANDLE" = '{escape(handle)}'
          OR "FACILITY_ID" = '{escape(handle)}';"""
      facility_mapping = run_query(facility_query).mappings().all()
      facility = to_dict(facility_mapping)[0]

      course_select_keys = '"COURSE_ID", "FACILITY_ID", "NAME", "HOLE_COUNT", "ESTABLISHED", "ARCHITECT"'
      course_query = f"""SELECT {course_select_keys} FROM COURSE
        WHERE "FACILITY_ID" = {facility['FACILITY_ID']};"""

      course_mapping = run_query(course_query).mappings().all()
      course = to_dict(course_mapping)

      return {
        'FACILITY': facility,
        'COURSES': course
      }

# GET ALL COURSES
@bp.route('/course', methods=['GET'])
def course_all(config_class=Config):
  if request.method == 'GET':
    select_keys = 'F."FACILITY_ID", F."NAME", F."HANDLE", F."CLASSIFICATION", F."CITY", F."STATE", F."COUNTRY", F."GEO_LAT", F."GEO_LON", C."COURSE_ID",C."NAME" as "COURSE_NAME",C."HOLE_COUNT",C."ESTABLISHED",C."ARCHITECT"'
    query = f"""SELECT {select_keys} FROM FACILITY F, COURSE C
      WHERE F."FACILITY_ID" = C."FACILITY_ID"
      ORDER BY F."NAME", F."FACILITY_ID", C."NAME",  C."COURSE_ID";"""

    mapping = run_query(query).mappings().all()
    res = to_dict(mapping)

    return res

# GET SINGLE COURSE
@bp.route('/course/<id>', methods=['GET'])
def course_single(id, config_class=Config):
  # course
  course_select_keys = '"COURSE_ID", "FACILITY_ID", "NAME", "HOLE_COUNT", "ESTABLISHED", "ARCHITECT"'
  course_query = f"""SELECT {course_select_keys} FROM COURSE
    WHERE "COURSE_ID" = {escape(id)};"""

  course_mapping = run_query(course_query).mappings().all()
  course = to_dict(course_mapping)[0]

  # facility
  facility_id = course['FACILITY_ID']
  facility_select_keys = '"FACILITY_ID", "NAME", "HANDLE", "CLASSIFICATION", "COURSE_COUNT", "ESTABLISHED", "WEBSITE", "ADDRESS", "CITY", "STATE", "COUNTRY", "GEO_LAT", "GEO_LON"'
  facility_query = f"""SELECT {facility_select_keys} FROM FACILITY
    WHERE "FACILITY_ID" = '{facility_id}';"""

  facility_mapping = run_query(facility_query).mappings().all()
  facility = to_dict(facility_mapping)[0]

  #tees
  tee_select_keys = '"TEE_ID", "COURSE_ID", "NAME", "YARDS", "METERS", "HOLE_COUNT"'
  tees_query = f"""SELECT {tee_select_keys} FROM TEE
    WHERE "COURSE_ID" = {escape(id)}
    ORDER BY "YARDS" DESC;"""

  tee_mapping = run_query(tees_query).mappings().all()
  tees = to_dict(tee_mapping)

  for tee in tees:
    tee_id = tee['TEE_ID']
    # ratings
    rating_keys = '"RATING_ID", "TEE_ID", "NAME", "HOLE_COUNT", "GENDER", "START_HOLE", "COURSE_RATING", "SLOPE", "PAR", "BOGEY_RATING"'
    rating_query = f"""SELECT {rating_keys} FROM RATING R
      WHERE "TEE_ID" = {tee_id}
        AND R."EFFECTIVE_DATE" = (SELECT MAX(R_1."EFFECTIVE_DATE") FROM  RATING R_1
          WHERE R."RATING_ID" = R_1."RATING_ID")
      ORDER BY  "GENDER" DESC, "HOLE_COUNT" DESC, "START_HOLE" ASC;"""

    rating_mapping = run_query(rating_query).mappings().all()
    rating = to_dict(rating_mapping)
    tee['RATING'] = rating

    # holes
    hole_keys = '"HOLE_ID", "TEE_ID", "NUMBER", "YARDS", "METERS", "PAR_MALE", "SI_MALE", "PAR_FEMALE", "SI_FEMALE"'
    hole_query = f"""SELECT {hole_keys} FROM HOLE H
      WHERE "TEE_ID" = {tee_id}
        AND H."EFFECTIVE_DATE" = (SELECT MAX(H_1."EFFECTIVE_DATE") FROM  HOLE H_1
          WHERE H."HOLE_ID" = H_1."HOLE_ID")
      ORDER BY "NUMBER" ASC;"""

    hole_mapping = run_query(hole_query).mappings().all()
    holes = to_dict(hole_mapping)
    tee['HOLES'] = holes

  return {
        'FACILITY': facility,
        'COURSE': course,
        'TEES': tees
      }

# CREATE NEW FACILITY
@bp.route('/new', methods=['POST'])
def facility_insert(config_class=Config):
  if request.method == 'POST':
    if request.json['GHIN'] == False:
      print('Create script to translate data from GHIN to load into DB')

    data = request.json
    # INSERT INTO FACILITY
    # validate the facility data and build query for insert
    facility = validate_insert_data(data['FACILITY'], facility_keys, facility_not_null)
    facility_query = build_insert(facility, facility_keys, 'FACILITY')
    run_query(facility_query)

    # INSERT INTO COURSE
    # Loop for the facility's list of courses
    for n in range(len(data['COURSE'])):
      # Define course and attach the facility id 
      course = data['COURSE'][n]
      course['FACILITY_ID'] = data['FACILITY']['FACILITY_ID']

      # validate the course data and build query for insert
      course = validate_insert_data(course, course_keys, course_not_null)
      course_query = build_insert(course, course_keys, 'COURSE')
      run_query(course_query)

      # INSERT INTO TEE
      # Loop for the course's list of tee sets
      for m in range(len(course['TEES'])):
        # Define tee and attach the course id 
        tee = course['TEES'][m]
        tee['COURSE_ID'] = course['COURSE_ID']

        # validate the course data and build query for insert
        tee = validate_insert_data(tee, tee_keys, tee_not_null)
        tee_query = build_insert(tee, tee_keys, 'TEE')
        run_query(tee_query)

        # INSERT INTO RATING
        # Loop for the tee set's list of ratings
        for o in range(len(tee['RATINGS'])):
          # Define rating and attach the tee id 
          rating = tee['RATINGS'][o]
          rating['TEE_ID'] = tee['TEE_ID']

          # validate the rating data and build query for insert
          rating = validate_insert_data(rating, rating_keys, rating_not_null)
          rating_query = build_insert(rating, rating_keys, 'RATING')
          run_query(rating_query)
      
        # INSERT INTO HOLE
        # Loop for the tee set's list of holes
        for p in range(len(tee['HOLES'])):
          # Define hole and attach the tee id 
          hole = tee['HOLES'][p]
          hole['TEE_ID'] = tee['TEE_ID']

          # validate the hole data and build query for insert
          hole = validate_insert_data(hole, hole_keys, hole_not_null)
          hole_query = build_insert(hole, hole_keys, 'HOLE')
          run_query(hole_query)

    return request.json

# SEED FACILITY
@bp.route('/seed', methods=['POST'])
def facility_seed(config_class=Config):
  if request.method == 'POST':
    from app.seeders.course_seed import course_seed

    # INSERT INTO FACILITY
    # validate the facility data and build query for insert
    facility = validate_insert_data(course_seed['FACILITY'], facility_keys, facility_not_null)
    facility_query = build_insert(facility, facility_keys, 'FACILITY')
    run_query(facility_query)

    # INSERT INTO COURSE
    # Loop for the facility's list of courses
    for n in range(len(course_seed['COURSE'])):
      # Define course and attach the facility id 
      course = course_seed['COURSE'][n]
      course['FACILITY_ID'] = course_seed['FACILITY']['FACILITY_ID']

      # validate the course data and build query for insert
      course = validate_insert_data(course, course_keys, course_not_null)
      course_query = build_insert(course, course_keys, 'COURSE')
      run_query(course_query)

      # INSERT INTO TEE
      # Loop for the course's list of tee sets
      for m in range(len(course['TEES'])):
        # Define tee and attach the course id 
        tee = course['TEES'][m]
        tee['COURSE_ID'] = course['COURSE_ID']

        # validate the course data and build query for insert
        tee = validate_insert_data(tee, tee_keys, tee_not_null)
        tee_query = build_insert(tee, tee_keys, 'TEE')
        run_query(tee_query)

        # INSERT INTO RATING
        # Loop for the tee set's list of ratings
        for o in range(len(tee['RATINGS'])):
          # Define rating and attach the tee id 
          rating = tee['RATINGS'][o]
          rating['TEE_ID'] = tee['TEE_ID']

          # validate the rating data and build query for insert
          rating = validate_insert_data(rating, rating_keys, rating_not_null)
          rating_query = build_insert(rating, rating_keys, 'RATING')
          run_query(rating_query)
      
        # INSERT INTO HOLE
        # Loop for the tee set's list of holes
        for p in range(len(tee['HOLES'])):
          # Define hole and attach the tee id 
          hole = tee['HOLES'][p]
          hole['TEE_ID'] = tee['TEE_ID']

          # validate the hole data and build query for insert
          hole = validate_insert_data(hole, hole_keys, hole_not_null)
          hole_query = build_insert(hole, hole_keys, 'HOLE')
          run_query(hole_query)

    return 'Facility Insert Completed'







