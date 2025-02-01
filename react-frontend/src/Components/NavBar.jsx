import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Offcanvas from 'react-bootstrap/Offcanvas';

import GetIcon from '../Functions/getIcon';

const NavBar = () => {
  let currentUser = false

  const headers = ['Rounds', 'Stats', 'Records', 'Courses', 'Profile', 'Logout']

  const loggedOutNav = () => {
    return (
      <Nav varient='light' title='Log in/Sign up' id='logged-out-dropdown' className='text-white'>
        {/* <Login /> */}
        Login
      </Nav>
    )
  }

  const loggedInNav = headers.map(header => {
      return (
        <Nav.Link href={`/${header}`} className='py-1' key={`navbar-${header}`}>
          <h5 className='text-white'>
            {GetIcon(header)} {header}
          </h5>
        </Nav.Link>
      )
    })


  return (
    <Navbar bg='danger' variant='danger' sticky="top" expand='xxl' className='m-0'>
      <Container className='mx-3 main' fluid>
        <Navbar.Toggle className='text-white bg-white' aria-controls='basic-navbar-nav' />
        <Navbar.Brand className='text-white' href='/'>
          <h3>Golf Statistics Tracker</h3>
        </Navbar.Brand>
        <Navbar.Offcanvas id='offcanvasNavbar' aria-labelledby='offcanvasNavbar' placement='start'>
          <Offcanvas.Header closeButton className='bg-danger text-white'>
            <Offcanvas.Title id='offcanvasNavbar' className='fs-4 fw-bolder'>
              {currentUser ? `Welcome ${currentUser.first_name}` : 'Welcome'}
            </Offcanvas.Title>
          </Offcanvas.Header>
          <Offcanvas.Body className='bg-danger' as={Container}>
            {currentUser ? loggedInNav : loggedOutNav() }
          </Offcanvas.Body>
        </Navbar.Offcanvas>
      </Container>
    </Navbar>
  )
}

export default NavBar