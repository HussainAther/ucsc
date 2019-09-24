import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
It's like Minecraft except not.
"""

# Read 'em in!
al = pd.read_csv("data/mineral/csv/Aluminum.csv")
al2 = pd.read_csv("data/mineral/csv/Aluminum2.csv")
sb = pd.read_csv("data/mineral/csv/Antimony.csv")
sb2 = pd.read_csv("data/mineral/csv/Antimony2.csv")
bar = pd.read_csv("data/mineral/csv/Barite.csv")
bau = pd.read_csv("data/mineral/csv/Bauxite.csv")
be = pd.read_csv("data/mineral/csv/Beryllium.csv")
bi = pd.read_csv("data/mineral/csv/Bismuth.csv")
b = pd.read_csv("data/mineral/csv/Boron.csv")
br = pd.read_csv("data/mineral/csv/Bromine.csv")
cd = pd.read_csv("data/mineral/csv/Cadmium.csv")
cr = pd.read_csv("data/mineral/csv/Chromiuim.csv")
cr2 = pd.read_csv("data/mineral/csv/Chromium2.csv")
co = pd.read_csv("data/mineral/csv/Cobalt.csv")
co2 = pd.read_csv("data/mineral/csv/Cobalt2.csv")
cu = pd.read_csv("data/mineral/csv/Copper.csv")
cu2 = pd.read_csv("data/mineral/csv/Copper2.csv")
cu3 = pd.read_csv("data/mineral/csv/Copper3.csv")
cu4 = pd.read_csv("data/mineral/csv/Copper4.csv")
fel = pd.read_csv("data/mineral/csv/Feldspar.csv")
fmo = pd.read_csv("data/mineral/csv/Ferromolybdenum.csv")
fni = pd.read_csv("data/mineral/csv/Ferronickel.csv")
fno = pd.read_csv("data/mineral/csv/Ferroniobium.csv")
fsi = pd.read_csv("data/mineral/csv/Ferrosilicon.csv")
fv = pd.read_csv("data/mineral/csv/Ferrovanadium.csv")
flu = pd.read_csv("data/mineral/csv/Fluorspar.csv")
ga = pd.read_csv("data/mineral/csv/Gallium.csv")
ge = pd.read_csv("data/mineral/csv/Germanium.csv")
globalmined = pd.read_csv("data/mineral/csv/GlobalMined.csv")
globalproc = pd.read_csv("data/mineral/csv/GlobalProcessed.csv")
au = pd.read_csv("data/mineral/csv/Gold.csv")
gra = pd.read_csv("data/mineral/csv/Graphite.csv")
importmined = pd.read_csv("data/mineral/csv/ImportMined.csv")
importprod = pd.read_csv("data/mineral/csv/ImportProduction.csv")
ind = pd.read_csv("data/mineral/csv/Indium.csv")
i = pd.read_csv("data/mineral/csv/Iodine.csv")
fe = pd.read_csv("data/mineral/csv/Iron.csv")
pb = pd.read_csv("data/mineral/csv/Lead.csv")
pb2 = pd.read_csv("data/mineral/csv/Lead2.csv")
pb3 = pd.read_csv("data/mineral/csv/Lead3.csv")
li = pd.read_csv("data/mineral/csv/Lithium.csv")
mgc = pd.read_csv("data/mineral/csv/Magnesiumcompounds.csv")
mgm = pd.read_csv("data/mineral/csv/Magnesiummetal.csv")
mn = pd.read_csv("data/mineral/csv/Manganese.csv")
mn2 = pd.read_csv("data/mineral/csv/Manganese2.csv")
mn3 = pd.read_csv("data/mineral/csv/Manganese3.csv")
hg = pd.read_csv("data/mineral/csv/Mercury.csv")
mica = pd.read_csv("data/mineral/csv/Mica.csv")
mo = pd.read_csv("data/mineral/csv/Molybdenum.csv")
mon = pd.read_csv("data/mineral/csv/Monazite.csv")
ni = pd.read_csv("data/mineral/csv/Nickel.csv")
ni2 = pd.read_csv("data/mineral/csv/Nickel2.csv")
ni3 = pd.read_csv("data/mineral/csv/NickelMisc.csv")
nio = pd.read_csv("data/mineral/csv/NickelOxide.csv")
nim = pd.read_csv("data/mineral/csv/Nickelmetal.csv")
nb = pd.read_csv("data/mineral/csv/Niobium.csv")
pgm = pd.read_csv("data/mineral/csv/PGM.csv")
pdm = pd.read_csv("data/mineral/csv/Palladium.csv")
po = pd.read_csv("data/mineral/csv/Phosphate.csv")
pl = pd.read_csv("data/mineral/csv/Platinum.csv")
pot = pd.read_csv("data/mineral/csv/Potash.csv")
prodmined = pd.read_csv("data/mineral/csv/ProductionMined.csv")
prodproc = pd.read_csv("data/mineral/csv/ProductionProcessed.csv")
ree = pd.read_csv("data/mineral/csv/REE.csv")
rem = pd.read_csv("data/mineral/csv/Rhenium.csv")
se = pd.read_csv("data/mineral/csv/Selenium.csv")
si = pd.read_csv("data/mineral/csv/Silicon.csv")
ag = pd.read_csv("data/mineral/csv/Silver.csv")
smeltsn = pd.read_csv("data/mineral/csv/SmelteredTin.csv")
smeltzn = pd.read_csv("data/mineral/csv/SmelteredZinc.csv")
steel = pd.read_csv("data/mineral/csv/Steel.csv")
sr = pd.read_csv("data/mineral/csv/Strontium.csv")
s = pd.read_csv("data/mineral/csv/Sulfur.csv")
ta = pd.read_csv("data/mineral/csv/Tantalum.csv")
te = pd.read_csv("data/mineral/csv/Tellurium.csv")
sn = pd.read_csv("data/mineral/csv/Tin.csv")
ti = pd.read_csv("data/mineral/csv/Titanium.csv")
w = pd.read_csv("data/mineral/csv/Tungsten.csv")
usmined = pd.read_csv("data/mineral/csv/USMined.csv")
usproc = pd.read_csv("data/mineral/csv/USProcessed.csv")
v = pd.read_csv("data/mineral/csv/Vanadium.csv")
y = pd.read_csv("data/mineral/csv/Yttrium.csv")
zn = pd.read_csv("data/mineral/csv/Zinc.csv")
zr = pd.read_csv("data/mineral/csv/Zirconium.csv")

alldf = [al, al2, sb, sb2, bar, bau, be, bi, b, br, cd, cr, 
           cr2, co, co2, cu, cu2, cu3, cu4, fel, fmo, fni, fno, fsi, 
           fv, flu, ga, ge, globalmined, globalproc, au, gra, importmined, 
           importprod, ind, i, fe, pb, pb2, pb3, li, mgc, mgm, mn, mn2, 
           mn3, hg, mica, mo, mon, ni, ni2, ni3, nio, nim, nb, pgm, pdm, 
           po, pl, pot, prodmined, prodproc, ree, rem, se, si, ag, smeltsn, 
           smeltzn, steel, sr, s, ta, te, sn, ti, w, usmined, usproc, v, y, zn, zr]


outjson = open("data/mineral/all.json", "w")
outhtml = open("data/mineral/all.html", "w")

for df in alldf:
    outjson.write(pd.DataFrame.to_json(df, orient="table", index=False))
    outjson.write("\n")
    outhtml.write(pd.DataFrame.to_html(df, index=False))
    outhtml.write("\n")
