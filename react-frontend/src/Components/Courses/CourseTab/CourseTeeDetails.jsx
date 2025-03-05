import { useContext } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CurrentUser } from '../../../Contexts/CurrentUserContext'
import ScoreCardTable from './ScoreCardTable'

const CourseTeeDetails = ({ tee, selectedTee, setSelectedTee }) => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)
  const { HOLES, HOLE_COUNT, METERS, NAME, RATINGS, YARDS } = tee
  const { UNITS } = currentUser

  const ratingInfo = (gender) =>  {
    const rating = RATINGS.filter(RATING => RATING.HOLE_COUNT === HOLE_COUNT && RATING.START_HOLE === 1 && RATING.GENDER === gender)
    
    if (!rating.length) return null
    const { BOGEY_RATING, COURSE_RATING, PAR,  SLOPE } = rating[0]

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
          <h6>{BOGEY_RATING}</h6>
          <p className='text-muted'><small>Bogey Rating</small></p>
        </Col>

        <Col>
          <h6>{PAR}</h6>
          <p className='text-muted'><small>{gender === 'M' ? 'Mens' : 'Ladies'} Par</small></p>
        </Col>
      </Row>
    )
  }
  
  return( 
    <Container fluid className='p-1'>
      <Row>
      <Col>
          <h6>{NAME}</h6>
          <p className='text-muted'><small>TEE</small></p>
        </Col>
        <Col>
          <h6>{ UNITS === 'M' ? METERS : YARDS}</h6>
          <p className='text-muted'><small>{ UNITS === 'M' ? 'METERS' : 'YARDS'}</small></p>
        </Col>
      </Row>
        {ratingInfo('M')}
        {ratingInfo('F')}
        <Accordion defaultActiveKey={selectedTee} className='p-0 mb-1' onSelect={e =>  setSelectedTee(NAME)}>
          <Accordion.Item eventKey={NAME}>
            <Accordion.Header>{NAME} Tee Scorecard</Accordion.Header>
            <Accordion.Body className='p-1'>
              <ScoreCardTable holes={HOLES} units={UNITS}/>
            </Accordion.Body>
          </Accordion.Item>
        </Accordion>
        <hr />

    </Container>
  )
}

export default CourseTeeDetails