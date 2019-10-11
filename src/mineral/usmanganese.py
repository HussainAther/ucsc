import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
mn = pd.read_csv("data/mineral/csv/Manganese.csv")
fmn = pd.read_csv("data/mineral/csv/Ferromanganese.csv")
smn = pd.read_csv("data/mineral/csv/Silicomanganese.csv")
usmine = pd.read_csv("data/mineral/csv/USMined.csv", index_col="Value")
usproc = pd.read_csv("data/mineral/csv/USProcessed.csv", index_col="Value")

usmine = usmine.transpose()
usproc = usproc.transpose()

mn["Year"] = [int(i) for i in mn["Year"]]
fmn["Year"] = [int(i) for i in fmn["Year"]]
smn["Year"] = [int(i) for i in smn["Year"]]
usmine["Year"] = [int(i) for i in usmine.index]
usproc["Year"] = [int(i) for i in usproc.index]

fig = plt.figure()
ax = fig.add_subplot()
plt.plot("Year", "Worldmineproduction", data=mn, color="#8A2BE2", label="Manganese")
plt.plot("Year", "Worldmineproduction", data=fmn, color="#FF00FF", label="Ferromanganese")
plt.plot("Year", "Worldmineproduction", data=smn, color="#4B0082", label="Silicomanganese")
plt.title("World Production of Types of Manganese")
plt.legend(loc=0)
plt.xlabel("Year")
plt.ylabel("Thousand metric tons")
plt.yscale("log")
plt.xticks(range(1990, 2011, 4))
plt.savefig("output/mineral/mnworldprod.png")

fig = plt.figure()
ax = fig.add_subplot()
plt.plot("Year", "ManganeseConsumption", data=usmine, color="b", label="Consumption")
plt.title("U.S. Manganese Consumption")
plt.xlabel("Year")
plt.ylabel("Thousand metric tons")
plt.xticks(range(2005, 2010))
plt.savefig("output/mineral/mnuscon.png")

fig = plt.figure()
ax = fig.add_subplot()
