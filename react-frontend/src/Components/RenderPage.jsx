import { useContext } from 'react' 

import { CurrentUser } from '../Contexts/CurrentUserContext'



import HomePage from "./HomePage"
import Login from "./Login"

const RenderPage = ({page, setPage}) => {
  const { currentUser, setCurrentUser } = useContext(CurrentUser)
  
  if (!currentUser) return <Login />
  console.log(currentUser)

  switch(page) {
  
    default:
      return <HomePage />
  }
}

export default RenderPage