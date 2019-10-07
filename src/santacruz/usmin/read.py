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
print(gdf.columns)
print(gdf.head())
sys.exit()
