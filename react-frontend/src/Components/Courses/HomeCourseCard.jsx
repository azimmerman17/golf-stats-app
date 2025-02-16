import { useContext } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import FacilityDetails from './FacilityDetails';

import { CurrentPage } from '../../Contexts/CurrentPageContext';

const HomeCourseCard = ({ facility, active }) => {
  const {currentPage, setCurrentPage} = useContext(CurrentPage)

  return (
    <Button variant='danger' className='p-1 my-1 text-center shadow-lg' disabled={!active} onClick={e => setCurrentPage('Home Course')}>
      <Card className='m-0 p-0 w-100 h-100'>
        <Card.Body>
          <Card.Title className='text-center'>{facility ? facility.NAME : null}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted"><small>{facility ? 'HOME COURSE' : null}</small></Card.Subtitle>
          {facility ? <FacilityDetails facility={facility} /> : (
            <Card.Text>
              No home course is set, click to set a home course
            </Card.Text>
            )
          }
          {facility.WEBSITE ? <Card.Link className='text-start' target='_blank' href={`https://${facility.WEBSITE}`}>WEBSITE</Card.Link> : null}
          {facility.GEO_LAT && facility.GEO_LON ? <Card.Link className='text-end' target='_blank' href={`https://www.google.com/maps/place/${facility.GEO_LAT},${facility.GEO_LON}`}>DIRECTIONS</Card.Link> : null }
        </Card.Body>
      </Card>
    </Button>
  )
}

export default HomeCourseCard