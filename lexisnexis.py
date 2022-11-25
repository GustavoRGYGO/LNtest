import re

teste = input('Insira a string desejada: ')

cnpj = '[0-9][0-9][.][0-9][0-9][0-9][.][0-9][0-9][0-9][/][0-9][0-9][0-9][0-9][-][0-9][0-9]'
cpf = '[0-9][0-9][0-9][.][0-9][0-9][0-9][.][0-9][0-9][0-9][-][0-9][0-9]'
date = '[0-9][0-9][/][0-9][0-9][/][0-9][0-9][0-9][0-9]'
cell = '[(][0-9][0-9][)][0-9][0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]'
tele = '[(][0-9][0-9][)][0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]'
email = r'[\D\.-]+@[\D\.-]+[.net|.org|.com]'
credcard = '[0-9][0-9][0-9][0-9][ |.|-][0-9][0-9][0-9][0-9][ |.|-][0-9][0-9][0-9][0-9][ |.|-][0-9][0-9][0-9][0-9]'

tab_cnpj = re.findall(cnpj, teste)
tab_cpf = re.findall(cpf, teste)
tab_date = re.findall(date, teste)
tab_cell = re.findall(cell, teste)
tab_tele = re.findall(tele, teste)
tab_email = re.findall(email, teste)
tab_cc = re.findall(credcard, teste)

for i in tab_cnpj:
    print(f"CNPJ                  | {i}")

for i in tab_cpf:
    print(f"CPF                  | {i}")

for i in tab_date:
    print(f"Date                  | {i}")

for i in tab_cell:
    print(f"Cellphone                  | {i}")

for i in tab_tele:
    print(f"Telephone                  | {i}")

for i in tab_email:
    print(f"Email                  | {i}")

for i in tab_cc:
    print(f"Credit Card                 | {i}")
    
