import { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom'
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Row from 'react-bootstrap/Row';
import DatePicker from 'react-datepicker'
import { Typeahead } from 'react-bootstrap-typeahead';

import { CourseList } from '../Contexts/CourseListContext';
import { NationList } from '../Contexts/NationListContext';
import { UserList } from '../Contexts/UserListContext';

import GetCourseOptions from '../Functions/GetCourseOptions';
import GetNationOptions from '../Functions/GetNationOptions';
import CheckUsers from '../Functions/CheckUsers';

const NewUser = () => {
  const { courseList, setCourseList } = useContext(CourseList)
  const { nations, setNations } = useContext(NationList)
  const { userList, setUserList } = useContext(UserList)

  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://localhost:8080'
  
  const navigate = useNavigate();
  let [validated, setValidated] = useState(false)
  let [user, setUser] = useState({
		FIRST_NAME: '',
		LAST_NAME: '',
    USERNAME: '',
		EMAIL: '',
		PASSWORD: '',
    PASSWORD_CONFIRM: '',
    USER_GENDER: 'P',
    DOB: '',
    PLAYER_TYPE: 'A',
    HOME_FACILITY: '',
    NATIONALITY: '',
    units: 'Y'
	})
  let [usernameUnique, setUsernameUnique] = useState(false)
  let [emailUnique, setEmailUnique] = useState(false)
  let [errorMessage, setErrorMessage] = useState(null)

  // validate unique username && email
  const validateUnique = (e, group) => {
    if (group === 'username') {
      setUser({ ...user, USERNAME: e})
      setUsernameUnique(CheckUsers(e, group, userList))
    } else {
      setUser({ ...user, EMAIL: e})
      setEmailUnique(CheckUsers(e, group, userList))
    }
  } 

  // Handle the Submit
  const handleSubmit = async (e) => {
    e.preventDefault()
    // console.log(user)

    setValidated(true);
    // now submit the form
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user)
    }
    
    let response = await fetch(BASE_URL + '/user/', options)
    let data = await response.json()

    if (response.status === 201) {
      localStorage.setItem('golf_token', data.access_token)
      setErrorMessage(null)
      navigate('/')
      location.reload()
    } else {
      setErrorMessage('Account Creation Failed')
    }
  };

  return (
    <Container fluid>
      <h3 className='text-center'>Create New Account</h3>
      { !errorMessage ? null : ( 
        <Row className='text-center rounded border-danger bg-danger-subtle mx-1 my-auto'>
          <p>{errorMessage}</p>
        </Row>
      )
      }
      <Form noValidate validated={validated} onSubmit={(e) => handleSubmit(e)}>
        <Row className='mb-3'>
          <Form.Group as={Col} md={6} controlId='newUserFirstName' className='mb-3' onChange={(e) => setUser({ ...user, FIRST_NAME: e.target.value})}>
            <Form.Label>First name</Form.Label>
            <Form.Control
              type='text'
              placeholder='Enter First name'
              maxLength={20}
            />
          </Form.Group>
          <Form.Group as={Col} md={6} controlId='newUserLastName' className='mb-3' onChange={(e) => setUser({ ...user, LAST_NAME: e.target.value})}>
            <Form.Label>Last name</Form.Label>
            <Form.Control
              type='text'
              placeholder='Enter Last name'
              maxLength={20}
            />
          </Form.Group>
        </Row>
        <Row className='mb-3'>
          <Form.Group as={Col} md={4} controlId='newUserUsername' className='mb-3' onChange={(e) => validateUnique(e.target.value, 'username')}>
            <Form.Label>Username<sup>*</sup></Form.Label>
            <InputGroup hasValidation>
              <Form.Control
                type='text'
                placeholder='Enter Username'
                required
                isInvalid={!usernameUnique}
                maxLength={20}
              />
              <Form.Control.Feedback type='invalid'>
                {usernameUnique === false ? 'Username not available' : 'Please choose a username'}
              </Form.Control.Feedback>
            </InputGroup>
          </Form.Group>
          <Form.Group as={Col} md={8} controlId='newUserEmail' className='mb-3' onChange={(e) => validateUnique(e.target.value, 'email')}>
            <Form.Label>Email<sup>*</sup></Form.Label>
            <Form.Control 
              type='email'
              placeholder='Enter Email'
              required
              isInvalid={!emailUnique}
              maxLength={30} />
            <Form.Control.Feedback type='invalid'>
            {emailUnique === false ? 'Email not available' : ' Please provide a valid email'}
            </Form.Control.Feedback>
          </Form.Group>
          <Form.Group as={Col} md={6} controlId='newUserPasword' className='mb-3' onChange={(e) => setUser({ ...user, PASSWORD: e.target.value})}>
            <Form.Label>Password</Form.Label>
            <Form.Control 
              type='password'
              placeholder='Enter Password'
              required 
              minLength={6}
              maxLength={32}/>
            <Form.Control.Feedback type='invalid'>
              {user.PASSWORD < 6 || user.PASSWORD.length > 32 ? 'Password is too long/short' : 'Please provide a password'}
            </Form.Control.Feedback>
          </Form.Group>
          <Form.Group as={Col} md={6} controlId='newUserPaswordConfirm' className='mb-3' onChange={(e) => setUser({ ...user, PASSWORD_CONFIRM: e.target.value})}>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control 
              type='password' 
              placeholder='Confirm Password'
              required 
              isInvalid={user.PASSWORD !== user.PASSWORD_CONFIRM} />
            <Form.Control.Feedback type='invalid'>
              Passwords do not match
            </Form.Control.Feedback>
          </Form.Group>
        </Row>
        <Row>
          <Form.Group as={Col} md={6} controlId='newUserFacility' className='mb-3'>
          <Form.Label>Home Course</Form.Label>
          <Typeahead
            id='newUserFacility'
            labelKey='Course-Name'
            onChange={e => {
              if ( e[0]) setUser({ ...user,  HOME_FACILITY: e[0].split(' - ')[2]})
              else setUser({ ...user,  HOME_FACILITY: ''})}}
            options={GetCourseOptions(courseList)}
            flip
            minLength={2}
          />
        </Form.Group>
        <Form.Group as={Col} md={6} controlId='newUserNation' className='mb-3'>
            <Form.Label>Nationality</Form.Label>
            <Typeahead
              style={{width: '100%'}}
              id='newUserNation'
              labelKey='Nation-user'
              onChange={e => {
                if ( e[0]) setUser({ ...user,  NATIONALITY: e[0].split(' - ')[1]})
                else setUser({ ...user,  nationality: ''})}}
              options={GetNationOptions(nations.nationObj, false)}
              flip
              minLength={2}
            />
          </Form.Group>
          <Form.Group as={Col} md={4} controlId='newUserGender' className='mb-3' onChange={(e) => setUser({ ...user,  USER_GENDER: e.target.value})}>
            <Form.Label>Gender</Form.Label>
            <Form.Select aria-label='Select User Gender'>
              <option value='P'>Prefer Not To Say</option>
              <option value='M'>Male</option>
              <option value='F'>Female</option>
              <option value='N'>Non-Binary/Other</option>
            </Form.Select>
          </Form.Group>
          <Form.Group as={Col} md={4} controlId='newUsertype' className='mb-3' onChange={(e) => setUser({ ...user,  PLAYER_TYPE: e.target.value})}>
            <Form.Label>Player Type</Form.Label>
            <Form.Select aria-label='Select User Type'>
              <option value='A'>Amatuer</option>
              <option value='C'>College</option>
              <option value='P'>Professional</option>
              <option value='TP'>Tour Professional</option>
            </Form.Select>
          </Form.Group>
          <Form.Group as={Col} md={4} controlId='newUserUnits' className='mb-3' onChange={(e) => setUser({ ...user,  UNITS: e.target.value})}>
            <Form.Label>Player Type</Form.Label>
            <Form.Select aria-label='Select User Units'>
              <option value='Y'>Yards</option>
              <option value='M'>Meters</option>
            </Form.Select>
          </Form.Group>
          <Form.Group as={Col} md={6} controlId='newUserDob' className='mb-3'>
            <Form.Label>Date of Birth</Form.Label>
            <div className='m-0 p-0'>
              <DatePicker 
                className='form-select'
                onChange={(date) => setUser({ ...user,  DOB: new Date(date).toLocaleDateString()})}
                selected={user.DOB}
                maxDate={new Date()}
                showMonthDropdown
                showYearDropdown
                dropdownMode='select'
                onChangeRaw={(e) => setUser({ ...user,  DOB: new Date(e.target.value).toLocaleDateString()})}
              />
            </div>
          </Form.Group>
        </Row> 
        <Button 
        type='submit'
        disabled={user.PASSWORD === null || user.PASSWORD.length < 6 || user.PASSWORD.length > 32 || user.PASSWORD !== user.PASSWORD_CONFIRM || !usernameUnique || !emailUnique}
        >
          Create Account
        </Button>
      </Form>
    </Container>
    );
}

export default NewUser