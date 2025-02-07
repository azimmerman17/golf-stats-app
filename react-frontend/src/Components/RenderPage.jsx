import { useContext } from 'react' 

import { CurrentUser } from '../Contexts/CurrentUserContext'
import { CurrentPage } from '../Contexts/CurrentPageContext'



import HomePage from "./HomePage"
import Login from "./Login"

const RenderPage = () => {
  const { currentUser, setCurrentUser } = useContext(CurrentUser)
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  
  if (currentPage === 'about') return currentPage
  if (!currentUser) return <Login />
  console.log(currentUser)

  switch(currentPage) {  
    case 'Rounds':
      return currentPage
    case 'Handicap':
      return currentPage 
    case 'Stats':
      return currentPage
    case 'Records':
      return currentPage
    case 'Courses':
      return currentPage
    case 'Profile':
      return currentPage
    case 'Logout':
      setCurrentUser(null)
      localStorage.removeItem('golf_token')
      location.reload()
      
    default:
      return <HomePage />
  }
}

export default RenderPage