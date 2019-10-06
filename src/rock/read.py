import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from shapely import wkt

"""
Rocks.
"""

# Read in shapefile as geopands dataframe.
gdf = gpd.read_file("data/rock/ngdbrock.shp", encoding="utf-8")

# Plot the world map.
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
ax = world.plot(
    color="white", edgecolor="black")
gdf.plot(ax=ax, color="red", markersize=5)
plt.savefig("output/rock/worldmap.png")
plt.close()

# Restrict to America, excluding Hawaii and Alaska.
country = gpd.read_file("data/gz_2010_us_040_00_5m.json")
country = country[country["NAME"].isin(["Alaska","Hawaii"]) == False]

# Plot.
ax = country.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/asbestos/usmap.png")
