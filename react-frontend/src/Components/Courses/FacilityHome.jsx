import { useContext, useEffect, useState } from 'react';
import Container from "react-bootstrap/Container"

import { CurrentFacility } from '../../Contexts/CurrentFacilityContext';

import Breadcrumbs from "../Breadcrumbs"


const FacilityHome = () => { 
  const {  currentFacility, setCurrentFacility } = useContext(CurrentFacility)
  const [ courseName, setCourseName] = useState(null)

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

  

  console.log(currentFacility)
 
  return (
    <Container fluid>
      <Breadcrumbs list={breadcrumbList} />

      FACILITY HOME
    </Container>
  )
}

export default FacilityHome