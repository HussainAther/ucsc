import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd

"""
Extract information and draw trends from platinum-group elements (PGE)
with nickel and chromium mineralization.
"""

# Read the .txt file as a pandas DataFrame df
df = pd.read_csv("data/nicr/nicrpge.txt", sep="|")

# List of states + Puerto Rico
statelist = [ 
"Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Puerto Rico",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"]

# Initialize empty dictionary to keep track of the 
# frequencies for each state.
statefreq = {}

# Extract the number of states to use as the frequency.
for state in statelist:
    statefreq[state] = len(df.loc[df["State"] == state])

# Lambert Conformal map of lower 48 states.
m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
        projection="lcc", lat_1=33, lat_2=45, lon_0=-95)
# Draw state boundaries.
shp_info = m.readshapefile("data/map/st99_d00", "states", drawbounds=True)

# Choose a color for each state based on number of jobs.
colors={}

# Use hot colormap set.
cmap = plt.cm.copper

# Hawaii has 8 main islands but several tiny atolls that extend for many miles.
# This is the area cutoff between the 8 main islands and the tiny atolls.
ATOLL_CUTOFF = 0.005

# Cycle through state names, color each one.
ax = plt.gca()

# List of statenames.
statenames = []

# Keep track of max and min.
maxx = 0
minn = 0

# For each state, find a color for it.
for shapedict in m.states_info:
    statename = shapedict["NAME"]
    freq = statedict[statename]
    if freq > maxx:
        maxx = freq
    if freq < minn:
        minn = freq
    # Calling colormap with value between 0 and 1 returns
    # rgba value.  Invert color range (hot colors are high
    # population), take sqrt root to spread out colors more.
    colors[statename] = cmap(freq)[:3]
    statenames.append(statename)

# For each state, map and color it.
for nshape, seg in enumerate(m.states):
    # skip DC and Puerto Rico.
    if statenames[nshape] != "Puerto Rico":
    # Offset Alaska and Hawaii to the lower-left corner.
        if statenames[nshape] == "Alaska":  # Scale Alaska appropriately.
            segx = [i[0] for i in seg]
            segy = [i[1] for i in seg]
            lamx = lambda x: .35*float(x) + 1100000
            lamy = lambda y: .35*float(y) - 1300000
            lamxy = lambda x, y: lamx, lamy
            segx = list(map(lamx, segx))
            segy = list(map(lamy, segy))
            seg = np.column_stack((segx, segy))
        elif statenames[nshape] == "Hawaii": # Scale Hawaii appropriately.
            segx = [i[0] for i in seg]
            segy = [i[1] for i in seg]
            lamx = lambda x: float(x) + 5200000
            lamy = lambda y: float(y) - 1400000
            segx = list(map(lamx, segx))
            segy = list(map(lamy, segy))
            seg = np.column_stack((segx, segy))
        color = rgb2hex(colors[statenames[nshape]])
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)
