import { useContext } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import { CurrentPage } from '../../Contexts/CurrentPageContext';

const HandicapCard = ({ handicap }) => {
  const {currentPage, setCurrentPage} = useContext(CurrentPage)

  // paceholder update when model is added
  handicap = {
    INDEX: '2.7',
    LOW: '2.7',
    LOW_DATE: '10/20/2024',
    GHIN: '12253866'


  }

  return (
    <Button variant='danger' className='p-1 my-1 text-center shadow-lg' onClick={e => setCurrentPage('Hanicap')}>
      <Card className='m-0 p-0 w-100 h-100'>
        <Card.Body>
          <Card.Title className='text-center'>Handicap Index</Card.Title>
          <Container fluid>
            <Row className='text-center'>
              <Col xs={12}>
                <h3 className='fs-1 fw-bolder'>{handicap ? handicap.INDEX : 'NH'}</h3>
                <p className='text-muted'>HANDICAP INDEX</p>
              </Col>
            </Row>
           {handicap? (
              <Row className='text-center'>
                <Col sm={6}>
                  <h3>{handicap.LOW}</h3>
                  <p className='text-muted'>LOW INDEX</p>
                </Col>
                <Col sm={6}>
                  <h6>{handicap.LOW_DATE}</h6>
                  <p className='text-muted'>LOW INDEX DATE</p>
                </Col>
              </Row>
            ) : null}
          </Container>
          <Card.Text>
            <small className='text-muted'>***This is not an official Handicap, please consult GHIN {handicap.GHIN ? 'for your offcial handicap' : 'to establish an offical handicap'}***</small>
          </Card.Text>
          <Card.Link className='text-start' target='_blank' href={`https://www.ghin.com/`}>GHIN WEBSITE</Card.Link>
          {/* {facility.GEO_LAT && facility.GEO_LON ? <Card.Link className='text-end' target='_blank' href={`https://www.google.com/maps/place/${facility.GEO_LAT},${facility.GEO_LON}`}>DIRECTIONS</Card.Link> : null } */}
        </Card.Body>
      </Card>
    </Button>
  )
}

export default HandicapCard