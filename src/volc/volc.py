import pandas as pd
import json
import os

# Reading the json as a dict
with open("data/volc/tertvolc.json") as json_data:
    data = json.load(json_data, encoding="utf-8")
