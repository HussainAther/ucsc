import geopandas as gpd

fp = "data/santacruz/asbestos/asbestos.shp"

data = gpd.read_file(fp)
print(data.head())
