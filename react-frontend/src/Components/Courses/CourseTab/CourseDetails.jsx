import { useEffect, useState } from "react"
import Container from "react-bootstrap/esm/Container"
import Row from "react-bootstrap/esm/Row"
import Col from "react-bootstrap/esm/Col"

import FacilityCourseCard from "../FacilityCourseCard"
import CourseTeeCard from "./CourseTeeCard"

const CourseDetails = ({ course }) => {
  const [ selectedTee, setSelectedTee ] = useState(course.TEES[0].NAME)
  const { TEES } = course
  
  useEffect(() => {
    if (!selectedTee && TEES) {
      setSelectedTee(TEES[0].NAME)
    }
    console.log(selectedTee)
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
            <p>Holes - Card with hole overview maybe satalite overview??</p>
            <p>Course Stats - Change with the tee offer base information - maybe combine with handicap?</p>
          </Row>
        </Col>
      </Row>
      Course Details
      </Container>
  )
}

export default CourseDetails