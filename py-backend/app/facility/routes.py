# this bluebrint controls db trasactions with the Facility Models
from flask import request

from app.facility import bp
from app.models.facility import facility_keys, facility_not_null
from app.models.course import course_keys, course_not_null
from app.models.tee import tee_keys, tee_not_null
from app.models.rating import rating_keys, rating_not_null
from app.models.hole import hole_keys, hole_not_null
from app.functions_sql import run_query, build_insert, validate_insert_data
from config import Config


# Get All facilities
# GET / UPDATE / DELETE SPECIFIC FACILITIES
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
          ratings_query = build_insert(rating, rating_keys, 'RATING')
          run_query(ratings_query)
      
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

    print(request)
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
          ratings_query = build_insert(rating, rating_keys, 'RATING')
          run_query(ratings_query)
      
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







