import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
It's like Minecraft except not.
"""

# Read 'em in!
bau = pd.read_csv("data/mineral/csv/Bauxite.csv")
co = pd.read_csv("data/mineral/csv/Cobalt.csv")
co2 = pd.read_csv("data/mineral/csv/Cobalt2.csv")
fsi = pd.read_csv("data/mineral/csv/Ferrosilicon.csv")
ta = pd.read_csv("data/mineral/csv/Tantalum.csv")

alldf = [bau, co, co2, fsi, tau]

outjson = open("output/mineral/specificall.json", "w")
outhtml = open("output/mineral/specificall.html", "w")

for df in alldf:
    outjson.write(pd.DataFrame.to_json(df, orient="table", index=False))
    outjson.write("\n")
    outhtml.write(pd.DataFrame.to_html(df, index=False))
    outhtml.write("\n")
