import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapefile

"""
Create the csv from the critical mineral information
to use as input for the periodic table.
"""

# Use geopandas to read in shapefile as DataFrame. 
gdf = gpd.read_file("data/criticalminerals/PP1802_CritMin_pts.shp")
