o = open("data/santacruz/isostatic/iso.csv", "w")

"""
Retain the relevant information as we extract it
from the iso.csv file.
"""

linelist = []
with open("data/santacruz/isostatic/iso.dec", "r") as file:
    for line in file:
        if line.split()[0] != "contour":
            if line.split()[0] == "ORD" or line.split()[0] == "SCR":
                if len(line.split()) == 15:
                    linelist.append([line.split()[0] + line.split()[1]] + line.split()[2:])
                elif len(line.split()) == 14: 
                    linelist.append([line.split()[0] + line.split()[1]] + line.split()[2:-2] + [""] + line.split()[-2:])
            elif len(line.split()) == 15:
                linelist.append(line.split()[:7] + line.split()[8:])
            elif len(line.split()) == 14:
                linelist.append(line.split())
            elif len(line.split()) == 13:
                linelist.append(line.split()[:-2] + [""] + line.split()[-2:])

