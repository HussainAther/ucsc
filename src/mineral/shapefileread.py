import shapefile
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.cm import *
from IPython.display import Image as ImageShow

sf = shapefile.Reader("data/mineral/mineplant-fUS/mineplant-fUS.shp")
shapes  = sf.shapes()

