import openpyxl as xl
arquivo = xl.load_workbook('pssa3.xlsx')
plan = arquivo.get_sheet_by_name('PSSA3')
plan['A1']='DATA PSSA3'
plan.title='PSSA3'

ultimodadodepreco = len(plan['E'])+1

plan.cell(row=1,column=8).value = 'Retornos diários'
#vamos inserir uma série de rentabilidade com base nos preços na coluna H.
for i in range(3,ultimodadodepreco):
    plan.cell(row=i,column=8).value = plan.cell(row=i,column=5).value/plan.cell(row=i-1,column=5).value-1
    

j=3
min = plan.cell(row=j,column=5).value/plan.cell(row=j-1,column=5).value-1

for i in range(3,ultimodadodepreco):
    if (plan.cell(row=i,column=5).value)/(plan.cell(row=i-1,column=5).value)-1 < min:
        min = (plan.cell(row=i,column=5).value)/(plan.cell(row=i-1,column=5).value)-1
    

plan.cell(row=1,column=9).value="Retorno Mínimo" 
plan.cell(row=2,column=9).value=min 

arquivo.save('pssa3.xlsx')
