diccionario = {
    "nombre" : "Nahuel",
    "apellido" : "Anduajar",
    "edad" : 23
}

claves = diccionario.keys()     #Nos da las claves del diccionario
print (claves)

gets = diccionario.gets("nombre")   #Nos da el valor, si no encuentra el programa continua y no tira error 
print (gets)

pop = diccionario.pop ("nombre")    #Elimina el elemento
print (pop)



clear = diccionario.clear() #elimina todos los elementos del diccionario
