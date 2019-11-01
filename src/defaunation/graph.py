import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Defaunation statistics.
"""

df = pd.DataFrame.from_csv("data/defaunation/gardneretal.csv", encoding="windows-1252")

print(df.columns)
