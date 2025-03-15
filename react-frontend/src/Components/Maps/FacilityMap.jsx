import { MapContainer } from 'react-leaflet/MapContainer'
import { TileLayer } from 'react-leaflet/TileLayer'
import { Marker } from 'react-leaflet/Marker'
import { Popup } from 'react-leaflet/Popup'
import { LayersControl } from 'react-leaflet/LayersControl'
import { golferIcon } from './MapIcons'


const FacilityMap = ({ GEO_LAT, GEO_LON, NAME }) => {

  return (
    <MapContainer center={[GEO_LAT, GEO_LON]} zoom={15} scrollWheelZoom={false} id='contact-map'> 
      <LayersControl>
        <LayersControl.BaseLayer checked name='OpenStreetMap'>
          <TileLayer
            url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
        </LayersControl.BaseLayer>
        <LayersControl.BaseLayer name='Satellite'>
          <TileLayer
              url={`https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}`}
              maxZoom= {20}
              attribution={`&copy; <a href=https://www.google.com/maps/place/${GEO_LAT},${GEO_LON} target='_black'>View on Google Maps</a>`}
              subdomains={['mt0','mt1','mt2','mt3']}
            />
        </LayersControl.BaseLayer>
        <LayersControl.BaseLayer name='Hybrid'>
          <TileLayer
              url={`https://{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}`}
              maxZoom= {20}
              attribution={`&copy; <a href=https://www.google.com/maps/place/${GEO_LAT},${GEO_LON} target='_black'>View on Google Maps</a>`}
              subdomains={['mt0','mt1','mt2','mt3']}
            />
        </LayersControl.BaseLayer>
        <LayersControl.BaseLayer name='Terrain'>
          <TileLayer
              url={`https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}`}
              maxZoom= {20}
              attribution={`&copy; <a href=https://www.google.com/maps/place/${GEO_LAT},${GEO_LON} target='_black'>View on Google Maps</a>`}
              subdomains={['mt0','mt1','mt2','mt3']}
            />
        </LayersControl.BaseLayer>
      </LayersControl>
     <Marker position={[GEO_LAT, GEO_LON]} icon={golferIcon}>
        <Popup>
          {NAME}
        </Popup>
      </Marker>
    </MapContainer>
  )
}

export default FacilityMap