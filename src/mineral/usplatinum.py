import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
pt = pd.read_csv("data/mineral/csv/Platinum.csv")
usproc = pd.read_csv("data/mineral/csv/USProcessed.csv", index_col="Value")

usproc = usproc.transpose()

pt["Year"] = [int(i) for i in pt["Year"]]
usproc["Year"] = [int(i) for i in usproc.index]

fig = plt.figre()
ax = fig.add_subplot()
plt.plot("Year", "Worldmineproduction", data=pt)
plt.title("World Platinum Production")
plt.ylabel("Thousand Metric Tons")
plt.xlabel("Year")
plt.xticks(range(1990, 2010)) 
plt.savefig("output/mineral/ptworldprod.png")

