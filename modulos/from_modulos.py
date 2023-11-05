#from enrutamiento.modulo_saludar import saludar  #forma de importa solo una parte del codigo del modulo, asi se importa si la carpeta contenedora esta en la misma ruta

import sys          #forma de importa si la carpeta esta fuera de la ruta

sys.path.append("C:\\Users\\nahue\\OneDrive\\Escritorio\\PythonDalto\\enrutamientos_exteriores")    #añadir la ruta del modulo al que queremos acceder
print(sys.path)

import saludar_de_nuevo as modulo_saludo

print (modulo_saludo.saludar("Nahuel"))