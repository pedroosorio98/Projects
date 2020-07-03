#Vamos fazer uma regressão com USD-BRL: 
import pandas as pd 
from pandas_datareader import data as wb 
import numpy as np 
from scipy import stats 
import statsmodels.api as sm 
import matplotlib.pyplot as plt

#definimos o ticker do USD-BRL:
tickers = ['USDBRL=X']
base_moeda=pd.DataFrame()

#Vamos pegar os preços no yahoo finance e passar tudo para um data frame:
for i in tickers: 
    base_moeda[i]=wb.DataReader(i,data_source='yahoo',start='2010-01-01')['Adj Close']

#Adicionando no data frame os retornos e os retornos do dia anterior: 
base_moeda['Retorno']=base_moeda/base_moeda.shift(1)-1
base_moeda['Retorno Dia Anterior']=base_moeda['Retorno'].shift(1)
base_moeda = base_moeda.iloc[2:]

#Fazemos uma regressão querendo explicar o retorno do USD-BRL pelo retorno do dia anterior: 
X = base_moeda['Retorno Dia Anterior']
Y = base_moeda['Retorno']
X1 = sm.add_constant(X)
reg = sm.OLS(Y,X1).fit()
print(reg.summary())     #p-valor muito pequeno!

#Plotamos tudo: 
plt.scatter(base_moeda['Retorno Dia Anterior'],base_moeda['Retorno'])
plt.plot(X,stats.linregress(X,Y).slope*X+stats.linregress(X,Y).intercept,color='Red')
plt.xlabel('Retorno Dia Anterior')
plt.ylabel('Retorno')
plt.title('Retorno USD-BRL x Retorno USD-BRL do dia Anterior')
plt.show()

#Plotamos tudo com um pouco mais de zoom: 
plt.scatter(base_moeda['Retorno Dia Anterior'],base_moeda['Retorno'])
plt.plot(X,stats.linregress(X,Y).slope*X+stats.linregress(X,Y).intercept,color='Red')
plt.xlabel('Retorno Dia Anterior')
plt.ylabel('Retorno')
plt.title('Retorno USD-BRL x Retorno USD-BRL do dia Anterior')
plt.axis([-0.05,0.05,-0.05,0.05])
plt.show()

#Agora vamos testar uma estratégia que vai comprar se o retorno do dia anterior foi negativo e vender caso contrário: 
def f1(row):
    if row['Retorno Dia Anterior'] < 0:
        valor = row['Retorno']
    elif row['Retorno Dia Anterior'] > 0:
        valor = -row['Retorno']
    else:
        valor = 0
    return valor

def normalizar(base,valor):
    norm = []
    norm.append(100)
    for i in range(len(base))[1:]: 
        norm.append((1+base[i])*norm[i-1])
    
    return norm

base_moeda=pd.DataFrame()
#Vamos pegar os preços no yahoo finance e passar tudo para um data frame:
for i in tickers: 
    base_moeda[i]=wb.DataReader(i,data_source='yahoo',start='2009-12-31')['Adj Close']
    
#Adicionando no data frame os retornos e os retornos do dia anterior: 
base_moeda['Retorno']=base_moeda/base_moeda.shift(1)-1
base_moeda['Retorno Dia Anterior']=base_moeda['Retorno'].shift(1)
    
#Inserindo a Estratégia: 
base_moeda['Retornos Estratégia']=base_moeda.apply(f1,axis=1)
base_moeda['Base 100 Estratégia']=normalizar(base_moeda['Retornos Estratégia'],100)

#Plotando a Estratégia: 
base_moeda['Base 100 Estratégia'].plot(figsize=(10,5),label='Estratégia')
plt.title('Estratégia USD-BRL')
plt.plot((base_moeda['USDBRL=X']/base_moeda['USDBRL=X'].iloc[0])*100,label='USD-BRL')
plt.ylabel('Index=100')
plt.legend()
plt.show()
