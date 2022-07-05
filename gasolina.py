import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
preços_gasolina = pd.read_csv('gasolina.csv',sep=',')
preços_gasolina
# código de geração do gráfico 
with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=preços_gasolina, x="dia",y="venda",palette="pastel")
  grafico.set(title='Preço da Gasolina por Dia', xlabel='Dias', ylabel='Preços');
  plt.savefig('gasolina.png')