import { useState, useEffect, useContext } from 'react'
import Card from 'react-bootstrap/Card'
import Dropdown from 'react-bootstrap/esm/Dropdown'
import Carousel from 'react-bootstrap/Carousel';
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CurrentUser } from '../../../Contexts/CurrentUserContext'

import BuildHolebyHole from '../../../Functions/buildHoleByHole'

const CourseHolesCard = ({ tees }) => {
  const { currentUser, setCurrentUser} = useContext(CurrentUser)

  const [selections, setSelections] = useState({
    currentHole: 1,
    currentTee: tees[0].NAME
  })
  const { currentHole, currentTee} = selections
  
  // translate tees obj to a hole-by-hole list
  const course = BuildHolebyHole(tees, tees[0].HOLE_COUNT)
  const hole = course[currentHole -1]

  const dropTees = tees.map(tee => {
    const { NAME } = tee

    return (
      <Dropdown.Item onClick={e => setSelections({...selections, currentTee: NAME})} key={tee.NAME}>{tee.NAME}</Dropdown.Item>
    )
  })

  const carouselHoles = course.map(carouselHole => {
    const { holeNumber, parMale, siMale, parFemale, siFemale } = carouselHole
    return (
      <Carousel.Item className='pb-4' key={holeNumber} >
        <Row>
          <Col>
          <h6>{parMale[currentTee] ? parMale[currentTee] : parMale['Default']}</h6>
          <p className='text-muted'><small>MENS PAR</small></p>
          </Col>
          <Col>
          <h6>{siMale}</h6>
          <p className='text-muted'><small>MENS SI</small></p>
          </Col>
        </Row>
        <Row>
          <Col>
          <h6>{parFemale[currentTee] ? parFemale[currentTee] : parFemale['Default']}</h6>
          <p className='text-muted'><small>LADIES PAR</small></p>
          </Col>
          <Col>
          <h6>{siFemale}</h6>
          <p className='text-muted'><small>LADIES SI</small></p>
          </Col>
        </Row>
        {/* Possible to have a hole map ??? */}
      </Carousel.Item>
    )
  })

  return (
    <Card className='border-danger border-3 rounded p-2 mb-3'>
      <Card.Body className='text-center p-2'>
        <Card.Title>Hole #{currentHole}</Card.Title>
        <Card.Text>
          <Row>
            <Col>
            <Dropdown>
                <Dropdown.Toggle variant="white" className='border rounded' id="dropdown-crse-hole">
                  {currentTee}
                </Dropdown.Toggle>
                <Dropdown.Menu>
                  {dropTees}
                </Dropdown.Menu>
              </Dropdown>
            </Col>
            <Col>
              <h6>{currentUser.UNITS === 'M' ? hole.meters[currentTee] : hole.yards[currentTee]}</h6>
              <p className='text-muted'><small>{currentUser.UNITS === 'M' ? 'METERS' : 'YARDS'}</small></p>
            </Col>
          </Row>
          <Carousel activeIndex={currentHole - 1} onSelect={e => setSelections({...selections, currentHole: e + 1})} variant="dark" className='p-0 m-0' interval={null}>
            {carouselHoles}
          </Carousel>
        </Card.Text>
      </Card.Body>
    </Card>
  )
}

export default CourseHolesCard