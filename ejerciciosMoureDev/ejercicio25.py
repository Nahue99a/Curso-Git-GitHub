""" * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2". """

import random

""" def ganador (jugadas):
    
     """
def juego ():
    jugadasMaquina = []
    decicion = input("Ingrese una opcion: 1- Jugar, 2- Terminar ")
    while decicion == 1:
        numeroRandom = random.randint(1,3)
        if numeroRandom == 1:
            accionMaquina = "R"
            jugadasMaquina.append(accionMaquina)
            decicion = input("Quiere seguir jugando?: 1- SI, 2- NO ")
            print(jugadasMaquina)
        elif numeroRandom == 2:
            accionMaquina = "S"
            jugadasMaquina.append(accionMaquina)
            decicion = input("Quiere seguir jugando?: 1- SI, 2- NO ")
            print(jugadasMaquina)
        else:
            accionMaquina = "P"
            jugadasMaquina.append(accionMaquina)
            decicion = input("Quiere seguir jugando?: 1- SI, 2- NO ")
            print(jugadasMaquina)
            
    
juego()
        