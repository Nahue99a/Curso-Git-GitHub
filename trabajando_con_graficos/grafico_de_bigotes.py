import pandas as pd
import matplotlib.pyplot as plt    #libreria de visualizacion de datos
import seaborn as sns       #libreria para generar graficos estadisticos

df = pd.read_csv ("trabajando_con_graficos\\bigotes.csv")

sns.boxplot(x="categoria",y="valor", data = df)    #generar el grafico

plt.show()                  #mostrar el grafico

