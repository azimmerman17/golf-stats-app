import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css';

import CurrentUserProvider from './Contexts/CurrentUserContext';

import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import NavBar from './Components/NavBar';
import Footer from './Components/Footer';
import RenderPage from './Components/RenderPage';


const App = () => {
  const [title, setTitle] = useState('APP')
  const [page, setPage] = useState('Home')

  useEffect(() => {
    document.title = 'Golf Statitics App'
  }, [title])

  return (
    <>
      {/* CONTEXT PROVIDERS */}
      <CurrentUserProvider>
        {/* PAGES */}
        <Container fluid>
          <Row className='mb-3'> 
            <NavBar />
          </Row>
          <Row className='p-2 main m-auto mb-5'>
            <RenderPage page={page} setPage={setPage}/>
          </Row>
          <Row>
            <Footer />
          </Row>
        </Container>
        {/* CONTEXT PROVIDERS CLOSE */}
      </CurrentUserProvider>
    </>
  )
}

export default App
