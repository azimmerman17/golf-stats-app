// Score Differential = (113 / Slope Rating) x (Adjusted Gross Score - Course Rating - PCC adjustment)

const CalcScoreDifferential = (handicap, rating, score ) => {
  const { SLOPE, COURSE_RATING, HOLE_COUNT } = rating

  // < 18 hole expected score Handicap Index * 1.5 per 9 holes
  let adj = 0
  if (HOLE_COUNT < 18) adj = handicap * 1.75 * (HOLE_COUNT / 18)

  return (((113 / SLOPE) * (score - COURSE_RATING)) + adj).toFixed(1)
}

export default CalcScoreDifferential