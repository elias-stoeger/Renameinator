import os
from os import listdir
from os.path import isfile, join

print("What's the directory (with the / at the end)?")
where = str(input())

print("What is the part to remove?")
what = str(input())


onlyfiles = [f for f in listdir(where) if isfile(join(where, f))]

cleanFiles = []
for item in onlyfiles:
	new = item.split(what)
	try:
		cleanFiles.append(new[0] + new[1])
	except IndexError:
		cleanFiles.append(item)


for item, item1 in zip(onlyfiles, cleanFiles):
    path = where + item
    newpath = where + item1
    os.rename(path, newpath)

print("The episodes are now called:")
for item in cleanFiles:
    print(item)
