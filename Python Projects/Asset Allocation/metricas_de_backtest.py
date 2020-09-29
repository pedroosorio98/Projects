import pandas as pd 
import numpy as np 

# Mede o retorno anualizado: 
def retorno_anualizado(base_de_precos_diarios): 
    return (base_de_precos_diarios[-1]/base_de_precos_diarios[0])**(252/len(base_de_precos_diarios))-1

# Mede a perda máxima possível dentro de uma série de preços: 
def maximum_drawdown(base_de_precos_diarios): 
    return min(base_de_precos_diarios.div(base_de_precos_diarios.cummax()).add(-1))

# Mede a volatilidade anualizada: 
def volatilidade_anualizada(base_de_retornos_diarios):
    return base_de_retornos_diarios.std()*252**0.5

# Retorna uma série com o underwater, a perda entre cada ponto e o máximo passado: 
def drawdown_underwater(base_de_precos_diarios):
    return base_de_precos_diarios.div(base_de_precos_diarios.cummax()).add(-1)

# Mede a relação risco retorno levando em consideração uma taxa livre de risco:
def sharpe_ratio(base_de_retornos_diarios,base_de_retornos_diarios_taxa_livre_de_risco):
    return ((base_de_retornos_diarios.mean()-base_de_retornos_diarios_taxa_livre_de_risco.mean())/base_de_retornos_diarios.std())*252**0.5

# Mede o % de retornos positivos diários: 
def hit_ratio(base_de_retornos_diarios): 
    return (base_de_retornos_diarios>0).sum()/base_de_retornos_diarios.count()

# Mede a relação risco retorno mas sem punir a volatilidade para cima, contamos apenas a volatilidade dos retornos negativos:
def sortino_ratio(base_de_retornos_diarios,base_de_retornos_diarios_taxa_livre_de_risco):
    return ((base_de_retornos_diarios.mean()-base_de_retornos_diarios_taxa_livre_de_risco.mean())/base_de_retornos_diarios[base_de_retornos_diarios<0].std())*252**0.5

# Mede o % de janelas de k dias em que uma série de preços retornou mais que outra série de preços: 
def consistencia(base_de_precos_diarios,base_de_precos_benchmark_diarios,k):
    retornos_janela_de_k_dias = base_de_precos_diarios.div(base_de_precos_diarios.shift(k)).add(-1)
    retornos_janela_de_k_dias_benchmark = base_de_precos_benchmark_diarios.div(base_de_precos_benchmark_diarios.shift(k)).add(-1)
    return (retornos_janela_de_k_dias>retornos_janela_de_k_dias_benchmark).sum()/retornos_janela_de_k_dias.count()
