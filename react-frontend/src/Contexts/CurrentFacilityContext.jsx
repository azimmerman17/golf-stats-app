// context for the current navigated facility
import { createContext, useState, useEffect } from 'react';

export const CurrentFacility = createContext()

const CurrentFacilityProvider = ({ children }) => {
  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://127.0.0.1:8080'
  const [currentFacility, setCurrentFacility] = useState(null)

  useEffect(() => {
    const getCourseFacility = async (id) => {
      let response = await fetch(BASE_URL + '/facility/' + id)
      let  facility = await response.json()
      console.log(facility)

      setCurrentFacility(facility)
    }

    console.log(typeof currentFacility)
    if (typeof currentFacility === 'number' || typeof currentFacility === 'string') getCourseFacility(currentFacility)
  }, [currentFacility])
  


  return (
    <CurrentFacility.Provider value={{ currentFacility, setCurrentFacility }}>
        {children}
    </CurrentFacility.Provider>
  )
}

export default CurrentFacilityProvider
