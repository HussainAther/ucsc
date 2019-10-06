o = open("isofixed.dec", "w")

strlist = []
with open("iso.dec", "r") as file:
    for bigstring in file:
        for i in bigstring.split():
            strlist.append(i.replace("\n", ""))
            if len(strlist) % 14 == 0:
                strlist.append("\n")

curstr = ""
for i in strlist:
    if i == "\n":
        o.write(curstr)
        curstr = ""
    else:
        curstr += i + "," 
