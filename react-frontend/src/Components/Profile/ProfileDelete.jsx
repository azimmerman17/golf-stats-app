import { useState } from 'react';
import Form from 'react-bootstrap/Form';
import Offcanvas from 'react-bootstrap/Offcanvas';
import Button from 'react-bootstrap/Button';

const ProfileDelete = ({ id, username, showDelete, setShowDelete, setCurrentUser, setCurrentPage }) => {
  const [checkUsername, setCheckUsername] = useState('')
  const [errorMessage, setErrorMessage] = useState(null)

    // const BASE_URL = import.meta.env.VITE_BASE_URL
  const BASE_URL = 'http://localhost:8080'

  const handleClose = () => {
    setCheckUsername('')
    setShowDelete(false)
  }

  const handleSubmit = async (id) => {
    console.log(id)
    if (username !== checkUsername) setErrorMessage('Username does not match')

    const options = {
      method: 'DELETE',
    }

    let response = await fetch(BASE_URL + '/user/' + id, options)
    let data = await response.json()
    console.log(response, data)

    if (response.status >= 400) setErrorMessage('Account Deletion Failed')
    else {
      setCurrentUser({})
      setCurrentPage('Home')
      localStorage.removeItem('golf_token')
    }
  }

  return (
    <Offcanvas show={showDelete} scroll={true} onHide={e => handleClose()} className='bg-secondary-subtle'>
      <Offcanvas.Header className='bg-danger text-white' closeButton>
        <Offcanvas.Title className='fs-3 m-auto'>DELETE ACCOUNT</Offcanvas.Title>
      </Offcanvas.Header>
      <Offcanvas.Body className='m-2 shadow rounded bg-white'>
        <Form  noValidate onSubmit={(e) => handleSubmit(id)}>
          <Form.Group controlId='deleteUserUsername' className='mb-2' onChange={(e) => setCheckUsername(e.target.value)}>
            <Form.Label>ENTER YOUR USERNAME</Form.Label>
              <Form.Control
                type='text'
                placeholder='Enter your username to delete your account'
                maxLength={20}
              />
          </Form.Group>
          <Button type='submit' disabled={checkUsername !== username} variant='danger'>
            DELETE ACCOUNT
          </Button >
        </Form>
        <p className='text-center rounded border-danger bg-danger-subtle m-2'> 
          {!errorMessage ? null : errorMessage }
        </p>
      </Offcanvas.Body>
    </Offcanvas>
  )
}

export default ProfileDelete