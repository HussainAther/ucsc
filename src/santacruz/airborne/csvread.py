import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# Plot.
plot = sns.lmplot("latitude", "longitude", data=magdf, fit_reg=False, hue="diurnal", legend=False)
plot.savefig("output/santacruz/quadrangle.png")

# K-Nearest neighbors clustering (kNN) with
# greater circle distance as a metric to minimize.
# Also kd-tree (kd tree kdtree).
def valpoint(p):
    """
    Validate a point.
    """
    lat, lon = p
    assert -90 <= lat <= 90, "bad latitude"
    assert -180 <= lon <= 180, "bad longitude"

def distance_haversine(a, b):
    """
    Calculate the great circle distance between two lists of points 
    on the earth (specified in decimal degrees)
    Haversine
    formula: 
        a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
        c = 2 ⋅ atan2( √a, √(1−a) )
        d = R ⋅ c
    where   φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
            note that angles need to be in radians to pass to trig functions!
    """
    result = []
    for i in range(len(a)):
        lat1, lon1 = a[i]
        lat2, lon2 = b[i]
        for p in [a[i], b[i]]:
            validate_point(p)
        R = 6371 # km - earths's radius
        # convert decimal degrees to radians 
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        # haversine formula 
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.asin(np.sqrt(a)) # 2 * np.atan2(np.sqrt(a), np.sqrt(1-a))
        d = R * c
        result.append(d)
    return result

distances = distance_haversine(magdf["latitude"], magdf["longitude"])
