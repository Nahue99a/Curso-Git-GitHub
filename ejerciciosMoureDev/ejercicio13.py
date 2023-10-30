#* Escribe una función que calcule y retorne el factorial de un número dado
#* de forma recursiva.

def calcular_factorial (numero):
    factorial = []
    resultado = 1
    factor = numero
    while factor > 0:
        factorial.append(factor)
        resultado = factor * resultado
        factor -= 1
    print (f"El factorial de {numero} es: {resultado}")
    
    
calcular_factorial (11)