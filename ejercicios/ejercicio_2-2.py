#Creando una funcion que devuelva los numeros primos entre 0 y el argumento que pasamos

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

resultado = primo_hasta (13)
print (resultado)