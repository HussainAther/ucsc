import shapefile
import numpy as np
import geopandas as gpd

import matplotlib
import matplotlib.pyplot as plt

fp = "data/mineral/mineplant-fUS/mineplant-fUS.shp"

# sf = shapefile.Reader(fp)
# shapes  = sf.shapes()
# feature = sf.shapeRecords()[0]
# first = feature.shape.__geo_interface__ 
# print(first)

data = gpd.read_file(fp) 
type(data)
print(data.head())
data.plot()
