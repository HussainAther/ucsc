import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# Plot.
plot = sns.lmplot("latitude", "longitude", data=magdf, fit_reg=False, hue="diurnal", legend=False)
plot.savefig("output/santacruz/quadrangle.png")

# K-Nearest neighbors clustering (kNN) with
# greater circle distance as a metric to minimize.
def valpoint(p):
    """
    Validate a point.
    """
    lat, lon = p
    assert -90 <= lat <= 90, "bad latitude"
    assert -180 <= lon <= 180, "bad longitude"
