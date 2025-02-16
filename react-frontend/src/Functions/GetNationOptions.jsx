const GetNationOptions = (obj, states) => {
  if (!obj) return []
  let options = []

  for (const [key, value] of Object.entries(obj)) {
    if (states === 'ALL') options.push(`${value} - ${key}`)
    else if (states && key.substring(0,3) == 'us-') options.push(`${value} - ${key}`)
    else if (key.substring(0,3) != 'us-') options.push(`${value} - ${key}`)
  }

  return options
}

export default GetNationOptions