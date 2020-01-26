def normalizar(base,valor):
    norm = list(range(len(base)+1))
    norm[0] = valor
    for i in range(len(base)+1)[1:]:
        norm[i] = norm[i-1]*(1+base[i-1])
       
    return norm 

def vol(base):
    x = 0
    for i in range(len(base))[1:]:
        x += base[i]/base[i-1]-1
       
    media = x/(len(base)-1)
    s = 0
    for i in range(len(base))[1:]:
        s += ((base[i]/base[i-1]-1)-media)**2
     
    return (s/(len(base)-1))**(1/2)*(252)**(1/2)

def desviopadrao(base):
    media = sum(base)/len(base)
    s=0
    for i in range(len(base)):
        s+=(base[i]-media)**2
       
        resultado = math.sqrt(s/len(base))
    return resultado


def retornosdaserie(base):
    serie = []
    for i in range(len(base))[1:]:
        serie.append(base[i]/base[i-1]-1)
   
    return serie 

def media(base):
    return sum(base)/len(base)

#calcula o retorno de uma estratégia que compra a ação se o dia anterior teve retorno positivo:
def estrategiaretornopositivo(base):
    est=[]
    for i in range(len(base))[2:]:
        if base[i-1]>base[i-2]:
            est.append(base[i]/base[i-1]-1)
        else:
            est.append(0)
       
    return est

#calcula o retorno de uma estratégia que compra a ação se o dia anterior teve retorno negativo:
def estrategiaretornonegativo(base):
    est=[]
    for i in range(len(base))[2:]:
        if base[i-1]<base[i-2]:
            est.append(base[i]/base[i-1]-1)
        else:
            est.append(0)
       
    return est
