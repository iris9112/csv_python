import pandas as pd
import dask.dataframe as dd

# Read the file

# data = pd.read_csv("csv_for_test/Accidents7904.csv", low_memory=False)
# pandas.errors.ParserError: Error tokenizing data. C error: out of memory

filename = 'csv_for_test/Accidents7904.csv'
data = dd.read_csv(filename, dtype='str')

# Output the number of rows
print("Total rows: {0}".format(len(data)))
print("-----------")

"""
Accidents which happened on a Sunday
el archivo Road-Accident-Safety-Data-Guide-1979-2004.xls contiene info extra
y puedes ver q el domingo tiene codigo 1
lo envio como string porque al cargar el df convertí todos los campos a este tipo
"""
accidents_sunday = data[data.Day_of_Week == '1']

print("Accidents which happened on a Sunday: {0}".format(len(accidents_sunday)))
print("-----------")

# Accidents in London on a Sunday
london_data = data[(data.Police_Force == '1') & (data.Day_of_Week == '1')]
print("Accidents in London from 1979-2004 on a Sunday: {0}".format(len(london_data)))