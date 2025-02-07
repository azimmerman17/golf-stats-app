import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css';

import CurrentUserProvider from './Contexts/CurrentUserContext';
import CurrentPageProvider from './Contexts/CurrentPageContext';

import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import NavBar from './Components/NavBar';
import Footer from './Components/Footer';
import RenderPage from './Components/RenderPage';


const App = () => {
  const [title, setTitle] = useState('Golf Statitics App')
  const [page, setPage] = useState('Home')

  useEffect(() => {
    document.title = title
  }, [title])

  return (
    <>
      <Router>
        {/* CONTEXT PROVIDERS */}
        <CurrentPageProvider>

          <CurrentUserProvider>
            {/* PAGES */}
            <Container fluid>
              <Row className='mb-3'> 
                <NavBar setPage={setPage}/>
              </Row>
              <Row className='p-2 main m-auto mb-5'>
                <Routes>
                  <Route exact path='/' element={<RenderPage page={page} setPage={setPage} />} />
                  <Route path='/new' element={<newUser />} />
                  <Route path='/reset' element={<passwordReset />} />
                </Routes>
                
              </Row>
              <Row>
                <Footer setPage={setPage}/>
              </Row>
            </Container>
            {/* CONTEXT PROVIDERS CLOSE */}
          </CurrentUserProvider>
        </CurrentPageProvider>
      </Router>
    </>
  )
}

export default App
