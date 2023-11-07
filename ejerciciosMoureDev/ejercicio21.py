""" * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones. """
 

with open('ejerciciosMoureDev\\challenge21.txt', 'r') as archivo:       #FORMA DE RECORRER POR LINEAS UN TXT
    lineas = archivo.readlines()
    cantidad_lineas = len(lineas)
    for i in range (0, cantidad_lineas):
        print (lineas[i])
   