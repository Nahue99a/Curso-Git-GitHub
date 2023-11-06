with open ("archivos\\texto.txt", "a", encoding = "UTF-8") as archivo:  
    archivo.write ("Probando de escribir una tercer linea")     #forma de sobreescribir un archivo
    
    archivo.writelines (["Estaoy agregando texto\n", " \n"])   #forma de sobreescribir un archivo con varias lineas, recibe una lista como parametro- \n es para dar un salto de linea
    archivo.writelines (["Quinteroooo\n", "Moriste en Madrid"])