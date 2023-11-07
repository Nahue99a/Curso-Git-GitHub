"""  * Enunciado: Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100. """
 
def batalla_pokemon (daño):
    vida_uno = 100
    vida_dos = 100
    while vida_uno or vida_dos > 0:
        break

def combate_uno (efectivo, ataque, defensa_dos):
    return

def combate_dos (efectivo, ataque_dos, defensa):
    return

def efectividad (tipo, tipo_dos):
    if tipo == "fuego":
        if tipo_dos == "fuego":
            efectivo = 0.5
            return efectivo
        elif tipo_dos == "agua":
            efectivo = 0.5
            return efectivo
        elif tipo_dos == "planta":
            efectivo = 2
            return efectivo
        
    return
            


#-------------* POKEMON UNO *--------------------# 
tipo = input("Que tipo es: ")
tipo = tipo.lower()
ataque = input("Cuanto ataque tiene: ")
ataque = int(ataque)
defensa = input("Cuanta defensa tiene: ")
defensa = int(defensa)
#-------------* POKEMON DOS *--------------------# 
tipo_dos = input("Que tipo es: ")
tipo_dos = tipo_dos.lower()
ataque_dos = input("Cuanto ataque tiene: ")
ataque_dos = int(ataque_dos)
defensa_dos = input("Cuanta defensa tiene: ")
defensa_dos = int(defensa_dos)


batalla_pokemon (tipo, ataque, defensa, tipo_dos, ataque_dos, defensa_dos)