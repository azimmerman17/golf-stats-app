import Accordion from 'react-bootstrap/Accordion';
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import GetClassification from '../../Functions/GetClassification'
import FacilityCourseCard from './FacilityCourseCard';
import Button from 'react-bootstrap/Button';


const CoursesHomeTab = ({ facility, courses, setCurrentCourse, setCurrentTab }) => {
  const { CITY, CLASSIFICATION, COUNTRY, COURSE_COUNT, ESTABLISHED, FACILITY_ID,  NAME, STATE } = facility
  
  const facilityCourses = courses.map(course => {

    const handleClick = (course) => {
      setCurrentCourse(course)
      setCurrentTab('Course')
    }

    return (
      <Col md={6} key={course.NAME}>
        <Button onClick={e => handleClick(course)} className='rounded mb-3' variant='danger'>
          <FacilityCourseCard course={course}/>
        </Button>
      </Col>
    )
  })
  

  return (
    <Accordion defaultActiveKey={['0', '1']} alwaysOpen>
      <Accordion.Item eventKey='0' >
        <Accordion.Header>Facility Details</Accordion.Header>
        <Accordion.Body>
          <Row className='m-3'>
            <Col xs={6}  md={4} className='text-center'>
              <h6>{ESTABLISHED}</h6>
              <p className='text-muted'><small>ESTABLISHED</small></p>
            </Col>
            <Col xs={6} md={4} className='text-center'>
              <h6>{GetClassification(CLASSIFICATION)}</h6>
              <p className='text-muted'><small>CLASSIFICATION</small></p>
            </Col>
            <Col xs={6}  md={4} className='text-center'>
              <h6>{COURSE_COUNT}</h6>
              <p className='text-muted'><small>COURSE COUNT</small></p>
            </Col>
            <Col xs={6}  md={4} className='text-center'>
              <h6>{CITY}</h6>
              <p className='text-muted'><small>CITY</small></p>
            </Col>
            <Col xs={6} md={4} className='text-center'>
              <h6>{STATE}</h6>
              <p className='text-muted'><small>STATE</small></p>
            </Col>
            <Col xs={6}  md={4} className='text-center'>
              <h6>{COUNTRY}</h6>
              <p className='text-muted'><small>COUNTRY</small></p>
            </Col>
          </Row>
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey='1'>
        <Accordion.Header>Courses</Accordion.Header>
        <Accordion.Body>
          <Row>
            {facilityCourses}
          </Row>
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
  )
}
export default CoursesHomeTab

