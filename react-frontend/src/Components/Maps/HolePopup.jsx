import Table from 'react-bootstrap/Table'
import { Popup } from 'react-leaflet/Popup'


const HolePopup = ({ current, marker, hole, course }) => {
  const { GREEN_DEPTH, NUMBER } = hole
  const { yards } = course

    let tees = []
    for (let key in yards) {
      tees.push(key)
    }

  const tableRows = tees.map(tee => {
    return (
      <tr key={`hole_${NUMBER}_${tee}`}>
        <td><small>{tee}</small></td>
        <td><small>{yards[tee]}</small></td>
      </tr>
      )
  })
  
  if (marker === 'Green' && GREEN_DEPTH) {
    return (
      <Popup>
        <h6 className='m-0 text-center'>GREEN DEPTH: {GREEN_DEPTH} yds</h6>
        {/* { hole.NUMBER !== NUMBER ? <Button className='' variant='link' onClick={e => setShowModal({...showModal, hole: hole.NUMBER})}>Switch to Hole</Button> : null } */}
      </Popup>
    )
  } else if (marker === 'Tee') {
    return (
      <Popup>
        <h6 className='m-0 text-center'>HOLE #{NUMBER}</h6>
        <Table size='sm'>
          <thead>
            <th><small>Tee</small></th>
            <th><small>Yards</small></th>
          </thead>
          <tbody>
            {tableRows}
          </tbody>
        </Table>
        {/* { current ? <Button className='' variant='link' onClick={e => setShowModal({...showModal, hole: hole.NUMBER})}>Switch to Hole</Button> : null } */}
      </Popup>
    )
  }

  }
  
  export default HolePopup