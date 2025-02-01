import { useState } from 'react'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Row';


import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import NavBar from './Components/NavBar'

function App() {

  return (
    <Container fluid>
      <Row className='mb-3'> 
        <NavBar />
      </Row>
      <Row className='p-2 main m-auto'>
          Page Content
      </Row>
     

      <Row>
          <Col sm={2}>
            <a href="https://vite.dev" target="_blank">
              <img src={viteLogo} className="logo-icon vite" alt="Vite logo" />
            </a>
          </Col>
          <Col sm={2}>
            <a href="https://react.dev" target="_blank">
              <img src={reactLogo} className="logo-icon react" alt="React logo" />
            </a>
          </Col>
      </Row>
    </Container>

  )
}

export default App
