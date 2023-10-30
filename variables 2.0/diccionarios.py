#Otra forma de crear un diccionario
diccionario = dict (nombre = "Nahuel", apellido = "Andujar")

#Crea un diccionario solo con las keys, con valor por defecto: none
diccionario = dict.fromkeys (["nombre", "apellido"])

print (diccionario)

#Crea un diccionario con las keys, con valor por defecto "no se"
diccionario = dict.fromkeys (["nombre", "apellido"], "No se")