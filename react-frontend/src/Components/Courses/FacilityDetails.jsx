import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import Card from "react-bootstrap/Card"

import GetClassification from "../../Functions/GetClassification"
import GetFlag from "../../Functions/GetFlag"

const FacilityDetails = ({ facility }) => {
  const { ADDRESS, CITY, CLASSIFICATION, COUNTRY, COURSE_COUNT, ESTABLISHED, STATE } = facility
  console.log(facility)
  return (
    <Container className='text-center' fluid>
      <Row>
        <Col xs={12} sm={6} xl={4}>
          <h6>{ESTABLISHED}</h6>
          <p className='text-muted'><small>ESTABLISHED</small></p>
        </Col>
        <Col xs={12} sm={6} xl={4}>
          <h6>{COURSE_COUNT}</h6>
          <p className='text-muted'><small>COURSE COUNT</small></p>
        </Col>
        <Col md={6} xl={4}>
          <h6>{GetClassification(CLASSIFICATION)}</h6>
          <p className='text-muted'><small>CLASSIFICATION</small></p>
        </Col>
        <Col sm={12}>
          <h6>{ADDRESS}</h6>
          <p className='text-muted'><small>ADDRESS</small></p>
        </Col>
        <Col xs={12} sm={6}>
          <h6>{CITY}{STATE ? `, ${STATE}` : null}</h6>
          <p className='text-muted'><small>CITY</small></p>
        </Col>
        <Col xs={12} sm={6}>
          <h6>{GetFlag(COUNTRY, 20, 15)}</h6>
          <p className='text-muted'><small>NATION</small></p>
        </Col>
      </Row>
    </Container>
  )
}

export default FacilityDetails