import { useContext } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CurrentUser } from '../../../Contexts/CurrentUserContext'

const CourseTeeDetails = ({ tee }) => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)
  const { HOLES, HOLE_COUNT, METERS, NAME, RATINGS, YARDS } = tee
  const { UNITS } = currentUser

  const ratingInfo = (gender) =>  {
    const rating = RATINGS.filter(RATING => RATING.HOLE_COUNT === HOLE_COUNT && RATING.START_HOLE === 1 && RATING.GENDER === gender)
    
    console.log(gender, NAME, rating.length)
    if (!rating.length) return null
    const { COURSE_RATING, PAR,  SLOPE } = rating[0]

    return (
      <Row>
        <Col>
          <h6>{COURSE_RATING}</h6>
          <p className='text-muted'><small>{gender === 'M' ? 'Mens' : 'Ladies'} Rating</small></p>
        </Col>
        <Col>
          <h6>{SLOPE}</h6>
          <p className='text-muted'><small>{gender === 'M' ? 'Mens' : 'Ladies'} Slope</small></p>
        </Col>
        <Col>
          <h6>{PAR}</h6>
          <p className='text-muted'><small>{gender === 'M' ? 'Mens' : 'Ladies'} Par</small></p>
        </Col>
      </Row>
    )
  }
  
  return( 
    <Container fluid>
      <Row>
      <Col>
          <h6>{NAME}</h6>
          <p className='text-muted'><small>TEE</small></p>
        </Col>
        <Col>
          <h6>{ UNITS === 'M' ? METERS : YARDS}</h6>
          <p className='text-muted'><small>{ UNITS === 'M' ? 'METERS' : 'YARDS'}</small></p>
        </Col>
        {ratingInfo('M')}
        {ratingInfo('F')}
        SCORECARD ACCORDIAN
        <hr />
      </Row>
    </Container>
  )
}

export default CourseTeeDetails