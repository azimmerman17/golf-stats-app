import { useContext } from 'react'
import Card from 'react-bootstrap/Card'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CurrentUser } from '../../Contexts/CurrentUserContext'

const FacilityCourseCard = ({ course }) => { 
  const { currentUser, setCurrentUser } = useContext(CurrentUser)
  const { ARCHITECT, COURSE_ID, ESTABLISHED, HOLE_COUNT, NAME, TEES } = course

  const courseTee = (tees) => {
    let longest = {}
    tees.forEach(tee => {!longest.YARDS || longest.YARDS < tee.YARDS ? longest = tee : null})

    const { YARDS, METERS, RATINGS } = longest
    const { UNITS } = currentUser

    const courseRating = RATINGS.filter(rating => rating.START_HOLE === 1 && rating.NAME === 'Full' && rating.HOLE_COUNT === HOLE_COUNT)
    const { COURSE_RATING, PAR, SLOPE } = courseRating[0]

    return (
      <Row className='m-3'>
        <Col xs={12}  md={6} className='text-center'>
          <h6>{UNITS === 'Y' ? YARDS : METERS}</h6>
          <p className='text-muted'><small>LENGTH</small></p>
        </Col>
        <Col xs={12} md={6} className='text-center'>
          <h6>{PAR}</h6>
          <p className='text-muted'><small>PAR</small></p>
        </Col>
        <Col xs={12}  md={6} className='text-center'>
          <h6>{COURSE_RATING}</h6>
          <p className='text-muted'><small>COURSE RATING</small></p>
        </Col>
        <Col xs={12}  md={6} className='text-center'>
          <h6>{SLOPE}</h6>
          <p className='text-muted'><small>SLOPE</small></p>
        </Col>
      </Row>
    )
  }

  return (
    <Card className='border-danger border-3 rounded p-2 mb-3'>
      <Card.Body>
        <Card.Title className='text-center p-1'>{NAME}</Card.Title>
        <Card.Text className='text-center p-1'>
        <Row className='m-3'>
            <Col xs={12}  md={6} className='text-center'>
              <h6>{ARCHITECT}</h6>
              <p className='text-muted'><small>ARCHITECT</small></p>
            </Col>
            <Col xs={12} md={6} className='text-center'>
              <h6>{ESTABLISHED}</h6>
              <p className='text-muted'><small>ESTABLISHED</small></p>
            </Col>
            <Col xs={12}  md={6} className='text-center'>
              <h6>{HOLE_COUNT}</h6>
              <p className='text-muted'><small>HOLE COUNT</small></p>
            </Col>
            <Col xs={12}  md={6} className='text-center'>
              <h6>{TEES.length}</h6>
              <p className='text-muted'><small>TEE_COUNT</small></p>
            </Col>
          </Row>
          {courseTee(TEES)}
        </Card.Text>
      </Card.Body> 
    </Card>
  )
}

export default FacilityCourseCard