const BuildHolebyHole = (course, hole_count) => {
  let res = []

  //function to find most common par value
  const mostCommon = (arr) => {
    let map = {}
    let maxCount = 0
    let res = null

    for (let x of arr) {
      map[x] = (map[x] || 0) + 1

      if (map[x] > maxCount) {
          maxCount = map[x]
          res = x
      }
    }
    return res
  }

  for (let i = 0; i < hole_count; i++) {
    // intialiaze hole obj
    let holeObj = {
      holeNumber: i + 1,
      yards: {},
      meters: {},
      siMale: null,
      parMale: {},
      siFemale: null,
      parFemale: {}
    }

    // find default par value (most common)
    let maleDefault = []
    let femaleDefault = []

    course.forEach(tee => {
      const { HOLES, NAME } = tee
      const hole = HOLES[i]
      const { METERS, PAR_FEMALE, PAR_MALE, SI_FEMALE, SI_MALE, YARDS } = hole

      // add data to hole obj
      holeObj.yards[NAME] = YARDS
      holeObj.meters[NAME] = METERS
      if (holeObj.siMale === null ) holeObj.siMale = SI_MALE
      if (holeObj.siFemale === null ) holeObj.siFemale = SI_FEMALE
      holeObj.parMale[NAME] = PAR_MALE
      holeObj.parFemale[NAME] = PAR_FEMALE

      // add to defaults
      if (PAR_MALE !== null ) maleDefault.push(PAR_MALE)
      if (PAR_FEMALE !== null )  femaleDefault.push(PAR_FEMALE)
    })

    // set default par - most common
    holeObj.parMale['Default'] = mostCommon(maleDefault)
    holeObj.parFemale['Default'] = mostCommon(femaleDefault)
    
    // console.log(holeObj)
    res.push(holeObj)
  }

  return res
}

export default BuildHolebyHole