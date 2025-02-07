import { BsGraphDown } from "react-icons/bs";
import { GoPersonFill } from "react-icons/go";
import { IoGolfSharp, IoLogInOutline, IoLogOutOutline } from "react-icons/io5";
import { FaGear, FaTrophy, FaGolfBallTee } from "react-icons/fa6";
import { VscGraph } from "react-icons/vsc"


const GetIcon = (iconName) => {
  switch (iconName) {
    case 'Rounds':
      return <FaGolfBallTee /> 
    case 'Stats':
      return <VscGraph />
    case 'Handicap':
      return <BsGraphDown />
    case 'Records':
      return <FaTrophy />
    case 'Courses':
      return <IoGolfSharp />
    case 'Profile':
      return <GoPersonFill />
    case 'Settings':
      return <FaGear />
    case 'Logout':
      return <IoLogOutOutline />
    case 'Login':
      return <IoLogInOutline />
    default:
      return null
  }
} 

export default GetIcon