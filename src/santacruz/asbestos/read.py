import geopandas as gpd

fp = "data/santacruz/asbestos/main.shp"

data = gpd.read_file(fp)
print(data.head())
