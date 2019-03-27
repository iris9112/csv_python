# CSV y python

Ejemplos de manejo de archivos csv con python.

## Ejercicios

- `csv_pandas.py` ejemplo simple para leer un archivo csv con pandas, guardar en una base de datos y leer desde ahí.
  - Link de datos de pruebas: [csv_for_test](https://drive.google.com/open?id=1pPkXCTKv4C2Gweb8c3C_r3c86kGPBX9S)

- `dask_csv.py` ejemplo usando dask para leer un archivo grande (7.43 GB) en csv.
  - Link de datos de pruebas: [311 Service Requests dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests/fvrb-kbbt)
  - Tiempo tomado en computar las 7gb de registros ~~ 4min

- `pandas_accidents.py` ejemplo de real python modificado para evitar el error: *out of memory*
  - Link de datos de prueba: [Accidents from data.gov.uk](http://data.dft.gov.uk/road-accidents-safety-data/Stats19-Data1979-2004.zip)

## Librerias usadas

- [Pandas](https://pandas.pydata.org/)
- [Dask](http://docs.dask.org/en/latest/)

## Links consultados

- [working-with-large-excel-files-in-pandas](https://realpython.com/working-with-large-excel-files-in-pandas/)
- [dask-large-csv-python](https://pythondata.com/dask-large-csv-python/)

## CSV y Django

- Obligatorio agregar el atributo `enctype="multipart/form-data"`, sino el request.FILES estará vacío.
- También el método de formulario debe ser el POST.
- Django proporciona dos campos modelo, `FileField` e `ImageField`, y los archivos cargados en ellos se almacenan en el sistema de archivos (MEDIA).
- `FileField` e `ImageField` se agregan a la base de datos como VARCHAR y contienen la referencia al archivo cargado. *En caso de que estos dos campos se eliminen de la base de datos, solo se eliminará la referencia al archivo físico.*
- Para acceder a `MEDIA_URL` en la plantilla se debe agregar `django.template.context_processors.media` a los procesadores de contexto.