// context for the coures
import { createContext, useEffect, useState } from 'react';

export const CourseList = createContext()

const CourseListProvider = ({ children }) => {
  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://127.0.0.1:8080'
  const [courseList, setCourseList] = useState([])

  useEffect(() =>{
    const getCourses = async () => {

      let response = await fetch(BASE_URL + '/facility')
      let courses = await response.json()
      setCourseList(courses)
    }

    if (courseList.length === 0 ) getCourses()
  },[courseList])

  return (
    <CourseList.Provider value={{ courseList, setCourseList }}>
        {children}
    </CourseList.Provider>
  )
}

export default CourseListProvider
