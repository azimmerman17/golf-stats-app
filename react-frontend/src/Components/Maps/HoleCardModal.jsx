import { useEffect, useState } from 'react'
import Modal from 'react-bootstrap/Modal'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'
import { MapContainer } from 'react-leaflet/MapContainer'
import { TileLayer } from 'react-leaflet/TileLayer'
import { useMap } from 'react-leaflet/hooks'
import { Marker } from 'react-leaflet/Marker'
import { Popup } from 'react-leaflet/Popup'
import { LayersControl } from 'react-leaflet/LayersControl'

import BuildHolebyHole from '../../Functions/buildHoleByHole'
import { golferIcon_yellow, golferIcon_white, greenIcon_yellow, greenIcon_white } from './MapIcons'
import FindMapCenter from '../../Functions/FindMapCenter'
import HolePolyline from './HolePolyline'
import HolePopup from './HolePopup'

const HoleCardModal = ({ tees, mapData, showModal, setShowModal }) => {
  const course = BuildHolebyHole(tees, tees[0].HOLE_COUNT)
  const [currView, setCurrView] = useState({
    currHole: course[showModal.hole - 1],
    currMap: mapData[showModal.hole - 1],
    loc: FindMapCenter(mapData[showModal.hole - 1])
  })
  // const [center, setCenter] = useState(null)

  useEffect(() =>{
    if (NUMBER != showModal.hole) {
      setCurrView({
        currHole: course[showModal.hole -1], 
        currMap: mapData[showModal.hole - 1],
        loc: FindMapCenter(mapData[showModal.hole - 1])
      })
      // const { currMap } = currView
      // setCenter(FindMapCenter(currMap))
    }

    // if (!center) setCenter(FindMapCenter(currView.currMap))
  }, [showModal])

  const { currHole, currMap, loc } = currView
  const {parMale, siMale, parFemale, siFemale} = currHole
  const { ZOOM, NUMBER } = currMap

  // const changeHole = (newHoleNumber) => {
  //   console.log(newHoleNumber)
  //   setShowModal({...showModal, hole: mapData[newHoleNumber - 1]})
  // }

  // const ChangeView = ({ hole }) => {
  //   const map = useMap()
  //   const { loc, currMap } = currView
  //   const { ZOOM } = currMap
  //   map.setView([loc.lat, loc.lon], ZOOM)

  //   return null
  // }

  const markers = mapData.map((hole, i) => {
    const { TEE_LAT, TEE_LON, CGREEN_LAT, CGREEN_LON } = hole
    return (
      <>
        <Marker position={[TEE_LAT, TEE_LON]} icon={hole.NUMBER === NUMBER ? golferIcon_white : golferIcon_yellow} key={`tee_icon_hole_${hole.NUMBER}`}>
          <HolePopup current={hole.NUMBER === NUMBER} marker='Tee' hole={hole} course={course[i]} />
        </Marker>
        <Marker position={[CGREEN_LAT, CGREEN_LON]} icon={hole.NUMBER === NUMBER ? greenIcon_white : greenIcon_yellow} key={`green_icon_hole_${hole.NUMBER}`}>
          <HolePopup current={hole.NUMBER === NUMBER} marker='Green' hole={hole} course={course[i]} />
        </Marker>
      </>
    )
  })

  const polylines = mapData.map(hole => {
    let pathColor = '#FFFFFF'
    if (hole.NUMBER === NUMBER) pathColor = '#FFFF00'

    return <HolePolyline hole={hole} pathColor={pathColor} key={`polyline_hole_${hole.NUMBER}`} />
  })
  
  if (currView) {
    return (
        <Modal show={showModal.show} fullscreen={true}  onHide={e => setShowModal({...showModal, show: false})}> 
          <Modal.Header closeButton>
            <Modal.Title>Hole #{NUMBER}</Modal.Title>
            {/* <p onClick={e => changeHole(NUMBER + 1)}>NEXT</p> */}
          </Modal.Header>
          <Modal.Body>
            <MapContainer center={[loc.lat, loc.lon]} zoom={ZOOM} scrollWheelZoom={false} id='hole-map'> 
              {/* <ChangeView hole={NUMBER} />  */}
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
                      attribution={`&copy; <a href=https://www.google.com/maps/place/${loc.lat},${loc.lon} target='_black'>View on Google Maps</a>`}
                      subdomains={['mt0','mt1','mt2','mt3']}
                    />
                </LayersControl.BaseLayer>
                <LayersControl.BaseLayer name='Hybrid'>
                  <TileLayer
                      url={`https://{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}`}
                      maxZoom= {20}
                      attribution={`&copy; <a href=https://www.google.com/maps/place/${loc.lat},${loc.lon} target='_black'>View on Google Maps</a>`}
                      subdomains={['mt0','mt1','mt2','mt3']}
                    />
                </LayersControl.BaseLayer>
                <LayersControl.BaseLayer name='Terrain'>
                  <TileLayer
                      url={`https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}`}
                      maxZoom= {20}
                      attribution={`&copy; <a href=https://www.google.com/maps/place/${loc.lat},${loc.lon} target='_black'>View on Google Maps</a>`}
                      subdomains={['mt0','mt1','mt2','mt3']}
                    />
                </LayersControl.BaseLayer>
              </LayersControl>
              {markers}
              {polylines}
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
}

export default HoleCardModal