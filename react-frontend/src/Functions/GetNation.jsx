import { useContext } from "react"

import { NationList } from "../Contexts/NationListContext"

const GetNation = (code) => {
  const { nations, setNations } = useContext(NationList)

  return nations[code]  
}

export default GetNation