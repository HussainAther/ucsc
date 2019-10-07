import itertools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score

"""
Logistic regression (lr)
"""

# Read in data.
raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# Extract data of interest for the lr.
X = [list(a) for a in zip(magdf["latitude"], magdf["longitude"])] # Features we test
y = list(magdf["diurnal"])
target = ynames
feature = ["latitude", "longitude"] # Feature names
