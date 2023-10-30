cadena1 = "Hola soy Nahue"
cadena2 = "Bienvenido"

print(dir (cadena1)) #Devuelve todos los atributos

#Los metodos se usan PARAMETRO.METODO()

print (cadena1.upper()) #Convierte el String en mayuscula
print (cadena2.lower()) #Conveirte el String en minuscula
print (cadena1.capitalize()) #Convienrte la primer letra en mayuscula

print (cadena1.find("N")) #Devuelve la ubicacion del caracter, si no encuentra devuelve -1
print (cadena2.index("e")) #Devuelve la ubicacion del caracter, si no encuentra una coincidencia nos da una excepcion

edad = "24"
clave = "9a8b7c6d"

print (edad.isnumeric()) #Si es un string numerico devuelve True
print (clave.isalpha()) #Si es alphanumerico devuelve True, los espacios cuentan como caracteres especiales

print (cadena1.count("a")) #Devuelve la cantidad de veces que se repite el parametro, si no se encuentra devuelve 0
print (len(cadena2)) #Devuelve la cantidad de caracteres que tiene una cadena 

print (cadena2.startswith("B")) #Verifica si una cadena inicia con una cadena dada, devuelve True o False
print (cadena1.endswith ("o")) #Verifica si una cadena termina con una cadena dada, devuelve True o False

cadena_nueva = cadena1.replace ("Nahue", "Nahuelito")    #Si encuentra una coincidencia, remplaza un pedazo de la cadena por una cadena dada, necesita dos parametros, primero el que se remplaza y luego por el que se remplaza

print (cadena_nueva)

cadena_separada = cadena1.split(" ")     #Separar cadenas con la cadena que le pasemos, devuelve una lista

print (cadena_separada)

