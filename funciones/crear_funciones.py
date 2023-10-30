def saludar():      #Forma de crear una funcion
    print ("Hola que tal")
    
saludar()           #Forma de ejecutar una funcion

#Crear una funcion con parametro

def saludar_persona (nombre,sexo):
    sexo = sexo.lower()    #para que el parametro este en minuscula
    if (sexo == "mujer"):
        print (f"Hola {nombre}, maestra, como va?")
    else:
        print (f"Hola {nombre} maestro, como va?")
    
saludar_persona("Ludmila", "MUJER")

def crear_contraseña_random(num):
    chars= "abcdeifgt"
    num_entero = str(num)
    num = int (num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c3]}{num*2}"
    return contraseña
    
password = crear_contraseña_random(98)

frase = f"Tu contraseña nueva es: {password}"
print(frase)