import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
pt = pd.read_csv("data/mineral/csv/Platinum.csv")
usmine = pd.read_csv("data/mineral/csv/USMined.csv", index_col="Value")
usproc = pd.read_csv("data/mineral/csv/USProcessed.csv", index_col="Value")
