#Vamos fazer uma regressão múltipla com ações do setor bancário: 
import pandas as pd 
from pandas_datareader import data as wb 
import numpy as np 
from scipy import stats 
import statsmodels.api as sm 
import matplotlib.pyplot as plt

#definimos os tickers das ações que utilizaremos: 
tickers = ['ITUB4.SA','SANB4.SA','BBDC4.SA','BBAS3.SA']
base_acoes=pd.DataFrame()

#Vamos pegar os preços no yahoo finance e passar tudo para um data frame:
for i in tickers: 
    base_acoes[i]=wb.DataReader(i,data_source='yahoo',start='2014-01-01')['Adj Close']

#Criamos uma base com os retornos diários de cada ativo: 
base_acoes_retornos = base_acoes/base_acoes.shift(1)-1

#Adicionamos na base colunas do retorno do dia anterior: 
base_acoes_retornos[['ITUB4.SA Anterior','SANB4.SA Anterior','BBDC4.SA Anterior','BBAS3.SA Anterior']]\
=base_acoes_retornos.shift(1)

#Tiramos as linha da base que possuem NAN: 
base_acoes_retornos = base_acoes_retornos.iloc[2:]

#Rodamos uma regressão querendo explicar o retorno de ITUB4 pelo retorno do dia anterior de cada ação: 
X = base_acoes_retornos[['ITUB4.SA Anterior','SANB4.SA Anterior','BBDC4.SA Anterior','BBAS3.SA Anterior']]
Y = base_acoes_retornos['ITUB4.SA']
X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()
reg.summary()
