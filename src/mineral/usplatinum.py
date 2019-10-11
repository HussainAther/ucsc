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
