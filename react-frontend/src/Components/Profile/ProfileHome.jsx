import { useContext, useState, useEffect } from 'react';
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import { CurrentUser } from '../../Contexts/CurrentUserContext';

import GetPlayerType from '../../Functions/GetPlayerType';
import GetGender from '../../Functions/GetGender';
import GetFlag from '../../Functions/GetFlag';

const ProfileHome = () => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)

  const { EMAIL, FIRST_NAME, LAST_NAME, NATIONALITY, PLAYER_TYPE, USERNAME, USER_GENDER, NATION } = currentUser

  return (
    <Card className='mx-auto my-1 p-2 border border-5 border-danger rounded-3 shadow-lg '>
      <Card.Body>
        <Card.Title className='text-center fs-2'>{FIRST_NAME} {LAST_NAME}</Card.Title>
        <Card.Subtitle className="mb-2 text-muted text-center fs-4">{USERNAME}</Card.Subtitle>
          <Row>
            <Col sm={6} className='text-center'>
              <h6>{EMAIL}</h6>
              <p className='text-muted'><small>EMAIL</small></p>
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
          </Row>
      </Card.Body>
    </Card>
  )
}

export default ProfileHome