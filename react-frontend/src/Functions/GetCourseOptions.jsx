const GetCourseOptions = (list) => {
  let options = []

  list.forEach(course => {
    const { NAME, STATE, CITY, COUNTRY, FACILITY_ID } = course
    options.push(`${NAME} - ${CITY}, ${STATE ? STATE : COUNTRY} - ${FACILITY_ID}`)
 
  });

  return options
}

export default GetCourseOptions