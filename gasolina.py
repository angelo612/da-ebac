import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
preços_gasolina = pd.read_csv('gasolina.csv',sep=',')
preços_gasolina
# código de geração do gráfico 
with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=preços_gasolina, x="dia",y="venda",palette="seagree")
  plt.savefig('gasolina.png')