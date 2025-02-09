const GetPlayerType = (type) => {
  switch (type) {
    case 'A':	
      return 'Amatuer'
    case 'C':	
      return 'College'
    case 'P':	
      return 'Professional'
    case 'TP':
      return 'Tour Professional'
    default:
      return 'Unknown'
  }
}

export default GetPlayerType