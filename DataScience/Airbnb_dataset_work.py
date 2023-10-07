import pandas as pand

# Defining the columns to read
usecolunm = ["room_id", "rate_type"]
file = pand.read_csv('DataSets/seattle_01.csv', usecols=usecolunm ,index_col='id')
file.head()
print(file)
