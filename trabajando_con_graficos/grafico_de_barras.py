import pandas as pd
import matplotlib.pyplot as plt    #libreria de visualizacion de datos
import seaborn as sns       #libreria para generar graficos estadisticos

df = pd.read_csv ("trabajando_con_graficos\\nahue_ingresos.csv")

sns.barplot(x="fuente",y="ingresos", data=df)    #generar el grafico

plt.show()                  #mostrar el grafico

total_ingresos = df["ingresos"].sum()   #obteniendo el total de ingresos
print (f"El total de ingresos es de: ${total_ingresos}")
