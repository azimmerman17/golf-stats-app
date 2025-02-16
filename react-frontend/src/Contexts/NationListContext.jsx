// context for the nations
import { createContext, useEffect, useState } from 'react';

export const NationList = createContext()

const NationListProvider = ({ children }) => {
  const BASE_URL = 'https://flagcdn.com/en/codes.json'
  const [nations, setNations] = useState({loaded: false})

  useEffect(() =>{
    const getNations = async () => {

      let response = await fetch(BASE_URL)
      let nationObj = await response.json()

      setNations({nationObj, loaded: true})
    }

    if (!nations.loaded) getNations()
  },[nations])

  return (
    <NationList.Provider value={{ nations, setNations }}>
        {children}
    </NationList.Provider>
  )
}

export default NationListProvider
