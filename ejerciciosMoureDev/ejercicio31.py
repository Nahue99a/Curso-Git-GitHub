""" * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio. """

def biciesto (año):
    biciesto = []
    while año % 4 != 0:
        año = año + 1
    biciesto.append(año)
    for i in range (1, 30):
        if i <= 30:
            año = año + 4
            biciesto.append(año)
    print (biciesto)


año = input("Indique un año: ")
año = int(año)
biciesto (año)
