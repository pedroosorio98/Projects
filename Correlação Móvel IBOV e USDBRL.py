#Vamos aprender a fazer uma correlação móvel entre ativos: 
from pandas_datareader import data as wb 
import pandas as pd 
import matplotlib.pyplot as plt 

#Importamos dados de USDBRL e Ibovespa:
data=pd.DataFrame()
data['USDBRL'] = wb.DataReader('USDBRL=X',data_source='yahoo',start='2005-01-01')['Adj Close']
data['IBOV'] = wb.DataReader('^BVSP',data_source='yahoo',start='2005-01-01')['Adj Close']

#Calculo os retornos diários da base: 
data_daily_returns = data.pct_change()

#Calculo a correlação móvel com janelas de 90 dias desde 2005 e em seguida plotamos:
correlacao_movel = data_daily_returns['USDBRL'].rolling(90).corr(data_daily_returns['IBOV'])
plt.figure(figsize=(6,2))
plt.plot(correlacao_movel)
plt.ylabel('Correlação')
plt.xlabel('Data')
plt.title('Correlação janelas de 90 dias')
plt.show()
