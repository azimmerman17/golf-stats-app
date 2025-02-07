import { useContext } from 'react' 

import { CurrentUser } from '../Contexts/CurrentUserContext'
import Login from './Login'
// import UserProfile from './User/UserProfile'

const  HomePage = () => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)


  // convert string to Component when built
  if (!currentUser) return <Login />
  else return '<UserProfile />'


  
}

export default HomePage