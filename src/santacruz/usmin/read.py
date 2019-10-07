import shapefile
import sys
import numpy as np
import geopandas as gpd

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Map map map!
from mpl_toolkits.basemap import Basemap 
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon

fp = "data/santacruz/usmin/poly.shp"

gdf = gpd.read_file(fp) 

# Restrict to America.
country = gpd.read_file("data/gz_2010_us_040_00_5m.json")
country = country[country["NAME"].isin(["Alaska","Hawaii"]) == False]

# Plot.
ax = country.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/santacruz/usmin/usmap.png")

# Close.
plt.close()

# Restrict to California.
ca = country[country["NAME"].isin(["California"]) == True]
gdf = gdf.loc[gdf["STATE"] == "CA"]
geom = [Point(x) for x in gdf["geometry"]]
gdf = gpd.GeoDataFrame(
    gdf, geometry=geom)

# Plot.
ax = ca.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/usmin/california.png")
