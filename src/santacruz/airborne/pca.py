import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition

"""
Principal Component Analysis (PCA pca).
"""

# Read in data.
raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")


# Extract data of interest for pca.
y = [] # The target values of interest with a specific number assocaited with each target
ynames = [] # Names for each target valuea
count = 0 # Used for keeping track of each target
for i in range(len(magdf["geology"])):
    if i in ynames:
        y.append(ynames.index(i))
    else:
        count += 1
        y.append(count)
        ynames.append(count)
X = [list(a) for a in zip(magdf["latitude"], magdf["longitude"])] # Features we test

# Plot.
fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
plt.cla()
pca = decomposition.PCA(n_components=2)
pca.fit(X)
X = pca.transform(X)

for name, label in zip(ynames, range(len(ynames))):
    ax.text3D(X[y == label, 0].mean(),
              X[y == label, 1].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment="center",
              bbox=dict(alpha=.5, edgecolor="w", facecolor="w"))
# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.nipy_spectral,
           edgecolor="k")
ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
plt.savefig("output/santacruz/airborne/pca.png")
