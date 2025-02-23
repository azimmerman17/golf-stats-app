import { useContext } from "react"
import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

import { CourseList } from "../../Contexts/CourseListContext"
import CourseCard from "./CourseCard"
import Breadcrumbs from "../Breadcrumbs"

const CoursesHome = () => {
  const { courseList, setCoureList } = useContext(CourseList)

  const breadcrumbList = [
    {name: 'Home', change: '', active: true},
    {name: 'Course', change: 'Courses', active: false}
  ]

  const courseCards = courseList.map(course => {
    return (
      <Col>
        <CourseCard course={course} />
      </Col>
    )
  })

  return (
    <Container fluid>
      <Breadcrumbs list={breadcrumbList} />
      <Row>
        {courseCards}
      </Row>
    </Container>
  )
}

export default CoursesHome