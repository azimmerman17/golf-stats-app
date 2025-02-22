import { useState, useEffect } from "react"
import Card from "react-bootstrap/Card"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

import GetFlag from "../../Functions/GetFlag"
import GetPlayerType from "../../Functions/GetPlayerType"
import GetGender from "../../Functions/GetGender"

const ProfileInfoCard = ({ currentUser }) => {
  const { DOB, ROLE, UNITS, USER_GENDER,  EMAIL, NATIONALITY, PLAYER_TYPE, USERNAME, NATION} = currentUser

  return (
    <Card className='mx-auto my-1 p-2 border border-5 border-danger rounded-3 shadow-lg '>
      <Card.Body>
        <Row>
          <Col sm={6} className='text-center'>
              <h6>{EMAIL}</h6>
              <p className='text-muted'><small>EMAIL</small></p>
          </Col>
          <Col sm={6} className='text-center'>
              <h6>{USERNAME}</h6>
              <p className='text-muted'><small>USERNAME</small></p>
          </Col>
          <Col sm={6} className='text-center'>
              <h6>N/A</h6>
              <p className='text-muted'><small>GHIN NUM</small></p>
          </Col>
          <Col sm={6} className='text-center'>
            <h6>{DOB}</h6>
            <p className='text-muted'><small>DATE OF BIRTH</small></p>
          </Col>
          <Col sm={6} className='text-center'>
            <h6>{NATION} {GetFlag(NATIONALITY, 20, 15)}</h6>
            <p className='text-muted'><small>NATIONALITY</small></p>
          </Col>
          <Col sm={6} className='text-center'>
              <h6 >{GetPlayerType(PLAYER_TYPE)}</h6>
              <p className='text-muted'><small>PLAYER TYPE</small></p>
          </Col>
          <Col sm={6} className='text-center'>
            <h6 >{GetGender(USER_GENDER)}</h6>
            <p className='text-muted'><small>GENDER</small></p>
          </Col>
          <Col sm={6} className='text-center'>
            <h6 >{UNITS}</h6>
            <p className='text-muted'><small>Preferred Units</small></p>
          </Col>
          <Col sm={6} className='text-center'>
            <h6 >{ROLE.toUpperCase()}</h6>
            <p className='text-muted'><small>Plan</small></p>
          </Col>
        </Row>
      </Card.Body>
    </Card>
  )
}


export default ProfileInfoCard