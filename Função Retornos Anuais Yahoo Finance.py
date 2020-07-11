def retornos_anuais_yahoo(ticker): 
    import yfinance as yf 
    ativo_precos=yf.download(ticker)['Adj Close']
    ativo_retornos = pd.DataFrame(ativo_precos.groupby([ativo_precos.index.year,ativo_precos.index.year]).tail(1).pct_change())
    ativo_retornos = ativo_retornos.set_index(ativo_retornos.index.year)
    ativo_retornos = ativo_retornos.rename(columns={'Adj Close':ticker})
    return ativo_retornos
