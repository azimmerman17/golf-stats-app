import { useState } from 'react'
import Modal from 'react-bootstrap/Modal'
import Row from 'react-bootstrap/esm/Row'
import Col from 'react-bootstrap/esm/Col'
import { MapContainer } from 'react-leaflet/MapContainer'
import { TileLayer } from 'react-leaflet/TileLayer'
import { Marker } from 'react-leaflet/Marker'
import { Popup } from 'react-leaflet/Popup'
import { Polyline } from 'react-leaflet/Polyline'
import { MdGolfCourse } from "react-icons/md";

import { LayersControl } from 'react-leaflet/LayersControl'

import BuildHolebyHole from '../../Functions/buildHoleByHole'
import CoordinatesMidpoint from '../../Functions/CoordinatesMidpoint';
import { golferIcon_yellow, golferIcon_white, greenIcon_yellow, greenIcon_white } from './MapIcons'

const HoleCardModal = ({ tees, map, showModal, setShowModal }) => {
  const course = BuildHolebyHole(tees, tees[0].HOLE_COUNT)
  const hole = course[showModal.hole -1]
  const {parMale, siMale, parFemale, siFemale} = hole
  console.log(hole, map)

  const {  BGREEN_LAT, BGREEN_LON, CGREEN_LAT, CGREEN_LON, DL2_LAT, DL2_LON,  DL_LAT, DL_LON, FGREEN_LAT,FGREEN_LON, GREEN_DEPTH, TEE_LAT, TEE_LON, ZOOM, NUMBER } = map[showModal.hole - 1]

  let center = CoordinatesMidpoint([
    {lat: BGREEN_LAT, lon: BGREEN_LON},
    {lat: CGREEN_LAT, lon: CGREEN_LON},
    {lat: FGREEN_LAT, lon: FGREEN_LON},
    {lat: DL2_LAT, lon: DL2_LON},
    {lat: DL_LAT, lon: DL_LON},
    {lat: TEE_LAT, lon: TEE_LON}
  ])

  const polylineCoods = []
  if (TEE_LAT && TEE_LON) polylineCoods.push([TEE_LAT, TEE_LON])
  if (DL_LAT && DL_LON) polylineCoods.push([DL_LAT, DL_LON])
  if (DL2_LAT && DL2_LON) polylineCoods.push([DL2_LAT, DL2_LON])
  if (CGREEN_LAT && CGREEN_LON) polylineCoods.push([CGREEN_LAT,  CGREEN_LON])
  
  return (
      <Modal show={showModal.show} fullscreen={true}  onHide={e => setShowModal({...showModal, show: false})}> 
        <Modal.Header closeButton>
          <Modal.Title>Hole #{NUMBER}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <MapContainer center={[center.lat, center.lon]} zoom={ZOOM} scrollWheelZoom={false} id='hole-map'> 
          <LayersControl>
            <LayersControl.BaseLayer name='OpenStreetMap'>
              <TileLayer
                url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              />
            </LayersControl.BaseLayer>
            <LayersControl.BaseLayer checked name='Satellite'>
              <TileLayer
                  url={`https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}`}
                  maxZoom= {20}
                  attribution={`&copy; <a href=https://www.google.com/maps/place/${center.lat},${center.lon} target='_black'>View on Google Maps</a>`}
                  subdomains={['mt0','mt1','mt2','mt3']}
                />
            </LayersControl.BaseLayer>
            <LayersControl.BaseLayer name='Hybrid'>
              <TileLayer
                  url={`https://{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}`}
                  maxZoom= {20}
                  attribution={`&copy; <a href=https://www.google.com/maps/place/${center.lat},${center.lon} target='_black'>View on Google Maps</a>`}
                  subdomains={['mt0','mt1','mt2','mt3']}
                />
            </LayersControl.BaseLayer>
            <LayersControl.BaseLayer name='Terrain'>
              <TileLayer
                  url={`https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}`}
                  maxZoom= {20}
                  attribution={`&copy; <a href=https://www.google.com/maps/place/${center.lat},${center.lon} target='_black'>View on Google Maps</a>`}
                  subdomains={['mt0','mt1','mt2','mt3']}
                />
            </LayersControl.BaseLayer>
          </LayersControl>
        <Marker position={[TEE_LAT, TEE_LON]} icon={golferIcon_white}></Marker>
        <Marker position={[CGREEN_LAT, CGREEN_LON]} icon={greenIcon_white}></Marker>
        <Polyline pathOptions={{color: '#ffff00'}} positions={polylineCoods} />
      </MapContainer>
        </Modal.Body>
        <Modal.Footer>
          <Row>
            <Col>
            <h6>{parMale['Default']}</h6>
            <p className='text-muted'><small>MENS PAR</small></p>
            </Col>
            <Col>
            <h6>{siMale}</h6>
            <p className='text-muted'><small>MENS SI</small></p>
            </Col>
            <Col>
              <h6>{parFemale['Default']}</h6>
              <p className='text-muted'><small>LADIES PAR</small></p>
            </Col>
            <Col>
              <h6>{siFemale}</h6>
              <p className='text-muted'><small>LADIES SI</small></p>
            </Col>
          </Row>
        </Modal.Footer>
      </Modal>
  )
}

export default HoleCardModal