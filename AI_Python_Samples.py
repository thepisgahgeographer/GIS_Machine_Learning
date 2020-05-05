from pathlib import Path
import fastai
from fastai import utils
import platform
import matplotlib 
from fastai.basics import *


#Working with PurePaths through pathlib
p = Path("C:\GIS_Data")
#print([x for x in p.iterdir() if x.is_dir()])
#print(list(p.glob('**/*.las')))

#print(platform)
#print('this is version {}.'.format(platform.python_version()))

Bike = {
    "color": "Gunmetal",
    "Frame": "Large",
    "travel": 160
}

for index, val in enumerate(Bike):
    print("Index: {}".format(index))
    print(val)

for vals in range(1,10):
    for values in range(1,10):
        print("{} X {} = {}".format(vals, values, vals*values))

#print(Bike["travel"])

#if "travel" in Bike:
#    print("True")

#print("5"*10)

#for letter in "Wilson Creek":
#    print(letter, end=':')


