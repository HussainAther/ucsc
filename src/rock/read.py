import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from shapely import wkt

"""
Rocks.
"""

# Read in shapefile as geopands dataframe.
gdf = gpd.read_file("data/rock/ngdbrock.shp", encoding="utf-8")

# Plot.
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
ax = world.plot(
    color="white", edgecolor="black")
gdf.plot(ax=ax, color="red", markersize=5)
plt.savefig("output/rock/map.png")
plt.close()
