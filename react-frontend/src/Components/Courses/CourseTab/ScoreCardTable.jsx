import Table from 'react-bootstrap/Table';

const ScoreCardTable = ({ holes, units }) => {

  const tableData = (side, title, key) => {
    let sideHoles = []
    let total = 0
    if (side ===  'Front') sideHoles = holes.filter(hole => hole.NUMBER <= 9)
    else sideHoles = holes.filter(hole => hole.NUMBER > 9)
    
    if (title === 'Number') return sideHoles.map(hole => {return <th><small>{hole[key]}</small></th>})
    if (title !== 'Mens SI' && title !==  'Ladies SI' && title !== 'SI') sideHoles.forEach(hole => {total += hole[key]})

      return (
      <tr>
        <td><small>{title}</small></td>
        {sideHoles.map(hole => {return <td><small>{hole[key]}</small></td>})}
        <td className='fw-bold'><small>{total > 0 ? total : null}</small></td>
      </tr>
    )
  }
    
  return (
    <Table  hover bordered size='sm' responsive>
      <thead>
        <th></th>
        {tableData('Front', 'Number', 'NUMBER')}
        <th><small>OUT</small></th>
      </thead>
      <tbody>
        {holes[0].PAR_MALE ? tableData('Front', 'Par', 'PAR_MALE') : null}
        {holes[0].SI_MALE ?tableData('Front', 'SI', 'SI_MALE') : null}
        {tableData('Front', `${units === 'M' ? 'Meters' : 'Yards'}`, `${units === 'M' ? 'METERS' : 'YARDS'}`)}
        {holes[0].PAR_FEMALE ? tableData('Front', 'Par', 'PAR_FEMALE') : null}
        {holes[0].SI_FEMALE ?tableData('Front', 'SI', 'SI_FEMALE') : null}
      </tbody>
      <thead>
        <th></th>
        {tableData('Back', 'Number', 'NUMBER')}
        <th><small>IN</small></th>
      </thead>
      <tbody>
        {holes[0].PAR_MALE ? tableData('Back', 'Par', 'PAR_MALE') : null}
        {holes[0].SI_MALE ?tableData('Back', 'SI', 'SI_MALE') : null}
        {tableData('Back', `${units === 'M' ? 'Meters' : 'Yards'}`, `${units === 'M' ? 'METERS' : 'YARDS'}`)}
        {holes[0].PAR_FEMALE ? tableData('Back', 'Par', 'PAR_FEMALE') : null}
        {holes[0].SI_FEMALE ?tableData('Back', 'Handicap', 'SI_FEMALE') : null}
      </tbody>
      </Table>
  )
}

export default ScoreCardTable