import csv

with open ("archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)     #forma de leer un archivo .csv
    for row in reader:
        print (row)