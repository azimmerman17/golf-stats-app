import { useEffect, useState } from "react"
import Card from 'react-bootstrap/Card'
import Dropdown from 'react-bootstrap/Dropdown';
import Form from 'react-bootstrap/Form'
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import CourseHandicapRating from "./CourseHandicapRatings";

const CourseHandicap = ({ tees, selectedTee }) => {
  const [displayedTee, setDisplayedTee] = useState(tees.filter(tee => tee.NAME === selectedTee))
  const [userHandicap, setUserHandicap] = useState(2.7)  // change to user's current handicap, when handicap data is added
  const [handicapGender, setHandicapGender] = useState('M')  //get from CurrentUser
  
  const [selections, setSelections] = useState({ 
    tee: tees.filter(tee => tee.NAME === selectedTee)[0],
    handicap: 2.7,    // change to user's current handicap, when handicap data is added
    gender: 'M', // change to user's current handicap, when handicap data is added
    ratingName: 'Full',
    score: null
  })
  const [selectedRating, setSelectedRating] = useState(selections.tee.RATINGS.filter(rating => rating.GENDER === 'M' && rating.NAME === selections.ratingName))
  
  useEffect(() => {
    setSelectedRating(selections.tee.RATINGS.filter(rating => rating.GENDER == selections.gender && rating.NAME == selections.ratingName))
  }, [selections])

  const dropTees = tees.map(tee => {
    const { NAME } = tee

    return (
      <Dropdown.Item onClick={e => setSelections({...selections, tee: tees.filter(selectTee => selectTee.NAME === NAME)[0] })} key={tee.TEE_ID}>{tee.NAME}</Dropdown.Item>
    )
  })

  const dropRatings = selections.tee.RATINGS.map(rating =>{
    if (rating.GENDER === selections.gender) return  <Dropdown.Item onClick={e =>setSelections({...selections, ratingName: rating.NAME})} key={rating.RATING_ID}>{rating.NAME}</Dropdown.Item>
  })

  return (
    <Card className='border-danger border-3 rounded p-2 mb-3'>
      <Card.Body className='text-center'>
        <Card.Title>Course Handcap</Card.Title>
        <Card.Text>
          <Row className='my-2 mx-0'>
            <Col  className="p-1">
              <Dropdown>
                <Dropdown.Toggle variant="white" className='border rounded' id="dropdown-crse-handicap">
                  {selections.tee.NAME}
                </Dropdown.Toggle>
                <Dropdown.Menu>
                  {dropTees}
                </Dropdown.Menu>
              </Dropdown>
              <p className="text-muted mb-0"><small>TEE</small></p>
            </Col>           
            <Col className="p-1" >
              <Dropdown>
                <Dropdown.Toggle variant="white" className='border rounded' id="dropdown-crse-handicap">
                  {selections.gender === 'M' ? 'Male' : 'Female'}
                </Dropdown.Toggle>
                <Dropdown.Menu>
                  <Dropdown.Item onClick={e => setSelections({...selections, gender:'M'})}>Male</Dropdown.Item>
                  <Dropdown.Item onClick={e => setSelections({...selections, gender:'F'})}>Female</Dropdown.Item>
                </Dropdown.Menu>
              </Dropdown>
              <p className="text-muted mb-0"><small>Gender</small></p>
            </Col>
            <Col className="p-1">
              <Dropdown>
                <Dropdown.Toggle variant="white" className='border rounded' id="dropdown-crse-rating">
                  {selections.ratingName}
                </Dropdown.Toggle>
                <Dropdown.Menu>
                  {dropRatings}
                </Dropdown.Menu>
              </Dropdown>
              <p className="text-muted mb-0"><small>Rating</small></p>
            </Col>
            <Col className="p-1" md={4}>
              <Form onChange={e => setSelections({...selections, handicap: e.target.value})}> 
                <Form.Group controlId="user-handicap">
                  <Form.Control type="number" placeholder={selections.handicap} />
                  <Form.Label className='text-muted'><small>Hdcp Index</small></Form.Label>
                </Form.Group>
              </Form>
            </Col>
          </Row>
          <CourseHandicapRating rating={selectedRating} setSelections={setSelections} selections={selections} />
        </Card.Text>
      </Card.Body>
    </Card>
  )
}

export default CourseHandicap