import { useContext } from 'react' 

import { CurrentUser } from '../Contexts/CurrentUserContext'
// import UserProfile from './User/UserProfile'

const  HomePage = () => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)
  return '<UserProfile />'


  
}

export default HomePage