with open("archivos\\texto.txt", encoding = "UTF-8") as archivo:    #la forma optima de abir un texto
    print (archivo.read())
    
    contenido = archivo.read()
    
    print (contenido)
    