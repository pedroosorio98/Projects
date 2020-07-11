def retornos_anuais_yahoo(ticker): 
    import yfinance as yf 
    ativo_precos=yf.download(ticker)['Adj Close']
    ativo_retornos = pd.DataFrame(ativo_precos.groupby([ativo_precos.index.year,ativo_precos.index.year]).tail(1).pct_change())
    return ativo_retornos
