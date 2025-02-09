const GetGender = (code) => {
  switch (code) {
    case 'M':	
      return 'Male'
    case 'F':	
      return 'Female'
    case 'N':
      return 'Non-Binary/Other'
    case 'P':
      return 'Prefer Not To Say'	
    default:
      return 'Unknown'
  }
}

export default GetGender