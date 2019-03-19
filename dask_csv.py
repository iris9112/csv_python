import dask.dataframe as dd

# leer el archivo 
filename = 'csv_for_test/311_Service_Requests.csv'

# defino el tipo como str para evitar algunos problemas con este archivo
df = dd.read_csv(filename, dtype='str')

print(df.head()) # 19seg

# eliminar espacios en blanco del nombre de las columnas
df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})

# crear un nuevo dataframe solo con las llamadas debido a problemas con el 'RADIATOR'
radiator_df = df[df.Descriptor=='RADIATOR']

# me retorna un tipo de dato dd.Scalar<series-..., dtype=int32>
radiator_df.Descriptor.count()

# esta funcion si calcula el numero de registros
# [67751 rows x 38 columns]
print(radiator_df.compute()) 

