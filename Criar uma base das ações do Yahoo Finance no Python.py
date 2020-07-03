import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

tickers = pd.read_csv('tickersacoesbr.csv',sep=";")
listadebases = list()
listadebases=[yf.download(tickers.Codigo[i],start="2019-01-01",end="2019-12-31").Close.rename(columns={'Close':tickers.Codigo[i]}, inplace=True) for i in range(len(tickers.Codigo))]
baseconjunta = pd.concat(listadebases, axis=1)

for i in range(len(tickers.Codigo)):
     baseconjunta.rename(columns={i:tickers.Codigo[i]}, inplace=True)
       
       
baseconjunta

baseconjunta.to_excel('Base preços das ações BR.xlsx')
