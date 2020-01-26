#Definimos uma função que utilizaremos no botão:
import pandas as pd
pssa3 = pd.read_csv('pssa3.csv',sep = ";")

def volatilidade(base):
    x = 0
    for i in range(len(base))[1:]:
        x += base[i]/base[i-1]-1
       
    media = x/(len(base)-1)
    s = 0
    for i in range(len(base))[1:]:
        s += ((base[i]/base[i-1]-1)-media)**2
     
    return (s/(len(base)-1))**(1/2)*(252)**(1/2)

def maxdrawdown(base):
    md = list(range(len(base)))
    for i in range(len(base)-1):
        md[i] = base[i:].min()/base[i]-1
   
    return min(md)
   
#Importamos todos os modulos do tkinter assim:
from tkinter import *
import tkinter as tk  
# criaremos agora a nossa janelas:
root = Tk()
#Definimos a dimensão da janela:
root.geometry('90x200')
#Vamos dar um título para a nossa janela:
root.title("Risk Management")
#Até aqui criamos a janela
#Vamos inserir nela um Label
l = Label(root, text="Cálculo do Maxdrawdown e da Volatilidade")
#Criamos o label, agora vamos exibir ele na janela:
l.pack(side=TOP)
#Vamos adicionar um quadrado colorido de decoração:
c = Canvas(root,height="5",width="1000",bg="black")
c.pack(side=TOP)

#Agora vamos inserir duas caixas de texto uma embaixo de cada botão:
#textomaxdrawdown = tk.Text(root,height="1",width="7")
#textomaxdrawdown.pack(side=LEFT)
#textovol = tk.Text(root,height="1",width="7")
#textovol.pack(side=RIGHT)



#Agora vamos adicionar um botão na janela, ele ficará na esquerda:
b1 = Button(root,text="Maxdrawdown",height="1",width="12", command=botaomaxdrawdown)
b1.pack()
resultadomaxdrawdown = tk.Text(root,height="1",width="12")
resultadomaxdrawdown.pack()

b2 = Button(root,text="Volatilidade",height="1",width="12", command=botaovolatilidade)
b2.pack()
resultadovolatilidade = tk.Text(root,height="1",width="12")
resultadovolatilidade.pack()

#Agora vamos inserir um menu com opções:
#mn = Menubutton(root,text="Menu de Opções")
#mn.menu = Menu(mn)
#mn["menu"] = mn.menu
#Agora adicionamos as opções e as funções para cada uma delas:
#mn.menu.add_command(label="Maxdrawdown",command=botaomaxdrawdown)
#mn.menu.add_command(label="Volatilidade",command=botaovolatilidade)
#mn.pack(side=TOP)


def botaomaxdrawdown():
    resultadomaxdrawdown.insert(tk.INSERT,str(maxdrawdown(pssa3.Close)))
    resultadomaxdrawdown.config(state="disabled")
 
   
def botaovolatilidade():
    resultadovolatilidade.insert(tk.INSERT,str(volatilidade(pssa3.Close)))
    resultadovolatilidade.config(state="disabled")
   
   
   
   
#Agora faremos com que a janela fique visivel pelo tempo que você desejar até fechar.
root.mainloop()
