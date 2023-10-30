# * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
# * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.

opcion = input ("Ingrese una opcion: 1- Triangulo, 2- Rectangulo, 3- Cuadrado, 4- Salir")
opcion = int(opcion)

def area (opcion):
    while opcion >= 1 or opcion <=3:
         
        if opcion == 1:
            base = input("Ingrese el valor de la base: ")
            base = int(base)
            altura = input("Ingrese el valor de la altura: ")
            altura = int(altura)
            area = (base * altura) / 2
            print (f"El area del triangulo es: {area}")
            opcion = input ("Ingrese una opcion: 1- Triangulo, 2- Rectangulo, 3- Cuadrado, 4- Salir")  
            opcion = int(opcion)  
            
        elif opcion == 2:
            base = input("Ingrese el valor de la base: ")
            base = int(base)
            altura = input("Ingrese el valor de la altura: ")
            altura = int(altura)
            area = (base * altura)
            print (f"El area del rectangulo es: {area}")
            opcion = input ("Ingrese una opcion: 1- Triangulo, 2- Rectangulo, 3- Cuadrado, 4- Salir")  
            opcion = int(opcion) 
            
        elif opcion == 3:
            base = input("Ingrese el valor de la base: ")
            base = int(base)
            area = (base * base)
            print (f"El area del cuadrado es: {area}")
            opcion = input ("Ingrese una opcion: 1- Triangulo, 2- Rectangulo, 3- Cuadrado, 4- Salir")  
            opcion = int(opcion) 
        
        else:
            print ("Nos vemo")
            break

        
area (opcion)

      