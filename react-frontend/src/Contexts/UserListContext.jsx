// context for the coures
import { createContext, useEffect, useState } from 'react';

export const UserList = createContext()

const UserListProvider = ({ children }) => {
  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://127.0.0.1:8080'
  const [userList, setUserList] = useState([])

  useEffect(() =>{
    const getCourses = async () => {

      let response = await fetch(BASE_URL + '/user')
      let users = await response.json()
      setUserList(users)
    }

    if (userList.length === 0 ) getCourses()
  },[userList])

  return (
    <UserList.Provider value={{ userList, setUserList }}>
        {children}
    </UserList.Provider>
  )
}

export default UserListProvider
