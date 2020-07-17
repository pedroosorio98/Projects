#Vamos montar uma estratégia de médias móveis para CSNA3: 
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas_datareader import data as wb 

ticker= 'CSNA3.SA'

def strategy(base): 
    if base['10 Days SMA']>base['30 Days SMA']: 
            return base['Next Day Return']
    else: 
            return -base['Next Day Return']

data_ticker = wb.DataReader(ticker,data_source='yahoo',start='2010-01-01')['Adj Close']
data_backtest = data_ticker.to_frame()
data_backtest['Daily Returns'] = data_backtest['Adj Close'].pct_change()
data_backtest['Next Day Return'] = data_backtest['Daily Returns'].shift(-1)
data_backtest['10 Days SMA'] = data_backtest['Adj Close'].rolling(window=10).mean()
data_backtest['30 Days SMA'] = data_backtest['Adj Close'].rolling(window=30).mean()
data_backtest['Strategy Returns']= data_backtest[29:].apply(strategy,axis=1).shift(1)
data_backtest['Strategy Performance']= data_backtest['Strategy Returns'][29:].fillna(0).add(1).cumprod()
data_backtest['Asset Performance'] = data_backtest['Adj Close'][29:]/data_backtest['Adj Close'][29]
plt.figure(figsize=(16,5))
plt.plot(data_backtest['Strategy Performance'][29:],label="Strategy Performance")
plt.plot(data_backtest['Asset Performance'][29:],label='Asset Performance')
plt.title(ticker)
plt.legend()
plt.show()

data_results = pd.DataFrame()
data_results['Strategy Returns']=data_backtest['Strategy Performance'].resample('Y').last().pct_change()
data_results['Asset Returns']=data_backtest['Asset Performance'].resample('Y').last().pct_change()
data_results.loc['Acumulado']=data_backtest['Strategy Performance'][-1]/data_backtest['Strategy Performance'][29]-1,\
                              data_backtest['Asset Performance'][-1]/data_backtest['Asset Performance'][29]-1
display(data_results)
