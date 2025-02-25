import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css';

import CurrentUserProvider from './Contexts/CurrentUserContext';
import CurrentPageProvider from './Contexts/CurrentPageContext';
import CourseListProvider from './Contexts/CourseListContext';
import NationListProvider from './Contexts/NationListContext';
import UserListProvider from './Contexts/UserListContext';
import CurrentFacilityProvider from './Contexts/CurrentFacilityContext';

import NavBar from './Components/NavBar';
import Footer from './Components/Footer';
import RenderPage from './Components/RenderPage';
import NewUser from './Components/NewUser';



const App = () => {
  const [title, setTitle] = useState('Golf Statitics App')

  useEffect(() => {
    document.title = title
  }, [title])

  return (
    <>
      <Router>
        {/* CONTEXT PROVIDERS */}
        <CurrentPageProvider>
          <CurrentUserProvider>
            <UserListProvider>
              <CourseListProvider>
                <CurrentFacilityProvider>
                  <NationListProvider>
                    {/* PAGES */}
                    <Container fluid>
                      <Row className='mb-3'> 
                        <NavBar />
                      </Row>
                      <Row className='p-2 main m-auto mb-5'>
                        <Routes>
                          <Route exact path='/' element={<RenderPage />} />
                          <Route path='/new' element={<NewUser />} />
                          {/* <Route path='/reset' element={<PasswordReset />} /> */}
                        </Routes>
                        
                      </Row>
                      <Row>
                        <Footer />
                      </Row>
                    </Container>
                  {/* CONTEXT PROVIDERS CLOSE */}
                  </NationListProvider>
                </CurrentFacilityProvider>
              </CourseListProvider>
            </UserListProvider>
          </CurrentUserProvider>
        </CurrentPageProvider>
      </Router>
    </>
  )
}

export default App
