import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";

import CalcCourseHandicap from "../../../Functions/CalcCourseHandicap";
import CalcScoreDifferential from "../../../Functions/CalcScoreDifferential";

const CourseHandicapRating = ({ rating, setSelections, selections }) => {
  const { handicap, score } = selections
  if (rating.length < 1) return <h6>No valid ratings found for the selections</h6>

  const { BOGEY_RATING, COURSE_RATING, PAR, SLOPE, HOLE_COUNT } = rating[0]

  return (
    <>
      <Row>
        <Col xs={12}  sm={6} md={3} className='text-center'>
          <h6>{PAR}</h6>
          <p className='text-muted'><small>PAR</small></p>
        </Col>
        <Col xs={12}  sm={6} md={3} className='text-center'>
          <h6>{COURSE_RATING}</h6> 
          <p className='text-muted'><small>COURSE RATING</small></p>
        </Col>
        <Col xs={12}  sm={6} md={3} className='text-center'>
          <h6>{SLOPE}</h6>
          <p className='text-muted'><small>SLOPE</small></p>
        </Col>
        { BOGEY_RATING ? (
          <Col xs={12}  sm={6} md={3} className='text-center'>
            <h6>{BOGEY_RATING}</h6>
            <p className='text-muted'><small>BOGEY RATING</small></p>
          </Col>) : null
        }  
      </Row>
      <Row>
        <Col xs={12} sm={6} md={6} className='text-center'>
          <h6>{CalcCourseHandicap(handicap, rating[0])}</h6>
          <p className='text-muted'><small>COURSE HANDICAP</small></p>
        </Col>
        <Col xs={12} sm={6} md={6} className='text-center'>
          <h6>{CalcCourseHandicap(handicap, rating[0]) + rating[0].PAR}</h6>
          <p className='text-muted'><small>EXP SCORE</small></p>
        </Col>
      </Row>
      <Row>
        <Col xs={12} sm={6} md={6} className='text-center'>
          <h6><Form onChange={e => setSelections({...selections, score: e.target.value})}> 
                <Form.Group controlId="user-handicap">
                  <Form.Control type="number" placeholder={score} />
                  <Form.Label className='text-muted'><small>Hdcp Index</small></Form.Label>
                </Form.Group>
              </Form></h6>
          <p className='text-muted'><small>SCORE</small></p>
        </Col>
        <Col xs={12} sm={6} md={6} className='text-center'>
          <h6>{CalcScoreDifferential(handicap, rating[0], score)}</h6>
          <p className='text-muted'><small>DIFFERENTIAL</small></p>
        </Col>
        {HOLE_COUNT < 18 ?  <p className='text-muted'><small>Differential is estimated for {HOLE_COUNT} hole scoles. Offical GHIN differential could be calculated differently.</small></p> : null}
      </Row>
    </>
  )
}

export default CourseHandicapRating