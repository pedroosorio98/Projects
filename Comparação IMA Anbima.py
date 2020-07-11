import quandl 
import pandas as pd 

#IMPORTAMOS O IMA-B, IMA-B-5 e IMA-G:
ima_b = quandl.get("BCB/12466").pct_change()
ima_b_retornos_anuais = ((ima_b.add(1).cumprod()).groupby([ima_b.index.year,ima_b.index.year]).tail(1)).pct_change()

ima_b_5 = quandl.get("BCB/12467").pct_change()
ima_b_5_retornos_anuais = ((ima_b_5.add(1).cumprod()).groupby([ima_b_5.index.year,ima_b_5.index.year]).tail(1)).pct_change()

ima_g = quandl.get("BCB/12469").pct_change()
ima_g_retornos_anuais = ((ima_g.add(1).cumprod()).groupby([ima_g.index.year,ima_g.index.year]).tail(1)).pct_change()

#CRIAMOS UM DATAFRAME COM O RETORNO ANUAL DE CADA UM: 
IMA = pd.DataFrame()
IMA['IMA-B']=ima_b_retornos_anuais['Value']
IMA['IMA-B-5']=ima_b_5_retornos_anuais['Value']
IMA['IMA-G']=ima_g_retornos_anuais['Value']

#PEGAMOS APENAS DE 2010-2020:
IMA_2010_2020 = IMA[6:].set_index(IMA[6:].index.year)

#CALCULAMOS O RETORNO ACUMULADO DE CADA UM E INSERIMOS EM UMA LISTA:
retorno_acumulado = [(IMA_2010_2020.add(1).cumprod().tail(1)-1).iloc[0,0],(IMA_2010_2020.add(1).cumprod()
                    .tail(1)-1).iloc[0,1],(IMA_2010_2020.add(1).cumprod().tail(1)-1).iloc[0,2]]

#ADICIONAMOS UMA LINHA COM OS RETORNOS ACUMULADOS NO DATA FRAME: 
IMA_2010_2020.loc['ACUMULADO'] = retorno_acumulado

#CALCULAMOS O CAGR DE CADA UM E INSERIMOS UMA NOVA LINHA COM ELES: 
IMA_2010_2020.loc['CAGR']=(IMA_2010_2020.loc['ACUMULADO'].add(1))**0.1-1

display(IMA_2010_2020*100)
