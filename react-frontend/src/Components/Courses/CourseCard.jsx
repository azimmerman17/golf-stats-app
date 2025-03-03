import { useContext } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import FacilityDetails from './FacilityDetails';

import { CurrentPage } from '../../Contexts/CurrentPageContext';
import { CurrentFacility } from '../../Contexts/CurrentFacilityContext'

import golferLogo from '/golfer.svg'

const CourseCard = ({ course })  => {
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const { currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const { HANDLE, NAME, FACILITY_ID } = course

  const handleClick = (id) => {
    setCurrentFacility(id)
    setCurrentPage('Facility')
  }

  return (
    <Button variant='danger' className='p-1 m-2 text-center shadow-lg' onClick={e => handleClick(FACILITY_ID)}>
      <Card>
        <Card.Img variant='top' src={`https://logos.bluegolf.com/${HANDLE}/profile.png` || `${golferLogo}` } alt={`${NAME} Logo`} style={{ width: '100px'}} className='m-auto'/>
        <Card.Body>
          <Card.Title className='text-center'>{NAME}</Card.Title>
            <FacilityDetails facility={course} />
        </Card.Body>
      </Card>
    </Button>
  )
}

export default CourseCard