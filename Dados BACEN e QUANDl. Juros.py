import quandl
import pandas as pd 

#Pegando dados de juros de países pelo site do BACEN e QUANDL:
juros_australia = quandl.get("BCB/17880",start_date='2010-01-01')
juros_canada = quandl.get("BCB/17881",start_date='2010-01-01')
juros_china = quandl.get("BCB/17899",start_date='2010-01-01')
juros_area_euro = quandl.get("BCB/17900",start_date='2010-01-01')
juros_eua = quandl.get("BCB/18152",start_date='2010-01-01')  
juros_japao = quandl.get("BCB/17903",start_date='2010-01-01')
juros_mexico = quandl.get("BCB/17904",start_date='2010-01-01')
juros_inglaterra = quandl.get("BCB/17908",start_date='2010-01-01')
juros_russia = quandl.get("BCB/17905",start_date='2010-01-01')
