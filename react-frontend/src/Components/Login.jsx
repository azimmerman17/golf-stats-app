import { useContext, useState } from 'react';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/esm/Row';
import Col from 'react-bootstrap/esm/Col';
import Container from 'react-bootstrap/esm/Container';
import Button from 'react-bootstrap/Button';

import { CurrentUser } from '../Contexts/CurrentUserContext'
import { CurrentPage } from '../Contexts/CurrentPageContext';



const Login = ({ variant }) => {
  // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://127.0.0.1:8080'
  const { currentUser, setCurrentUser } = useContext(CurrentUser)
  const { currentPage, setCurrentPage } = useContext(CurrentPage)

  let [validated, setValidated] = useState(false)
  let [errorMessage, setErrorMessage] = useState(null)
  let [user, setUser] = useState({
    user_name: '',
    password: ''
  })
  if (!variant) variant = 'danger'

  // Handle the Submit
  const handleSubmit = async (e) => {
    const form = e.currentTarget;
    e.preventDefault()

    if (form.checkValidity() === false) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    setValidated(true);

    // now submit the form
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'mode': 'cors',
        'USERNAME': user.user_name,
        'PASSWORD': user.password
      },
    }

    let response = await fetch(BASE_URL + '/auth/login', options)

    const data = await response.json()

    if (response.status === 200) {
      setCurrentUser(data.user)
      localStorage.setItem('golf_token', data.access_token)
      setErrorMessage(null)
      setCurrentPage('Home')
      location.reload()
    } else {
      setErrorMessage(data.message)
    }
  };

  return (
    <Container id='log-in-form' style={{maxidth: '300px'}}>
      {!errorMessage ? <p style={{minHeight: '30px'}}></p> : <p className={`m-2 p-2 bg-${variant}-subtle border border-danger text-center rounded-pill`}>{errorMessage}</p>}
      <Form noValidate validated={validated} onSubmit={handleSubmit}>
        <Form.Group className='mb-3 login-form-group' as={Col}  controlId='loginUserNameEmail' onChange={e => setUser({...user, user_name: e.target.value })}>
          <Form.Label>Username or Email Address</Form.Label>
          <Form.Control 
            type='text' 
            placeholder='Enter Username or Email Address' 
            required/>
        </Form.Group>
        <Form.Group className='mb-3 login-form-group'  as={Col} controlId='loginPassword' onChange={e => setUser({...user, password: e.target.value })}>
          <Form.Label>Password</Form.Label>
          <Form.Control 
            type='password' 
            placeholder='Enter Password' 
            required/>
        </Form.Group>
        <Button variant={variant} type='submit' disabled={user.password === '' || user.user_name === ''}>
          Submit
        </Button>
      </Form>
      <hr />
      <Row>
        <Col>
          <a href='/new' className={`text-${variant}`}>Create Account</a>
        </Col>
        <Col>
          <a href='/reset' className={`text-${variant}`}>Forgot Password</a>
        </Col>
      </Row>
    </Container>
  );
}

export default Login