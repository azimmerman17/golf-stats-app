# Function to translate GHIN JSON to JSON that can load into the DB
def translate_ghin(data):
  # Define Facility Data
  facility_data = data['DATA'][0]['Facility']
  override_data = data['OVERRIDE']['FACILITY']
  state = data['DATA'][0]['CourseState']

  # Generate Facility City, State, and Country
  if state.split('-')[0] =='US':
    location = {
      'CITY':  data['DATA'][0]['CourseCity'],
      'STATE':  state.split('-')[1],
      'COUNTRY': 'USA'
    }
  elif state.strip()[0] =='CA':
    location = {
      'CITY': data['DATA'][0]['CourseCity'],
      'STATE': state.split('-')[1],
      'COUNTRY': 'CAN'
    }
  else:
    location = {
      'CITY': override_data['CITY'],
      'STATE': None,
      'COUNTRY': override_data['COUNTRY']
    }

  # Facitiy Dict
  FACILITY = {
    "FACILITY_ID": facility_data['FacilityId'],
		"NAME": facility_data['FacilityName'],
		"ADDRESS": facility_data['GeoLocationFormattedAddress'],
		"GEO_LON": facility_data['GeoLocationLongitude'],
		"GEO_LAT": facility_data['GeoLocationLatitude'],
		"COURSE_COUNT": override_data['COURSE_COUNT'] if override_data['COURSE_COUNT'] != None else len(data['DATA']),
    "CLASSIFICATION": override_data['CLASSIFICATION'],
		"CITY": location['CITY'],
		"STATE": location['STATE'],
		"COUNTRY": location['COUNTRY'],
		"WEBSITE": override_data['WEBSITE'],
		"ESTABLISHED": override_data['ESTABLISHED'],
		"HANDLE": override_data['HANDLE'],
  }

  # Define Course Data
  COURSE = []
  print(len(data['DATA']))
  for n in range(len(data['DATA'])):
    course_data = data['DATA'][n]
    override_data = data['OVERRIDE']['COURSE'][n]
    
    # Course dict
    new_course = {
      'COURSE_ID': course_data['CourseId'],
      'NAME': course_data['CourseName'],
      'HOLE_COUNT':override_data['HOLE_COUNT'] if override_data['HOLE_COUNT'] != None else len(course_data['TeeSets'][0]['Holes']),
      'ESTABLISHED':override_data['ESTABLISHED'],
      'ARCHITECT': override_data['ARCHITECT']
    }

    # Define Tee Data
    TEES = []
    tee_sets = {}
    for m in range(len(course_data['TeeSets'])):
      tee_data = course_data['TeeSets'][m]
      if course_data['TeeSets'][m]['TeeSetRatingName'] not in tee_sets:
        # new tee 
        tee_sets[tee_data['TeeSetRatingName']] = {
          'TEE_ID': tee_data['TeeSetRatingId'], 
          'COURSE_ID':  new_course['COURSE_ID'], 
          'NAME': tee_data['TeeSetRatingName'], 
          'YARDS': tee_data['TotalYardage'],
          'METERS': tee_data['TotalMeters'],
          'HOLE_COUNT': new_course['HOLE_COUNT'], 
          'RATINGS': [],
          'HOLES': []
        }

      # set tee we are adding to, regardless if it is a new tee or not
      current_tee = tee_sets[tee_data['TeeSetRatingName']]

      # Define Rating Data
      for o in range(len(tee_data['Ratings'])):
        rating_data = tee_data['Ratings'][o]

        # new rating dict
        rating = {
          'TEE_ID': tee_data['TeeSetRatingId'],
          'NAME': 'Full' if rating_data['RatingType'] == 'Total' else rating_data['RatingType'],
          'HOLE_COUNT': current_tee['HOLE_COUNT']  if rating_data['RatingType'] == 'Total' else 9,
          'GENDER': 'M' if tee_data['Gender'] == 'Male' else 'F',
          'START_HOLE': 10 if rating_data['RatingType'] == 'Back' else 1,
          'COURSE_RATING': rating_data['CourseRating'],
          'SLOPE': rating_data['SlopeRating'],
          'PAR': tee_data['TotalPar'],
          'BOGEY_RATING': rating_data['BogeyRating'],
          'EFFECTIVE_DATE': override_data['EFFECTIVE_DATE']
        }

        # add dict to Tee Rating List
        tee_sets[tee_data['TeeSetRatingName']]['RATINGS'].append(rating)

      # Define Hole Data
      for p in range(len(tee_data['Holes'])):
        hole_data = tee_data['Holes'][p]
        index = hole_data['Number'] - 1

        # If the hole number is <= length of Hole list, create a new hole
        if len(tee_sets[tee_data['TeeSetRatingName']]['HOLES']) <= index:
          hole = {
            'TEE_ID': tee_data['TeeSetRatingId'],
            'NUMBER': hole_data['Number'],
            'YARDS': hole_data['Length'],
            'EFFECTIVE_DATE': override_data['EFFECTIVE_DATE']
          }

          # add hole to hole list
          tee_sets[tee_data['TeeSetRatingName']]['HOLES'].append(hole)

        # Add Par and Stroke Index data to the hole for both Male and Female
        if tee_data['Gender'] == 'Male':
          tee_sets[tee_data['TeeSetRatingName']]['HOLES'][index]['PAR_MALE'] = hole_data['Par']
          tee_sets[tee_data['TeeSetRatingName']]['HOLES'][index]['SI_MALE'] = hole_data['Allocation']
        else:
          tee_sets[tee_data['TeeSetRatingName']]['HOLES'][index]['PAR_FEMALE'] = hole_data['Par']
          tee_sets[tee_data['TeeSetRatingName']]['HOLES'][index]['SI_FEMALE'] = hole_data['Allocation']

    # transform the tee_set map to a list
    for tee_set in tee_sets:
      TEES.append(tee_sets[tee_set]) 

    # add Tee list to new course
    new_course['TEES'] = TEES

    #add new Course to course list
    COURSE.append(new_course)

  return {'FACILITY': FACILITY, 'COURSE': COURSE}
