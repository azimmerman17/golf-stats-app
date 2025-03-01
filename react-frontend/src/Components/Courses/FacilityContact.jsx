import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import FacilityMap from '../Maps/FacilityMap'

const FacilityContact = ({ facility }) => {
  const { ADDRESS, CITY, COUNTRY, FACILITY_ID, GEO_LAT, GEO_LON, STATE, WEBSITE, NAME } = facility

  return (
    <Container>
      <Row className='m-4'>
        <Col className='text-center'>
          <h6>{ADDRESS}</h6>
          <p className='text-muted'><small>ADDRESS</small></p>
        </Col>
        <Col className='text-center'>
          <h6><a href={`https://${WEBSITE}`} target='_blank'>{WEBSITE}</a></h6>
          <p className='text-muted'><small>COURSE WEBSITE</small></p>
        </Col>
      </Row>
      <Row>
        <h6 className='text-center mb-4'>
          <a  className='text-black' href={`https://www.google.com/maps/dir//${NAME}+${ADDRESS}`} target='_blank'>Get Directions</a>
        </h6>
        <FacilityMap GEO_LAT={GEO_LAT} GEO_LON={GEO_LON} FACILITY_ID={FACILITY_ID} NAME={NAME} />

      </Row>





    </Container>
  )

}

export default FacilityContact