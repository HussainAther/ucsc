import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Defaunation statistics.
"""

df = pd.DataFrame.from_csv("data/defaunation/gardneretal.csv", encoding="windows-1252")

colors = ["b", "g", "r", "c", "m", "y", "k"]

# plt.figure(figsize=(4,15))
plt.figure()
df["Region"].value_counts().plot.bar(stacked=True)
plt.xlabel("Region")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/defaunation/region.png") 

# plt.figure(figsize=(10,4))
plt.figure()
df["Study design"].value_counts().plot.barh(stacked=True)
plt.ylabel("Study design")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("output/defaunation/studydesign.png")
