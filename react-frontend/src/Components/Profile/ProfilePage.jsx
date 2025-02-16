import { useContext, useState } from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/esm/Button';
import { FaTrash } from "react-icons/fa6";
import { FaEdit } from "react-icons/fa";

import { CurrentUser } from '../../Contexts/CurrentUserContext';
import { CurrentPage } from '../../Contexts/CurrentPageContext';

import Breadcrumbs from '../Breadcrumbs';
import ProfileHome from './ProfileHome';
import HomeCourseCard from '../Courses/HomeCourseCard';
import ProfileInfoCard from './ProfileInfoCard';

const ProfilePage = () => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)
  const {currentPage, setCurrentPage} = useContext(CurrentPage)

  const breadcrumbList = [
    {name: 'Home', change: '', active: true},
    {name: 'Profile', change: 'profile', active: false}
  ]


// DOB"Thu, 17 Mar 1994 00:00:00 GMT"
// HOME_FACILITY{COURSES: Array(1), FACILITY: {…}}
// ROLE"basic"
// UNITS"Y"
// USER_GENDER"M"

  return (
    <div>
      <Breadcrumbs list={breadcrumbList} />
      <ProfileHome />
      <Row>
        <Col md={6} className='text-center mb-4'>
          <HomeCourseCard facility={currentUser.HOME_FACILITY.FACILITY} active={false} />
          <Row className='mx-2'>
            <Button variant='danger' onClick={e => setCurrentPage('Courses')}>
              View Home Facility
            </Button>
          </Row>
        </Col>
        <Col md={6}>
          <ProfileInfoCard currentUser={currentUser} />
          <Row className='text-end mx-2'>
            <Button variant='warning' className='my-1' onClick={e => console.log('EDIT')}>
              <FaEdit />
            </Button>
            <Button variant='danger' className='text-light my-1' onClick={e => console.log('DELETE')}>
              <FaTrash />
            </Button>
          </Row>
        </Col>
      </Row>
 

      
    </div>
  )
}

export default ProfilePage