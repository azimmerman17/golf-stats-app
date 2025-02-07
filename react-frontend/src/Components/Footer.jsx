import { useContext } from 'react' 

import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';

import { CurrentPage } from '../Contexts/CurrentPageContext';

const Footer = () => {
  const { currentPage, setCurrentPage } = useContext(CurrentPage)

  return (
    <Navbar fixed='bottom' bg='danger' varient='white' className='footer m-0'>
      <Container fluid >
        <Row>
          <Col className='footer m-0 px-2 text-center'>
            <Button onClick={e=>setCurrentPage('about')} variant='link' className='m-1 p-1 text-white text-center'>About Us</Button>
          </Col>
        </Row>
        <Row>
          <a href='/' className='m-1 p-1 text-white text-decoration-none'>Golf Statistics App</a>
        </Row>
      </Container>
    </Navbar>
  )

}

export default Footer