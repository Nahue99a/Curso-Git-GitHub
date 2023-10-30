lista = ["Nahuel", "Andujar", 24]
numero = [24, 11, 8, 1999]

print (len(lista)) #Cuenta la cantidad de elementos que tiene la lista

agregando_con_append = lista.append("Programador")    #Agrega un elemento a la lista
print (lista)

lista.insert(2, "Edad")     #Agrega un elemento a la lista en un indice especifico
print (lista)

lista.extend ([False, "2023"])  #Agrega una lista, como elementos individuales, a otra lista
print (lista)

lista.pop (2)   #Elimina un elemento por su indice, si le pasamos como parametro -1 se elimina el ultimo elemento de la lista
print (lista)

lista.remove ("2023")    #Remueve un elemento de la lista por su valor
print (lista)

numero.sort()   #Ordena la lista, no puede ordenar Strings, el parametro reverse = True lo ordena de forma decendente
print (numero)

numero.reverse () #Invierte los elementos de una lista, no puede ordenar Strings
print (numero)

lista.clear()   #Elimina todos los elementos de la lista
print (lista)