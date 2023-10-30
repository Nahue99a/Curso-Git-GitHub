# * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# * Hecho esto, imprime los números primos entre 1 y 100.
 
""" def es_primo ():
    numero = 1
    primos = []
    while numero <= 100:
            primos.append (numero)
            
        numero += 1
    return primos """
    
def es_primo (num):
    for i in range (2, num - 1):
        if num%i == 0: return False          #Si el resto de i es != a 0 es primo
    return True

def primo_hasta (num):
    primos = []
    for i in range (num):
        resultado = es_primo (i)
        if resultado == True: primos.append (i)
    return primos

resultado = primo_hasta (100)
print (resultado)