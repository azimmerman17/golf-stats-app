import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import FacilityDetails from './FacilityDetails';

import golferLogo from '/golfer.svg'

const CourseCard = ({ course })  => {
  const { HANDLE, NAME } = course

  return (
    <Button variant='danger' className='p-1 m-2 text-center shadow-lg'>
      <Card  >
        <Card.Img variant="top" src={`https://logos.bluegolf.com/${HANDLE}/profile.png` || `${golferLogo}` } alt={`${NAME} Logo`} style={{ width: '100px'}} className='m-auto'/>
        <Card.Body>
          <Card.Title className='text-center'>{NAME}</Card.Title>
            <FacilityDetails facility={course} />
        </Card.Body>
      </Card>
    </Button>
  )
}

export default CourseCard