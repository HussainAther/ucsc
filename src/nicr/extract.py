import pandas as pd

"""
Extract information and draw trends from platinum-group elements (PGE)
with nickel and chromium mineralization.
"""

df = pd.read_csv("data/nicr/nicrpge.txt", sep="|")
print(df.head()) 
