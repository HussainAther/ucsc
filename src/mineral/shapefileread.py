import shapefile
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

sf = shapefile.Reader("data/mineral/mineplant-fUS/mineplant-fUS.shp")
shapes  = sf.shapes()
feature = sf.shapeRecords()[0]
first = feature.shape.__geo_interface__ 
print(first) 
