import re

with open("exo2.txt", "r") as file:
    txt = file.read()


rgx = re.compile("(.* : \\{[^\\}]*\\})")
cmd = rgx.findall(txt)

rgx2 = re.compile("(\\#.*\n)")
com = rgx2.findall(txt)

res = re.sub("[*\n]", '', (re.sub(rgx2, '', (re.sub(rgx, '', txt)))))

if len(res) != 0:
    print("ERROR")
else:
    print(txt)