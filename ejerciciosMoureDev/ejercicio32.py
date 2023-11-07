"""  * Dado un listado de números, encuentra el SEGUNDO más grande.
 """

def segundo_mas_grande (lista):
    lista.sort(reverse = True)
    print (lista[1])

lista = [2, 5, 8 ,9, 12, 1, 53, 25]
segundo_mas_grande(lista)