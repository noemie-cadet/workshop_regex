import re

with open("exo1.txt", "r") as file:
    txt = file.read()

rgx = re.compile("[A-Z]")
rgx
res = rgx.findall(txt)

for i in res:
    print(i)
print()