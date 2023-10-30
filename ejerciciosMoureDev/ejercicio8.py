#* Crea un programa se encargue de transformar un número
#* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def de_binario_a_decimal (numero):
    binario = []
    while numero != 0:
        bin = numero % 2
        numero = numero // 2
        binario.append (bin)
    binario.reverse()
    print(binario)
    
de_binario_a_decimal (1999)
    

    
