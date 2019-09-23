import arcpy
import os 

arcpy.env.overwriteOutput = True 

arcpy.env.workspace = ws = ""
out = "output" 

for cov in arcpy.ListFiles("data/arc/*.e00"): 
    arcpy.ImportFromE00_conversion(cov, ws, cov.split('.')[0]) 
