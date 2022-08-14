import folium
import pandas
from geopy.geocoders import ArcGIS

nom = ArcGIS()

loc = nom.geocode("San Francisco, USA")
data = pandas.read_csv("./Volcanoes.txt")

n_map = folium.Map(
    location=[loc.latitude, loc.longitude], 
    zoom_start=6, 
    tiles = "Stamen Terrain")

fgm = folium.FeatureGroup(name="Volcanoes")
fgl = folium.FeatureGroup(name="Population")

json_geo_data = (open("world.json", "r", encoding="utf-8-sig")).read()
fgl.add_child(folium.GeoJson(
    data=json_geo_data,
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}
))


lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
names = list(data["NAME"])

def color_maker(elevation):
    if elevation < 1000:
        return "green"
    if elevation < 2000:
        return "orange"
    return "red"

for lt, ln, el, name in zip(lat, lon, elev, names):
    fgm.add_child(folium.CircleMarker(
        location=[lt, ln],
        popup=folium.Popup("%s. Elevation %sm" % (name, str(el)), parse_html=True),
        color="grey",
        fill_color=color_maker(el),
        fill_opacity=0.6,
        radius=6
    ))

n_map.add_child(fgl)
n_map.add_child(fgm)
n_map.add_child(folium.LayerControl())
n_map.save("map.html")
