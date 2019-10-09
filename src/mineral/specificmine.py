import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
bau = pd.read_csv("data/mineral/csv/Bauxite.csv")
cu = pd.read_csv("data/mineral/csv/Copper.csv")
cu2 = pd.read_csv("data/mineral/csv/Copper2.csv")
cu3 = pd.read_csv("data/mineral/csv/Copper3.csv")
cu4 = pd.read_csv("data/mineral/csv/Copper4.csv")
mo = pd.read_csv("data/mineral/csv/Molybdenum.csv")
ta = pd.read_csv("data/mineral/csv/Tantalum.csv")

alldf = [bau, cu, cu2, cu3, cu4, mo, ta]

outjson = open("output/mineral/specificall.json", "w")
outhtml = open("output/mineral/specificall.html", "w")

for df in alldf:
    outjson.write(pd.DataFrame.to_json(df, orient="table", index=False))
    outjson.write("\n")
    outhtml.write(pd.DataFrame.to_html(df, index=False))
    outhtml.write("\n")

usmined = pd.read_csv("data/mineral/csv/USMined.csv")

usminedconsumption = pd.concat([usmined.loc[usmined.Value == "BauxiteConsumption"],
                           usmined.loc[usmined.Value == "CopperConsumption"],
                           usmined.loc[usmined.Value == "MolybdenumConsumption"],
                           usmined.loc[usmined.Value == "TantalumConsumption"]])
usminedconsumption = usminedconsumption.transpose()
usminedconsumption.columns = usminedconsumption.iloc[0]
usminedconsumption = usminedconsumption[1:]

# Plot.
plt.scatter(["2005", "2006", "2007", "2008", "2009"],
             list(usminedconsumption["BauxiteConsumption"].values)) 
plt.scatter(["2005", "2006", "2007", "2008", "2009"],
             list(usminedconsumption["CopperConsumption"].values)) 
plt.scatter(["2005", "2006", "2007", "2008", "2009"],
             list(usminedconsumption["MolybdenumConsumption"].values)) 
plt.scatter(["2005", "2006", "2007", "2008", "2009"],
             list(usminedconsumption["TantalumConsumption"].values)) 
