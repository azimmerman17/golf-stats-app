import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import Breadcrumbs from './Breadcrumbs'
import modules from '../assets/builtWith'
import GetIcon from '../Functions/getIcon'

const About = () => {
  // message
  const message = `This application will allow golfers to record and track statistics and playing handicaps.  Over time we will continue to evolve to provide new features and more advanced statistics to allow golfers to play and practice better.`
  const disclaimer = `Note: The handicap given on the application is not official and it is strongly recommended to consult your local course or handicap organization to track an official handicap.`

  const breadcrumbList = [
    {name: 'Home', change: '', active: true},
    {name: 'About', change: 'about', active: false}
  ]


  const displayModules = (s) => {
    return(
      modules.map(mod => {
        const {url, alt, server, module } = mod
        if (s === server) {
          return (
            <Col className='text-center my-2' key={`mod-${alt}`}>
              <a href={url} target='_blank'>
                <Image src={GetIcon(alt)} className={`logo ${module}`} alt={alt} />
              </a>
            </Col>
          )
        }
      })
    )
  }

  return (
    <div>
      <Breadcrumbs list={breadcrumbList}></Breadcrumbs>
      <h2 className='text-center my-2'>About the GOLF STATS APP</h2>
      <p className='pt-2'>{message}</p>
      <br/>
      <p>{disclaimer}</p>
      <Container>
        <h3 className='text-center my-2'>Built With</h3>
        <h5 className='text-center my-2'>Frontend Modules</h5>
        <Row>
          {displayModules('frontend')}
        </Row>
        <h5 className='text-center my-2'>Backend Modules</h5>
        <Row>
          {displayModules('backend')}  
        </Row>
      </Container>
    </div>

  )
  
}

export default About