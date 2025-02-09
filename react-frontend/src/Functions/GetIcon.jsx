import Image from 'react-bootstrap/Image'

import reactLogo from '/react.svg'
import viteLogo from '/vite.svg'
import bootstrapLogo from '/bootstrap.svg'
import flaskLogo from '/flask.svg'
import pythonLogo from '/python.svg'
import postgresLogo from '/postgres.svg'
import SQLAlchemyLogo from '/SQLAlchemy.svg'
import golferLogo from '/golfer.svg'

import { BsGraphDown, BsFillBucketFill } from 'react-icons/bs';
import { GoPersonFill } from 'react-icons/go';
import { IoGolfSharp, IoLogInOutline, IoLogOutOutline } from 'react-icons/io5';
import { FaGear, FaTrophy, FaGolfBallTee, FaPlus } from 'react-icons/fa6';
import { VscGraph } from 'react-icons/vsc'

const GetIcon = (iconName) => {
  switch (iconName) {
    case 'Vite Logo':
      return viteLogo
    case 'React Logo':
      return reactLogo
    case 'Bootstrap Logo':
      return bootstrapLogo
    case 'Python Logo':
      return pythonLogo
    case 'Flask Logo':
      return flaskLogo
    case 'PostgreSQL Logo':
      return postgresLogo
    case 'SQLAlchemy Logo':
      return SQLAlchemyLogo
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
    case 'Courses Analysis':
      return <IoGolfSharp />
    case 'Rounds Plus':
      return <><FaPlus /><FaGolfBallTee /></>
    case 'Practice Plus':
      return <><FaPlus /><BsFillBucketFill /></>
    case 'Course Plus':
      return <><FaPlus /><IoGolfSharp /></>
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