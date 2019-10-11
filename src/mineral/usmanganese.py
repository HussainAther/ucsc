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
ismine = pd.read_csv("data/mineral/csv/USMined.csv", index_col="Value")
usproc = pd.read_csv("data/mineral/csv/USProcessed.csv", index_col="Value")
