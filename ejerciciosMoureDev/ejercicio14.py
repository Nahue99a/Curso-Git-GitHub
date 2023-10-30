#* Escribe una función que calcule si un número dado es un número de Armstrong
# * (o también llamado narcisista).
# * Si no conoces qué es un número de Armstrong, debes buscar información 
# * al respecto.

def armstrong (numero):
    largo = len(numero)
    numero = int(numero)
    auxiliar = numero
    almacenamiento = []
    resultado = 0
    
    while numero // 10 != 0:
        almacenamiento.append(numero%10)
        numero = numero // 10
    almacenamiento.append(numero%10)    
    
    for i in almacenamiento:
        resultado = resultado + i ** largo
    
    if resultado == auxiliar:
        print(f"El numero: {auxiliar} es un numero de Armstrong")
    else:
        print(f"El numero {auxiliar} no es un numero de Armstrong")
    
    
numero = input ("Ingrese un numero: ")
armstrong (numero)

    