applestock = yf.Ticker("AAPL")
hist = applestock.history(start="2000-10-10",end="2010-10-10")

applestock.actions
print(applestock.dividends)
print(hist)
