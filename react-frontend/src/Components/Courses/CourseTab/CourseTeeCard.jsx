import Card from 'react-bootstrap//Card'
import CourseTeeDetails from './CourseTeeDetails'

const CourseTeeCard = ({ tees, selectedTee, setSelectedTee }) => {

  const courseTees = tees.map(tee => {
    console.log(tee)
    const { TEE_ID } = tee
    return <CourseTeeDetails tee={tee} key={TEE_ID} />
  })
  
  return (
    <Card  className='border-danger border-3 rounded p-2 mb-3'>
      <Card.Body className='text-center'>
        <Card.Title>Tees and Ratings</Card.Title>
        <Card.Text>
          {courseTees}
        </Card.Text>
      </Card.Body>
    </Card>
  )
}

export default CourseTeeCard