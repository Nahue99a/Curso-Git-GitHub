import pandas as pd  #importamos la libreria, se suele renomambrar como pd

#LA LIBRERIA PANDAS SE INSTALA POR CMD
    # pip para corroborar tener istalado pip
    # py -m pip install pandas
    
df = pd.read_csv("archivos\\datos.csv")     #df se refiere a data frame, names = [] crea los nombres de las columnas de la tabla
df2 = pd.read_csv("archivos\\datos.csv", names = ["name","lastname","age"])

nombres = df["nombre"]    #Obteniendo datos de la columna nombre

#ordendando el dataframe por la edad

""" df_ordenado = df.sort_values ("edad")

print (df_ordenado) """

#ordenandolo de forma descendente

""" df_ordenado = df.sort_values ("age", ascending = False)

print (df_ordenado) """

#concatenenado dos datasframe

""" df_concatenado = pd.concat([df, df2])
print (df_concatenado) """

#accediendo a la primer fila con head()
primer_fila = df.head(1)
print (primer_fila)

#accediendo a las ultima fila con tail ()

ultimas_fila = df.tail (1)
print (ultimas_fila)

#accediendo a la cantidad de filas y columnas con shape

""" filas_y_columnas = df.shape     #devuelve una tupla con la cantidad de filas y columnas, el [0] pertenece al primer valor de la tupla, el indice [1] pertenece al segundo
filas_totales = filas_y_columnas[0]
columnas_totales = filas_y_columnas [1]     #forma de acceder a las columnas """

#otra forma de hacerlo es desempaquetando

filas_totales, columnas_totales = df.shape

print (filas_totales, columnas_totales)

#obteniendo data estadistica del df

df_info = df.describe()

#accediendo a un elemento especifico del df con loc

""" elemento_especifico_loc = df.loc[2, "age"]

print (elemento_especifico_loc) """

#accediendo a un elemento especifico del df con iloc

elemento_especifico_iloc = df.iloc[2, 2]

print (elemento_especifico_iloc)

#accediento a todas las filas en una columna

apellidos = df.iloc[:,1]

print (apellidos)

#accediento a todas las columnas en una fila

datos_columna = df.loc[2,:]

print (datos_columna)

#accediendo a filas con edad mayor a 20

mayor_que_20 = df.loc[df["edad"] > 20,:]

print (mayor_que_20)