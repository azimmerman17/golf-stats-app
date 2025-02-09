import { useContext } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CurrentUser } from '../Contexts/CurrentUserContext'

import NavCards from './NavCards'
import ProfileHome from './Profile/ProfileHome'
import HomeCourseCard from './Courses/HomeCourseCard'
import HandicapCard from './Handicap/HandicapCard'

const  HomePage = () => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)
  const { HOME_FACILITY, HANDICAP } = currentUser

  console.log(currentUser)

  const cards = [
    // {title: 'Statistics', icon: 'Stats', page: 'Stats', space: true},
    // {title: 'Rounds', icon: 'Rounds', page: 'Rounds', space: true},
    // {title: 'Handicap', icon: 'Handicap', page: 'Handicap', space: true},
    // {title: 'Records', icon: 'Records', page: 'Records', space: true},
    {title: 'Courses', icon: 'Courses', page: 'Courses', space: true},
    // {title: 'New Round', icon: 'Rounds Plus', page: 'New Round', space: true},
    // {title: 'New Practice', icon: 'Practice Plus', page: 'New Practice', space: false},
    // {title: 'New Course', icon: 'Course Plus', page: 'New Course', space: false},
    {title: 'Profile', icon: 'Profile', page: 'Profile', space: true}
  ]

  const navCards = cards.map(card => {
    const { title, icon, page, space } = card

    return (
      <Col className='mx-auto p-1' key={`HPcard-${title}`}>
        <NavCards title={title} icon={icon} page={page} space={space}/>
      </Col>
    )
  })

  return (
    <Container fluid>
      <Row className='my-1 mx-auto'>
        <ProfileHome currentUser={currentUser}/>
      </Row>
      <Row className='my-1 mx-auto'>
        <Col className='p-2'>
          <HomeCourseCard facility={HOME_FACILITY.FACILITY} />
        </Col>
        <Col className='p-2'> 
          <HandicapCard  handicap={HANDICAP}/>
        </Col>
      </Row>
      <Row className='my-1 mx-auto'>
        {navCards}   
      </Row>
    </Container>

  )
}

export default HomePage