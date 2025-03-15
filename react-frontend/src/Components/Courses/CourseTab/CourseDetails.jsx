import { useEffect, useState } from 'react'
import Container from 'react-bootstrap/esm/Container'
import Row from 'react-bootstrap/esm/Row'
import Col from 'react-bootstrap/esm/Col'


import FacilityCourseCard from '../FacilityCourseCard'
import CourseTeeCard from './CourseTeeCard'
import CourseHandicap from './CourseHandicap'
import CourseHolesCard from './CourseHolesCard'
import HoleCardModal from '../../Maps/HoleCardModal';


const CourseDetails = ({ course }) => {
  console.log(course)
  const [showModal, setShowModal] = useState({show: false, hole: 1})
  const [ selectedTee, setSelectedTee ] = useState(course.TEES[0].NAME)
  const { TEES, MAP } = course
  
  useEffect(() => {
    if (!selectedTee && TEES) {
      setSelectedTee(TEES[0].NAME)
    }
  }, [selectedTee])

  return (
    <Container fluid className='p-0'>
      <Row className='my-2 mx-1'>
        <Col>
          <CourseTeeCard tees={TEES} selectedTee={selectedTee} setSelectedTee={setSelectedTee}/>
        </Col>
        <Col>
          <Row>
            <FacilityCourseCard course={course}/>
          </Row>
          <Row>
            <CourseHandicap tees={TEES} selectedTee={selectedTee} />
            <CourseHolesCard tees={TEES} map={MAP} setShowModal={setShowModal} />
            {/* FUTURE DEVELOPMENT */}
            {/* <p>Course Stats - Change with the tee offer base information</p> */}
            {/* <p>Strokes Gained - Expected Scores based on HAndicap Index</p> */}
          </Row>
        </Col>
      </Row>        
      <HoleCardModal tees={TEES} map={MAP} showModal={showModal} setShowModal={setShowModal}/>
    </Container>
  )
}

export default CourseDetails