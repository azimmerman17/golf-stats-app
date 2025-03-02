import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import FacilityCourseCard from '../FacilityCourseCard';
import Button from 'react-bootstrap/Button';
import CourseDetails from './CourseDetails';
import Breadcrumb from 'react-bootstrap/Breadcrumb'


const CourseTabHome = ({ currentCourse, setCurrentCourse, courses }) => {
  console.log(currentCourse)
  if (!currentCourse) {
    const facilityCourses = courses.map(course => {

      const handleClick = (course) => {
        setCurrentCourse(course)
      }
  
      return (
        <Col md={6} key={course.NAME}>
          <Button onClick={e => handleClick(course)} className='rounded my-3' variant='danger'>
            <FacilityCourseCard course={course}/>
          </Button>
        </Col>
      )
    })

    return (
      <Container fluid>
        <Row>
          {facilityCourses}
        </Row>
      </Container>
    )
  }
console.log(courses)

  return (
    <>
      { courses.length > 1 ? (
        <Breadcrumb>
          <Breadcrumb.Item onClick={e => setCurrentCourse(null)}>{`< Select Different Course`}</Breadcrumb.Item>
        </Breadcrumb>) : null 
      }
      <CourseDetails course={currentCourse}  />
    </>
  )
}

export default CourseTabHome