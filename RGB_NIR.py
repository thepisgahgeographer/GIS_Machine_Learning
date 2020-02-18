import pandas as pd
import numpy as np

#Series - 1 Dimensional Data

s = pd.Series(np.random.randn(5), index = [1,3,5,6,8])

#print(s)
#print(s.dtype)


#DataFrame - 2 Dimensional Data

d = {"one": pd.Series([1,2,3], index=["a", "b", "c"]),
    "two": pd.Series([1,2,3,4], index=["a", "b", "c", "d"])}

test = {
    "Raster": "Imagery",
    "Sensor": "Worldview"
}

df = pd.DataFrame(d)
print(df)

#for t in test:
print(test)



from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import sys
import matplotlib

#%matplotlib inline

print("Python Version" + sys.version)

Images = ["RGB", "NIR", "IR"]
Dates = [2010, 2012, 2019]

DataSet = list(zip(Images, Dates))
print(DataSet)

df = pd.DataFrame(data = DataSet, columns=['Image', 'Date'])
print(df)


Location = "C:\\Users\\yuri7100\\Desktop\\csv\\text.csv"
Locations = "C:\\Users\\yuri7100\\Desktop\\csv\\texts.csv"
#df.to_csv(Location)

#dff = pd.read_csv(Location, names=["Image", "Date"])

df.to_csv(Location)

print(df.dtypes)

dff = pd.read_csv(Location, names=["Image", "Date"])
df

Sorted = df.sort_values(["Image"])
print(Sorted.head(1))

df["Date"].plot()