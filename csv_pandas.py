import pandas as pd
from sqlalchemy import create_engine


# ruta del archivo csv
file = 'csv_for_test/1000000SalesRecords.csv'

# imprimir cabeceras del archivo y 5 primeras filas
print(pd.read_csv(file, nrows=5))

# crear bd sqlite local para guardar el archivo grande
csv_database = create_engine('sqlite:///csv_database.db')

# definimos tamaño del trozo
chunksize = 100000

# iteradores
i = 0
j = 1

# vamos recorrer el archivo por trozos y almacenar en la db
# al tener los datos en BD podemos procesarlos sin preocuparnos por memoria
for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
    # eliminar espacios en blanco del nombre de las columnas
    df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
    df.index += j
    i +=1
    # ver que hace algo para no impacientarnos
    print('*'*10, 'guardando...')
    df.to_sql('table', csv_database, if_exists='append') 
    j = df.index[-1] + 1

# hacer consultas desde sqlite
data_countries_asia = pd.read_sql_query('SELECT Country FROM "table" WHERE Region="Asia"', csv_database)

# 146017 rows x 1 columns
print(data_countries_asia)