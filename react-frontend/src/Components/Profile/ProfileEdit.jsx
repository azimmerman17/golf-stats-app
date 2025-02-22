import { useState, useContext, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Offcanvas from 'react-bootstrap/Offcanvas';
import { Typeahead } from 'react-bootstrap-typeahead';
import DatePicker from 'react-datepicker'

import { CourseList } from '../../Contexts/CourseListContext';
import { NationList } from "../../Contexts/NationListContext";
import { UserList } from '../../Contexts/UserListContext';

import GetCourseOptions from '../../Functions/GetCourseOptions';
import GetNationOptions from '../../Functions/GetNationOptions';
import CheckUsers from '../../Functions/CheckUsers';
import GetNation from '../../Functions/GetNation';
import GetHomeFacility from '../../Functions/GetHomeFacility';

const ProfileEdit = ({ showEdit, setShowEdit, currentUser, setCurrentUser }) => {
  const { courseList, setCourseList } = useContext(CourseList)
  const { nations, setNations } = useContext(NationList)
  const { userList, setUserList } = useContext(UserList)
  const [editUser, setEditUser] = useState({})
  const [usernameUnique, setUsernameUnique] = useState(false)
  const [emailUnique, setEmailUnique] = useState(false)
  const [errorMessage, setErrorMessage] = useState(null)
  let [validated, setValidated] = useState(false)

  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://localhost:8080'

  // validate unique username && email
  const validateUnique = (e, group) => {
    if (group === 'username') {
      setEditUser({ ...editUser, USERNAME: e})
      setUsernameUnique(CheckUsers(e, group, userList))
    } else {
      setEditUser({ ...editUser, EMAIL: e})
      setEmailUnique(CheckUsers(e, group, userList))
    }
  } 

  // submit the form
  const handleSubmit = async (e) => {
    
    e.preventDefault()
    setValidated(true)

    const options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(editUser)
    }
    
    let response = await fetch(BASE_URL + '/user/' + currentUser.USER_ID, options)
    let data = await response.json()

    if (response.status >= 400) {
      setErrorMessage(data.message)
    } else {
      setErrorMessage('Profile successfully updated')
      const { user } = data
      user.HOME_FACILITY = await GetHomeFacility(user.HOME_FACILITY)
      user.NATION = await GetNation(user.NATIONALITY)
      setCurrentUser(user)
      setEditUser({})
    }
  }

  return (
    <Offcanvas show={showEdit} scroll={true} onHide={e => setShowEdit(false)} className='bg-secondary-subtle'>
    <Offcanvas.Header className='bg-danger text-white' closeButton>
      <Offcanvas.Title className='fs-3 m-auto'>Edit Profile Data</Offcanvas.Title>
    </Offcanvas.Header>
    <Offcanvas.Body className='m-2 shadow rounded bg-white'>
      <Form noValidate validated={validated} onSubmit={(e) => handleSubmit(e)}>
        <Form.Group controlId='editUserFirstName' className='mb-2' onChange={(e) => setEditUser({ ...editUser, FIRST_NAME: e.target.value})}>
          <Form.Label>First name</Form.Label>
          <Form.Control
            type='text'
            placeholder={currentUser.FIRST_NAME}
            maxLength={20}
          />
        </Form.Group>
        <Form.Group controlId='editUserLastName' className='mb-2' onChange={(e) => setEditUser({ ...editUser, LAST_NAME: e.target.value})}>
          <Form.Label>Last name</Form.Label>
          <Form.Control
            type='text'
            placeholder={currentUser.LAST_NAME}
            maxLength={20}
          />
        </Form.Group>
        <Form.Group controlId='editUserUsername' className='mb-2' onChange={(e) => validateUnique(e.target.value, 'username')}>
          <Form.Label>Username</Form.Label>
          <InputGroup hasValidation>
            <Form.Control
              type='text'
              placeholder={currentUser.USERNAME}
              isInvalid={!usernameUnique && !currentUser.USERNAME}
              maxLength={20}
            />
            </InputGroup>
        </Form.Group>
        <Form.Group controlId='editUserEmail' className='mb-2' onChange={(e) => validateUnique(e.target.value, 'email')}>
          <Form.Label>Email</Form.Label>
          <Form.Control 
            type='email'
            placeholder={currentUser.EMAIL}
            isInvalid={!emailUnique  && !currentUser.EMAIL}
            maxLength={30} />
          <Form.Control.Feedback type='invalid'>
          {usernameUnique === false ? 'Email not available' : ' Please provide a valid email'}
          </Form.Control.Feedback>
        </Form.Group>
        <Form.Group controlId='editUserFacility' className='mb-2'>
          <Form.Label>Home Course</Form.Label>
          <Typeahead
            id='editUserFacility'
            labelKey='Course-Name'
            onChange={e => {
              if ( e[0]) setEditUser({ ...editUser,  HOME_FACILITY: e[0].split(' - ')[2]})
              else setEditUser({ ...editUser,  HOME_FACILITY: ''})}}
            options={GetCourseOptions(courseList)}
            placeholder={currentUser.HOME_FACILITY.FACILITY.NAME}
            flip
            minLength={2}
          />
        </Form.Group>
        <Form.Group controlId='editUserNation' className='mb-2'>
          <Form.Label>Nationality</Form.Label>
          <Typeahead
            style={{width: '100%'}}
            id='editUserNation'
            labelKey='Nation-user'
            placeholder={currentUser.NATIONALITY}
            onChange={e => {
              if ( e[0]) setEditUser({ ...editUser,  NATIONALITY: e[0].split(' - ')[1]})
              else setEditUser({ ...editUser,  NATIONALITY: ''})}}
            options={GetNationOptions(nations.nationObj, false)}
            flip
            minLength={2}
          />
        </Form.Group>
        <Form.Group controlId='editUserGender' className='mb-2' onChange={(e) => setEditUser({ ...editUser,  USER_GENDER: e.target.value})}>
          <Form.Label>Gender</Form.Label>
          <Form.Select aria-label='Select User Gender' value={editUser.USER_GENDER ? editUser.USER_GENDER : currentUser.USER_GENDER}>
            <option value='P'>Prefer Not To Say</option>
            <option value='M'>Male</option>
            <option value='F'>Female</option>
            <option value='N'>Non-Binary/Other</option>
          </Form.Select>
        </Form.Group>
        <Form.Group controlId='editUsertype' className='mb-2' onChange={(e) => setEditUser({ ...editUser,  PLAYER_TYPE: e.target.value})}>
          <Form.Label>Player Type</Form.Label>
          <Form.Select aria-label='Select User Type' value={editUser.PLAYER_TYPE ? editUser.PLAYER_TYPE : currentUser.PLAYER_TYPE}>
            <option value='A'>Amatuer</option>
            <option value='C'>College</option>
            <option value='P'>Professional</option>
            <option value='TP'>Tour Professional</option>
          </Form.Select>
        </Form.Group>
        <Form.Group controlId='editUserUnits' className='mb-2' onChange={(e) => setEditUser({ ...editUser,  UNITS: e.target.value})}>
          <Form.Label>Player Type</Form.Label>
          <Form.Select aria-label='Select User Units' value={editUser.UNITS ? editUser.UNITS : currentUser.UNITS}>
            <option value='Y'>Yards</option>
            <option value='M'>Meters</option>
          </Form.Select>
        </Form.Group>
        <Form.Group controlId='editUserDob' className='mb-2'>
          <Form.Label>Date of Birth</Form.Label>
          <div className='m-0 p-0'>
            <DatePicker 
              className='form-select'
              onChange={(date) => setEditUser({ ...editUser,  DOB: new Date(date).toLocaleString()})}
              selected={editUser.DOB ? editUser.DOB : currentUser.DOB}
              maxDate={new Date()}
              showMonthDropdown
              showYearDropdown
              dropdownMode="select"
              onChangeRaw={(e) => setEditUser({ ...editUser,  DOB: new Date(e.target.value).toLocaleString()})}
            />
          </div>
        </Form.Group>
        <Button type='submit' disabled={usernameUnique || emailUnique}>
          Save Changes
        </Button>
      </Form>
      <p className='text-center rounded border-danger bg-danger-subtle m-2'> 
        {!errorMessage ? null : errorMessage }
      </p>
    </Offcanvas.Body>
  </Offcanvas>
  )
}

export default ProfileEdit