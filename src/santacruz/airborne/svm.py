import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.svm import SVC 

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

