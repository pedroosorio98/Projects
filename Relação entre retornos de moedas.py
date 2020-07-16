import pandas as pd
import matplotlib.pyplot as plt 

#Defino uma função que pega cotações do Yahoo Finance:
def yahoo_ticker_price(tickers):
    from pandas_datareader import data as wb
    return wb.DataReader(tickers,data_source='yahoo')['Adj Close']

dados=pd.DataFrame()

#Defino uma lista de tickers de moedas:
moedas = ['EURBRL=X','USDBRL=X','JPYBRL=X','GBPBRL=X','CADBRL=X','ARSBRL=X','INRBRL=X','CHFBRL=X','CNYBRL=X','RUBBRL=X']

#Faço uma sequência de fors que plotará os retornos das moedas em gráficos, sempre dois a dois: 
for i in moedas:
    for j in moedas:  
        if i != j:
            ativos = pd.DataFrame()
            ativos['Ativo1']= yahoo_ticker_price(i).pct_change()
            ativos['Ativo2']= yahoo_ticker_price(j).pct_change()
            plt.scatter(ativos['Ativo1'], ativos['Ativo2'])
            plt.ylabel(j)
            plt.xlabel(i)
            plt.show()
