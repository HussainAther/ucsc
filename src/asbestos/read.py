import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from shapely.geometry import Point

"""
Let's get down to business to defeat asbestos.
"""

df = pd.read_csv("data/asbestos/main.csv")

fig, ax = plt.subplots(figsize=(100, 100))
geometry = [Point(xy) for xy in zip(df["latitude"], df["longitude"])]
crs = {"init": "epsg:2263"} #http://www.spatialreference.org/ref/epsg/2263/
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
gdf.to_file(driver="ESRI Shapefile", filename="output/asbestos/data")
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# We restrict to North America.
ax = world[world.continent == "North America"].plot(
    color="white", edgecolor='black')
