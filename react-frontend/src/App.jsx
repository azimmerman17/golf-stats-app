import { useState } from 'react'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Row';


import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import NavBar from './Components/NavBar'
import Footer from './Components/Footer';

function App() {

  return (
    <Container fluid>
      <Row className='mb-3'> 
        <NavBar />
      </Row>
      <Row className='p-2 main m-auto mb-5'>
          Page Content
      </Row>
     

      <Row>
          <Footer />
      </Row>
    </Container>

  )
}

export default App
