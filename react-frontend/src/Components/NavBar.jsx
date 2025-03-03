import { useContext, useState } from 'react' 
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Offcanvas from 'react-bootstrap/Offcanvas';
import GetIcon from '../Functions/getIcon';

import { CurrentUser } from '../Contexts/CurrentUserContext'
import { CurrentPage } from '../Contexts/CurrentPageContext';

import Login from './Login';

const NavBar = () => {
  const { currentUser, setCurrentUser } = useContext(CurrentUser) 
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const [expanded, setExpanded] = useState(false)

  const headers = ['Rounds', 'Handicap', 'Stats', 'Records', 'Courses', 'Profile', 'Logout']

  const loggedOutNav = () => {
    return (
      <Nav varient='light' title='Log in/Sign up' id='logged-out-dropdown' className='text-white'>
        <Login variant={'light'}/>
      </Nav>
    )
  }

  const loggedInNav = headers.map(header => {
    const handleClick = (page) => {
      setCurrentPage(page)
      setExpanded(!expanded)

    }

    return (
      <Nav.Link className='py-1' key={`navbar-${header}`} onClick={e=> handleClick(header)}>
        <h5 className='text-white'>
          {GetIcon(header)} {header}
        </h5>
      </Nav.Link>
    )
  })


  return (
    <Navbar bg='danger' variant='danger' sticky='top' expand='xxxl' className='m-0' expanded={expanded}>
      <Container className='mx-3 main' fluid>
        <Navbar.Toggle className='text-white bg-white' aria-controls='basic-navbar-nav' onClick={() => setExpanded(!expanded)}/>
        <Navbar.Brand className='text-white' href='/'>
          <h3>Golf Statistics Tracker</h3>
        </Navbar.Brand>
        <Navbar.Offcanvas id='offcanvasNavbar' aria-labelledby='offcanvasNavbar' placement='start'>
          <Offcanvas.Header closeButton className='bg-danger text-white'  onClick={() => setExpanded(!expanded)}>
            <Offcanvas.Title id='offcanvasNavbar' className='fs-4 fw-bolder'>
              {currentUser ? `Welcome ${currentUser.FIRST_NAME}` : 'Welcome'}
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