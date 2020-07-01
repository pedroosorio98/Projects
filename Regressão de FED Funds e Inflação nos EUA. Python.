#Vamos fazer uma regressão simples com juros e inflação nos EUA.
import quandl   #Estaremos pegando os dados do Quandl.
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm 
from scipy import stats

dado_fedfunds = quandl.get('FRED/FEDFUNDS',start_date='1960-01-01')
dado_infla = quandl.get('RATEINF/INFLATION_USA',start_date='1960-01-01')

#Vamos plotar esses dados e ver como é a relação entre eles: 
plt.scatter(dado_fedfunds,dado_infla)
plt.ylabel('Inflation Rate')
plt.xlabel('FED Funds Rate')
plt.title('FED FUNDS X INFLATION US')
plt.show()

#Criamos um data frame para botar estes dados, pois são de datas diferentes:
indicadores_econ = pd.DataFrame({'FED Funds Rate':np.array(dado_fedfunds.Value),'Inflation Rate':np.array(dado_infla.Value)})

#Fazemos uma regressão simples com método OLS(Ordinary Least Squares)
X = indicadores_econ['FED Funds Rate']
Y = indicadores_econ['Inflation Rate']
X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()
reg.summary()

#Agora plotamos o gráfico com a regressão: 
plt.scatter(dado_fedfunds,dado_infla)
plt.ylabel('Inflation Rate')
plt.xlabel('FED Funds Rate')
plt.plot(X,stats.linregress(X,Y).slope*X+stats.linregress(X,Y).intercept,color='Red')
plt.title('FED FUNDS X INFLATION US')
plt.show()
