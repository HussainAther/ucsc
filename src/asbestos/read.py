import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from shapely.geometry import Point

"""
Let's get down to business to defeat asbestos.
"""

df = pd.read_csv("data/asbestos/main.csv")

geom = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
gdf = gpd.GeoDataFrame(
    df, geometry=geom)
crs = {"init": "epsg:2263"} #http://www.spatialreference.org/ref/epsg/2263/
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geom)
gdf.to_file(driver="ESRI Shapefile", filename="output/asbestos/data")

# Restrict to America.
country = gpd.read_file("data/asbestos/gz_2010_us_040_00_5m.json")
country = country[country["NAME"].isin(["Alaska","Hawaii"]) == False]

# Plot.
ax = country.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/asbestos/usmap.png")
