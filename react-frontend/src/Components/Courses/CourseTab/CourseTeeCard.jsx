import Card from 'react-bootstrap//Card'

import CourseTeeDetails from './CourseTeeDetails'

const CourseTeeCard = ({ tees, selectedTee, setSelectedTee }) => {

  const courseTees = tees.map(tee => {
    const { TEE_ID } = tee
    
    return <CourseTeeDetails tee={tee} key={TEE_ID} selectedTee={selectedTee} setSelectedTee={setSelectedTee} />
  })

  return (
    <Card  className='border-danger border-3 rounded p-2 mb-3'>
      <Card.Body className='text-center'>
        <Card.Title>Tees and Ratings</Card.Title>
        <Card.Text>
          {courseTees}
          <p className='text-muted m-0'><small>Men's Par and Stroke Index are displayed above the hole length </small></p>
          <p className='text-muted m-0'><small>Ladies's Par and Stroke Index are  displayed below the hole length </small></p>
        </Card.Text>
      </Card.Body>
    </Card>
  )
}

export default CourseTeeCard