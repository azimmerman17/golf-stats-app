const CoordinatesMidpoint = (coords) => {
  const getMiddle = (prop, markers) => {
    let values = markers.map(m => m[prop]).filter(v => v !== null)
    let min = Math.min(...values)
    let max = Math.max(...values)

    if (prop === 'lon' && (max - min > 180)) {
      values = values.map(val => val < max - 180 ? val + 360 : val)
      min = Math.min(...values)
      max = Math.max(...values)
    }
    let result = (min + max) / 2
    if (prop === 'lon' && result > 180) {
      result -= 360
    }
    return result
  }
  
  return {
    lat: getMiddle('lat', coords),
    lon: getMiddle('lon', coords)
  }
}

export default CoordinatesMidpoint