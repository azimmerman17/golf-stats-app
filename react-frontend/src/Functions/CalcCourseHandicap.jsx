// FORMULA - Course Handicap = Handicap Index × (Slope Rating ÷ 113) + (Course Rating – Par)

const CalcCourseHandicap = (handicap, rating) => {
  const { COURSE_RATING, HOLE_COUNT, PAR, SLOPE } = rating

  handicap = (handicap / (18 / HOLE_COUNT)).toFixed(1)

  return Math.round((handicap * (SLOPE / 113)) + (COURSE_RATING - PAR))
}

export default CalcCourseHandicap