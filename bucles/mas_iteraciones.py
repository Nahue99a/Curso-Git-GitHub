frutas = ["banana", "manzana", "ciruela", "pera", "naranja"]
cadena = "Hola como va?"
numero = [11, 8, 99, 24]

for fruta in frutas:
    if fruta == "pera":     #Forma de saltear un elemento y continuar con el for
        continue
    print (f"Me voy a comer una {fruta}")
    
    for fruta in frutas:      #Forma de terminar un bucle
        if fruta == "ciruela":
            break
        print (f"Me voy a comer una {fruta}")
        
#Recorrer una cadena de texto

for letra in cadena:
    print (letra)

#For en una sola linea de codigo

numeros_duplicados =  [x*2 for x in numero]

print(numeros_duplicados)