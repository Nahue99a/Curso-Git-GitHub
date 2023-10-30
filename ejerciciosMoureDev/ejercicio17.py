""" /*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */ """
 
import random
 
def carrera_de_obstaculos (acciones, obstaculos):
         
     for i in obstaculos:
        jugar()
        
        if acciones == "1":
            if i == "_":
                obstaculos.insert(i, "x") 
        else:
            if i == "|":
                obstaculos.insert(i, "/")
        print (obstaculos)               
                
def jugar ():
    jugar = True
    while jugar == True:
        acciones = input ("Ingrese una opcion: 1- Saltar, 2- Correr")
        return acciones
             
         

def pista ():
    numero_aleatorio = random.randint(1,100) 
    print (numero_aleatorio)
    
    while numero_aleatorio != 0:
        if numero_aleatorio % 2 == 0:
            obstaculos.append("|")
        else:
            obstaculos.append("_")
            
        numero_aleatorio = numero_aleatorio - 1
    
    return obstaculos

acciones = ["correr", "saltar"]
obstaculos = []
pista()
print (obstaculos)
carrera_de_obstaculos(acciones, obstaculos )