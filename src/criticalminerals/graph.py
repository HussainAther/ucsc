import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapefile

"""
Critical mineral graphs
"""

# shape = shapefile.Reader("data/criticalminerals/PP1802_CritMin_pts.shp") 

# # First feature of the shapefile
# feature = shape.shapeRecords()[0]
# first = feature.shape.__geo_interface__  
# print(first) # (GeoJSON format)

gdf = gpd.read_file("data/criticalminerals/PP1802_CritMin_pts.shp")

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
geoplot.polyplot(world, figsize=(8, 4))
ax = world.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")
plt.savefig("output/criticalminerals/worldmap.png")
