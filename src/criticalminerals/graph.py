import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapefile

"""
Critical mineral graphs
"""

shape = shapefile.Reader("data/criticalminerals/PP1802_CritMin_pts.shp") 

#first feature of the shapefile
feature = shape.shapeRecords()[0]
first = feature.shape.__geo_interface__  
print(first) # (GeoJSON format)
