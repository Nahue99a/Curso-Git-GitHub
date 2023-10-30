diccionario = {
    "nombre": "Nahuel",
    "apellido": "Andujar",
    "edad": 24
}

for key in diccionario:     #Recorrer un diccionario y obtener solo las claves
    print (key)

for datos in diccionario.items():     #Forma de recorrer un diccionario con clave y valor
    key = datos[0]
    value = datos[1]
    print (f"La clave es: {key} y el valor es: {value}")