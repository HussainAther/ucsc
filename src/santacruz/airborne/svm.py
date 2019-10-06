import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.svm import SVC 

"""
Support vector machine (SVM svm).
"""

# Read in data.
raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# Extract dat of interest.
X = magdf["latitude"]
y = magdf["longitude"]
target = magdf["diurnal"]

# And the rest of it.
clf = SVC(kernel="rbf")

