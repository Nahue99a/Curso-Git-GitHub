#Promedio de duracion

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duracion (Ejercicio A)

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100   #El curso de Dalto dura un 60% de lo que dura el curso minimo
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max /10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print (f"El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido")
print (f"El curso de dalto dura un {diferencia_con_max}% menos que el mas rapido")
print (f"El curso de dalto dura un {diferencia_con_promedio}% menos que el mas rapido")


#Calculando el % de tiempo vacio (Ejercicio B)

tiempo_vacio_promedio = 100 - otros_cursos_promedio // crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso // crudo_dalto * 100

print (f"Un curso promedio tiene un {tiempo_vacio_promedio}% de tiempo vacio promedio")
print (f"El curso de Dalto elimino un {tiempo_vacio_dalto}% de tiempo vacio promedio")