import arc
import os

mxd = file("data/offshoremonterey/OffshoreMontereyGIS.mxd", "a")  
mxd.close()  
mxddoc = arcpy.mapping.MapDocument(mxd)  
