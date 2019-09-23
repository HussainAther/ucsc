# Import numpy for number manipulation
import numpy as np

# Import pandas for data manipulation
import pandas as pd

# Map plotting tools
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Map map map!
from mpl_toolkits.basemap import Basemap 
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon

"""
Extract information and draw trends from platinum-group elements (PGE)
with nickel and chromium mineralization.
"""

# Read the .txt file as a pandas DataFrame df
df = pd.read_csv("data/nicr/nicrpge.txt", sep="|", encoding = "ISO-8859-1")
