import yfinance as yf
import matplotlib.pyplot as plt

usdbrl = yf.download('USDBRL=X',start="2000-01-10",end="2020-01-01")
usdjpy = yf.download('USDJPY=X',start="2000-01-10",end="2020-01-01")
usdeur =  yf.download('USDEUR=X',start="2000-01-10",end="2020-01-01")
usdars =  yf.download('USDARS=X',start="2000-01-10",end="2020-01-01")
usdgbp = yf.download('USDGBP=X',start="2000-01-10",end="2020-01-01")
usdchf=yf.download('USDCHF=X',start="2000-01-10",end="2020-01-01")
usdinr=yf.download('USDINR=X',start="2000-01-10",end="2020-01-01")
usdcad=yf.download('USDCAD=X',start="2000-01-10",end="2020-01-01")
usdcny=yf.download('USDCNY=X',start="2000-01-10",end="2020-01-01")

plt.figure(figsize=(20,10))
plt.plot(usdbrl.Close,label="USD-BRL(BRASIL)")
plt.plot(usdeur.Close,label="USD-EUR(EURO)")
plt.plot(usdgbp.Close,label="USD-GBP(Inglaterra)")
plt.plot(usdchf.Close,label="USD-CHF(Suíça)")
plt.plot(usdcad.Close,label="USD-CAD(Canadá)")
plt.plot(usdcny.Close,label="USD-CNY(China)")
plt.legend()
