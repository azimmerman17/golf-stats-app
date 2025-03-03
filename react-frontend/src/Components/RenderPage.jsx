import { useContext } from 'react' 

import { CurrentUser } from '../Contexts/CurrentUserContext'
import { CurrentPage } from '../Contexts/CurrentPageContext'



import HomePage from './HomePage'
import Login from './Login'
import About from './About'
import ProfilePage from './Profile/ProfilePage'
import CoursesHome from './Courses/CoursePage'
import FacilityHome from './Courses/FacilityHome'

const RenderPage = () => {
  const { currentUser, setCurrentUser } = useContext(CurrentUser)
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  
  if (currentPage === 'about') return <About />
  if (!currentUser) return <Login />
  console.log(currentPage)

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
      return <CoursesHome />
    case 'Facility':
      return <FacilityHome />
    case 'Profile':
      return <ProfilePage />
    case 'Logout':
      setCurrentUser(null)
      localStorage.removeItem('golf_token')
      location.reload()
      
    default:
      return <HomePage />
  }
}

export default RenderPage