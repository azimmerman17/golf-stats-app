import { Polyline } from 'react-leaflet/Polyline'

const HolePolyline = ({ hole, pathColor }) => {
    const { CGREEN_LAT, CGREEN_LON, DL2_LAT, DL2_LON,  DL_LAT, DL_LON, TEE_LAT, TEE_LON } = hole

    const polylineCoods = []
    if (TEE_LAT && TEE_LON) polylineCoods.push([TEE_LAT, TEE_LON])
    if (DL_LAT && DL_LON) polylineCoods.push([DL_LAT, DL_LON])
    if (DL2_LAT && DL2_LON) polylineCoods.push([DL2_LAT, DL2_LON])
    if (CGREEN_LAT && CGREEN_LON) polylineCoods.push([CGREEN_LAT,  CGREEN_LON])

   return  <Polyline pathOptions={{color: pathColor}} positions={polylineCoods} />
}

export default HolePolyline