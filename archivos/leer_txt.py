archivo = open("archivos\\texto.txt", encoding="UTF-8")     #abrir un archivo, el encoding = "UTF-8" es para modificar el codigo y que se pueda leer en todos los dispositivos sin errores
#print (archivo.read())          #leer el contenido del archivo .txt

lineas_1 = archivo.readline () #Lee el texto por lineas

print (lineas_1)