import geopandas as gpd

shapefile = "data/mineral/mineplant-fUS/mineplant-fUS.shp"

gdf = gpd.read_file(shapefile)

print(gdf.head())
