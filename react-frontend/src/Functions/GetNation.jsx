const GetNation = async (code) => {
  
  let res = await fetch('https://flagcdn.com/en/codes.json')
  let data = await res.json()

  return data[code]
}


export default GetNation