#Vamos fazer um histograma dos retornos diários do S&P500:
from pandas_datareader import data as wb 
import pandas as pd
import matplotlib.pyplot as plt 

dados_sp = pd.DataFrame()
dados_sp['S&P500']=wb.DataReader('^GSPC',data_source='yahoo',start='1970-01-01')['Adj Close']
dados_sp['Returns S&P500']=(dados_sp['S&P500'].pct_change())

plt.figure(figsize=(5,5))
plt.hist(dados_sp['Returns S&P500'],bins=100,edgecolor='black')
plt.title('S&P500 Daily Returns')
plt.ylabel('Absolute frequency')
plt.xlabel('Daily Returns')
plt.axis([-0.075,0.075,0,2300])
plt.show()
