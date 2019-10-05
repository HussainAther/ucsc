import shapefile
import numpy as np
import geopandas s gpd

import matplotlib
import matplotlib.pyplot as plt

fp = "data/mineral/mineplant-fUS/mineplant-fUS.shp")

# sf = shapefile.Reader("data/mineral/mineplant-fUS/mineplant-fUS.shp")
# shapes  = sf.shapes()
# feature = sf.shapeRecords()[0]
# first = feature.shape.__geo_interface__ 
# print(first)

data = gpd.read_file(fp) 
