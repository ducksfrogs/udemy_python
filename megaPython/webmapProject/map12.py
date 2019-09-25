import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain" )
fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[38.26, -99.00],  icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")