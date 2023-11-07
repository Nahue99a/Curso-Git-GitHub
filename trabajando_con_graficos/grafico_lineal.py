import pandas as pd
import matplotlib.pyplot as plt    #libreria de visualizacion de datos
import seaborn as sns       #libreria para generar graficos estadisticos

df = pd.read_csv ("trabajando_con_graficos\\goles.csv")

sns.lineplot(x="fecha",y="goles", data = df)    #generar el grafico

plt.plot("01-14",12,"o")    #marca un punto "o" en el grafico con las cordenadas que le pasamos

plt.show()                  #mostrar el grafico

