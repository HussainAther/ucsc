import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
fe = pd.read_csv("data/mineral/csv/Iron.csv")
cu = pd.read_csv("data/mineral/csv/Copper.csv")
cu2 = pd.read_csv("data/mineral/csv/Copper2.csv")
cu3 = pd.read_csv("data/mineral/csv/Copper3.csv")
cu4 = pd.read_csv("data/mineral/csv/Copper4.csv")
mo = pd.read_csv("data/mineral/csv/Molybdenum.csv")
ta = pd.read_csv("data/mineral/csv/Tantalum.csv")

alldf = [fe, cu, cu2, cu3, cu4, mo, ta]

outjson = open("output/mineral/specificall.json", "w")
outhtml = open("output/mineral/specificall.html", "w")

for df in alldf:
    outjson.write(pd.DataFrame.to_json(df, orient="table", index=False))
    outjson.write("\n")
    outhtml.write(pd.DataFrame.to_html(df, index=False))
    outhtml.write("\n")

fig = plt.figure()
ax = fig.add_subplot()
range1 = [float(i) for i in cu["Worldmineproduction"].str.replace(",", "").values]
range2 = [float(i) for i in cu3["Worldrefinedsecondaryproduction"].str.replace(",", "").values]
range1 = [int(i) for i in range1]
range2 = [int(i) for i in range2]
miny = min(range1) 
maxy = max(range2)
plt.yticks(np.arange(1000, 10000, 1000))
plt.plot("Year", "Worldmineproduction", data=cu, color="#FAFAD2", label="Mined Copper")
plt.plot("Year", "Worldrefinedproduction", data=cu2, color="#FFD700", label="Refined Copper")
plt.plot("Year", "Worldrefinedsecondaryproduction", data=cu3, color="#DAA520", label="Secondary Copper")
plt.plot("Year", "Worldrefinedelectrowonproduction", data=cu4, color="#FF8C00", label="Refined Electrowon Copper")
plt.savefig("output/mineral/copperprod.png")
plt.close()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_yscale("log")
plt.plot("Year", "Worldmineproduction", data=fe, color="b", label="Iron")
plt.plot("Year", "Worldmineproduction", data=cu, color="y", label="Mined Copper")
plt.plot("Year", "Worldmineproduction", data=mo, color="g", label="Molybdenum")
plt.plot("Year", "Worldmineproduction", data=mo, color="r", label="Tantalum")
plt.savefig("output/mineral/specificprod.png")
plt.close()
