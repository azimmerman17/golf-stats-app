import CoordinatesMidpoint from '../Functions/CoordinatesMidpoint';

const FindMapCenter = (hole) => {
  const {  BGREEN_LAT, BGREEN_LON, CGREEN_LAT, CGREEN_LON, DL2_LAT, DL2_LON,  DL_LAT, DL_LON, FGREEN_LAT,FGREEN_LON, TEE_LAT, TEE_LON } = hole

  let center = CoordinatesMidpoint([
    {lat: BGREEN_LAT, lon: BGREEN_LON},
    {lat: CGREEN_LAT, lon: CGREEN_LON},
    {lat: FGREEN_LAT, lon: FGREEN_LON},
    {lat: DL2_LAT, lon: DL2_LON},
    {lat: DL_LAT, lon: DL_LON},
    {lat: TEE_LAT, lon: TEE_LON}
  ])
  
  return center
}

export default FindMapCenter