ingreso_mensual = 100000
gasto_mensual = 8000

if ingreso_mensual >= 100000:
    if ingreso_mensual - gasto_mensual > 3000:
        print ("Ahora si estas bien")
    else:
        print ("Estas gastando de mas")
elif ingreso_mensual > 1000:
    print ("Estas bien economicamente en latinoamerica")
    
else:
    print ("Sos pobre")