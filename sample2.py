#!/usr/bin/env python                                                                               
 
from pygeocoder import Geocoder
import folium
 
area_name = '東京スカイツリー' 
 place= Geocoder.geocode(area_name)
 loc = place[0].coordinates
 
map_obj =folium.Map(location=loc,zoom_start=15)
 
folium.Marker(loc,popup=str(area_name),
icon=folium.Icon(color='blue',icon='info-sign')
).add_to(map_obj)
 
 
 
map_obj.save("output_sample.html")