'Simula algumas estratégias simples para ações do ibovespa com dados do Yahoo Finance. 

import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 

tickers = ['ITUB4.SA','B3SA3.SA','PETR4.SA','BRFS3.SA','MRFG3.SA','PSSA3.SA','LAME4.SA','WIZS3.SA',\
          'BBAS3.SA','ELET3.SA']

def normalizar(base,valor):
    norm = list(range(len(base)+1))
    norm[0] = valor
    for i in range(len(base)+1)[1:]:
        norm[i] = norm[i-1]*(1+base[i-1])
       
    return norm 

def vol(base):
    x = 0
    for i in range(len(base))[1:]:
        x += base[i]/base[i-1]-1
       
    media = x/(len(base)-1)
    s = 0
    for i in range(len(base))[1:]:
        s += ((base[i]/base[i-1]-1)-media)**2
     
    return (s/(len(base)-1))**(1/2)*(252)**(1/2)

def desviopadrao(base):
    media = sum(base)/len(base)
    s=0
    for i in range(len(base)):
        s+=(base[i]-media)**2
       
        resultado = math.sqrt(s/len(base))
    return resultado


def retornosdaserie(base):
    serie = []
    for i in range(len(base))[1:]:
        serie.append(base[i]/base[i-1]-1)
   
    return serie 

def media(base):
    return sum(base)/len(base)

#calcula o retorno de uma estratégia que compra a ação se o dia anterior teve retorno positivo:
def estrategiaretornopositivo(base):
    est=[]
    for i in range(len(base))[2:]:
        if base[i-1]>base[i-2]:
            est.append(base[i]/base[i-1]-1)
        else:
            est.append(0)
       
    return est

#calcula o retorno de uma estratégia que compra a ação se o dia anterior teve retorno negativo:
def estrategiaretornonegativo(base):
    est=[]
    for i in range(len(base))[2:]:
        if base[i-1]<base[i-2]:
            est.append(base[i]/base[i-1]-1)
        else:
            est.append(0)
       
    return est

#calcula o retorno de uma estratégia que compra a ação baseada na volatilidade anualizada dos últimos dias:
def estrategiavol(base,dias,volatilidade):
    est=[]
    for i in range(len(base))[dias:]:
        if vol(list(base[i-dias:i-1]))<volatilidade:
            est.append(base[i]/base[i-1]-1)
        else:
            est.append(0)
       
    return est

def reglin(y):
    x = list(range(len(y)))
    mediax = sum(x)/len(x)
    mediay = sum(y)/len(y)
    n = len(y)
    somax = sum(x)
    somay = sum(y)
   
    somaxy =0
    somax2 =0
    for j in x:
        somaxy += x[j]*y[j]
        somax2 += x[j]**2
       
    b =(n*somaxy-somax*somay)/(n*somax2-(somax)**2)
    a =(somay-b*somax)/n
   
    return a,b 

for i in range(len(tickers)):
            base_preco = yf.download(tickers[i],start="2017-01-01",end="2020-01-01")['Adj Close']
            plt.figure(figsize=(10,8))
            plt.plot(normalizar(estrategiavol(base_preco,4,0.35),1000),label='Volatilidade')
            plt.plot(normalizar(estrategiaretornonegativo(base_preco),1000),label='Retorno negativo')
            plt.plot(normalizar(estrategiaretornopositivo(base_preco),1000),label='Retorno positivo')
            plt.plot(normalizar(retornosdaserie(base_preco),1000),label='Ação')
            plt.title(tickers[i])
            plt.legend()
