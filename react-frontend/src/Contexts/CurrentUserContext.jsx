// context for the current user
import { useEffect, createContext, useState } from 'react';

import GetNation from '../Functions/GetNation';
import GetHomeFacility from '../Functions/GetHomeFacility';

export const CurrentUser = createContext()

const CurrentUserProvider = ({ children }) => {
  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://127.0.0.1:8080'
  const [currentUser, setCurrentUser] = useState(null)

  useEffect(() => {
    const getLoggedInUser = async () => {
      const options = {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${localStorage.getItem('golf_token')}`,
          'user': currentUser
        },
      }

      let response = await fetch(BASE_URL + '/auth/user', options)
      let user = await response.json()

      if (response.status === 200) {    
        if (user.HOME_FACILITY) {
          user.HOME_FACILITY =  await GetHomeFacility(user.HOME_FACILITY)
        }
        if (user.NATIONALITY) {
          user.NATION = await GetNation(user.NATIONALITY)
        }

        setCurrentUser(user)
      }
    }
    getLoggedInUser()
  }, [])
  
  return (
    <CurrentUser.Provider value={{ currentUser, setCurrentUser }}>
        {children}
    </CurrentUser.Provider>
  )
}

export default CurrentUserProvider