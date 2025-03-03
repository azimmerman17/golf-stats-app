import Image from 'react-bootstrap/Image'

const GetFlag = (nation, width, height) => {
  const flag_url = 'https://flagcdn.com'

  return (
    <Image 
      src={`${flag_url}/${width}x${height}/${nation.toLowerCase()}.png`}
      srcSet={`${flag_url}/${width*2}x${height*2}/${nation.toLowerCase()}.png 2x,
        ${flag_url}/${width*3}x${height*3}/${nation.toLowerCase()}.png 3x`}
      width={width}
      height={height}
      alt={nation}
    />
  )

}

export default GetFlag