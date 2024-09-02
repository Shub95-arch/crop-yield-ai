import pyowm
from pyowm.agro10 import AgroManager
from pyowm.utils.geo import Polygon as GeoPolygon
import folium

owm = pyowm.OWM('f4a54522d6932f25c44283cb9839217d')
mgr = owm.agro_manager()

from pyowm.utils.geo import Polygon as GeoPolygon

india_polygon = GeoPolygon([
    [68.1766, 8.0722], [68.1766, 37.0844], [92.5137, 37.0844],
    [92.5137, 35.5041], [95.1667, 35.5041], [95.1667, 28.2179],
    [90.2667, 28.2179], [90.2667, 22.5444], [86.6333, 22.5444],
    [86.6333, 20.5939], [82.6333, 20.5939], [82.6333, 18.2179],
    [78.6333, 18.2179], [78.6333, 15.8444], [74.6333, 15.8444],
    [74.6333, 13.5041], [70.6333, 13.5041], [70.6333, 10.2179],
    [68.1766, 10.2179], [68.1766, 8.0722]
])

polygon = mgr.create_polygon(india_polygon, 'India')

temperature_data = mgr.soil_data(polygon)
crop_data = mgr.get_polygons()

m = folium.Map(location=[20, 77], zoom_start=4)

folium.raster_layers.TileLayer('Temperature', temperature_data).add_to(m)

for crop in crop_data:
    folium.Marker([crop.latitude, crop.longitude], popup=crop.crop_type).add_to(m)

m