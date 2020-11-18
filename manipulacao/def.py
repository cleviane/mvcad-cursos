import csv


def escrever_cabecalho(lista_cabecalho):
    with open('mvcad-exemplo-dict.csv', 'a') as file:
        escritor = csv.DictWriter(file,fieldnames=lista_cabecalho)
        escritor.writeheader()

def escrever_linhas(lista_cabecalho, lista_linhas):
    with open('mvcad-exemplo-dict.csv','a') as file:
        escritor = csv.DictWriter(file, fieldnames=lista_cabecalho)
        escritor.writerows(lista_linhas)