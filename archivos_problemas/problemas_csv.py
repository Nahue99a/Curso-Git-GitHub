#cambiar el tipo de dato de una columna

import pandas as pd

df = pd.read_csv("archivos_problemas\\datos.csv")

df ['edad'] = df['edad'].astype(str)    #Convertir a string los datos de una columna
print (df["edad"])

df ["nombre"].replace ("Cavani", "Burro", inplace=True)     #Remplazando un dato
print (df["nombre"])

print(df)
df = df.dropna()     #Eliminando las filas con datos vacios, df.dropna(axis=1) elimina las columnas
print(df)

df = df.drop_duplicates()   #Eliminando las filas repetidas
print (df)

#Creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")