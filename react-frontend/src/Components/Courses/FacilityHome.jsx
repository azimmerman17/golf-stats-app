import { useContext, useEffect, useState } from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Nav from 'react-bootstrap/Nav';

import { CurrentFacility } from '../../Contexts/CurrentFacilityContext';

import Breadcrumbs from '../Breadcrumbs'
import FacilityContact from './FacilityContact';
import Image from 'react-bootstrap/esm/Image';


const FacilityHome = () => { 
  const {  currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const [ courseName, setCourseName] = useState(null)
  const [ currentTab, setCurrentTab ] = useState('Home')

  useEffect(() => {
    if (currentFacility.FACILITY) {
      const { NAME } = currentFacility.FACILITY
      setCourseName(NAME)
    }
  }, [currentFacility])

  const breadcrumbList = [
    {name: 'Home', change: '', active: true},
    {name: 'Course', change: 'Courses', active: true},
    {name: `${courseName}`, change: 'Facility', active: false}
  ]

  const tabs = [
    'Home',
    'Courses',
    // 'Records',
    'Contact Info'
  ]

  const tabLinks = tabs.map(tab => {
    return (
      <Nav.Item key={`course-navtab-${tab}`}>
          <Nav.Link className={`bg-danger${currentTab === tab ? ' text-white border-black border-2 fw-bold' :'-subtle text-black border-bottom'} rounded--top`}  onClick={e => setCurrentTab(tab)}>{tab}</Nav.Link>
      </Nav.Item>
    )
  })

  const view = (tab) => {
    switch (tab) {
      case 'Home':
        return tab
      case 'Courses':
        return tab
      // case 'Records':
      // return tab
      // case 'Stats':
      // return tab
      case 'Contact Info':
        return <FacilityContact facility={currentFacility.FACILITY} />
    }
  }

  const header = (facility) => {
    if (facility) {
      const { HANDLE, NAME } = facility
      return (
        <Row>
          <Col sm={2}>
            <Image src={`https://logos.bluegolf.com/${HANDLE}/profile.png` || `${golferLogo}` } alt={`${NAME} Logo`} style={{ maxWidth: '100px'}} className='m-auto'/>
          </Col>
          <Col className='align-bottom'>
            <h2 className='m-2 text-center align-text-bottom'>{NAME}</h2>
          </Col>
          <Col sm={2}>
          </Col>
        </Row>

      )
    }
  }

  return (
    <Container fluid>
      <Breadcrumbs list={breadcrumbList} />
      {header(currentFacility.FACILITY)}
      <Nav justify variant='tabs' className='border-bottom border-black border-3 p-1' defaultActiveKey='Home' activeKey={currentTab}>
        {tabLinks}
      </Nav>
      {view(currentTab)}
    </Container>
  )
}

export default FacilityHome