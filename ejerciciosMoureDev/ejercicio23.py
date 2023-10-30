#Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
# * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# * - No se pueden utilizar operaciones del lenguaje que 
# *   lo resuelvan directamente

def maximo_comun_divisor (numeroUno, numeroDos):
    numero = []
    for i in range(1, numeroUno):
        if numeroUno%i == 0 and numeroDos%i == 0:
            numero.append (i)
    print (f"El maximo comun divisor de {numeroUno} y {numeroDos} es: {numero[-1]}")
    

""" def minimo_comun_multiplo (numeroUno, numeroDos):
    
 """
maximo_comun_divisor (64, 8)