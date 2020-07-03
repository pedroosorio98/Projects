#Vamos olhar quais foram os melhores e os piores dias de retornos no S&P500: 
import pandas as pd 
from pandas_datareader import data as wb 
import matplotlib.pyplot as plt 

dados_sp = pd.DataFrame()
tickers = ['^GSPC','^BVSP']
for t in tickers: 
     dados_sp[t]=wb.DataReader(t,data_source='yahoo',start='1996-01-01')['Adj Close']

dados_sp=dados_sp.rename(columns={'^GSPC':'S&P500','^BVSP':'IBOVESPA'})
dados_sp[['Returns S&P500','Returns IBOVESPA']]=(dados_sp[['S&P500','IBOVESPA']].pct_change())

piores_dias_ibovespa = dados_sp.nsmallest(10,'Returns IBOVESPA')[['Returns IBOVESPA']]
piores_dias_sp = dados_sp.nsmallest(10,'Returns S&P500')[['Returns S&P500']]
melhores_dias_ibovespa = dados_sp.nlargest(10,'Returns IBOVESPA')[['Returns IBOVESPA']]
melhores_dias_sp = dados_sp.nlargest(10,'Returns S&P500')[['Returns S&P500']]

display(melhores_dias_sp)
display(melhores_dias_ibovespa)
display(piores_dias_sp)
display(piores_dias_ibovespa)
