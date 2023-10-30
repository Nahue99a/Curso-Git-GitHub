#Pedir nombre y edad de los compañeros

def obtener_compañeros (cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input ("Ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append (compañero)
    compañeros.sort(key = lambda x:x[1])
    asistente = compañeros[0][0]    #Ingresa al primer elemento de la lista, al ser una tupla tambien identificamos que use el primer elemento dentro de la tupla
    profesor = compañeros [-1][0]   #Ingresa al ultimo elemento de la lista
    return asistente, profesor

asistente, profesor = obtener_compañeros (5)

print (f"El profesor es {profesor}, y su asistente {asistente}")
