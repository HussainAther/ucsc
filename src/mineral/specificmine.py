import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.plotly as py

from IPython.display import IFrame    

plotly.tools.set_credentials_file(username='SHussainAther', api_key='NIq3xfEuGHKtywGFRr0c')

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
