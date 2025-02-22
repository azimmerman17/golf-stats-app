const GetHomeFacility = async (id) => {
  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://localhost:8080'

  let response = await fetch(BASE_URL + `/facility/${id}`)
  let course = await response.json()

  if (course) return course
  else return null
}

export default GetHomeFacility