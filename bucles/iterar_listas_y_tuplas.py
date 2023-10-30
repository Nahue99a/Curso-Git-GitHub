animales = ["gato", "perro", "loro", "bufalo"]
numeros = [11, 8, 99, 24]

for animal in animales:
    print(f"la variable animal es igual a: {animal}")
    
for numero in numeros:
    resultado = numero * 10
    print (resultado)
    
for numero, animal in zip(animales, numeros):   #Forma de recorrer dos listas al mismo tiempo con un for
    print (f"Recorriendo lista 1: {numero}")
    print (f"Recorriendo lista 2: {animal}")

for num in range (5,10):    #Definir un for que muestra cada numero en un rango
    print (num)
    
for num in enumerate(numeros):  #Recorre una lista por su indice
    print(num)
    
for numero in numeros:      #Usando For Else
    print (f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print ("el bucle termino")