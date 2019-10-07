import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score

"""
Logistic regression (lr)
"""

# Read in data.
raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# Extract data of interest for the lr.
X = [list(a) for a in zip(magdf["latitude"], magdf["longitude"])] # features we test
lab_enc = preprocessing.LabelEncoder() # label encoder
y = magdf["diurnal"].values
y = lab_enc.fit_transform(y)
feature = ["latitude", "longitude"] # feature names

clf = LogisticRegression(random_state=0, solver="lbfgs",
    multi_class="multinomial").fit(X, y)
