#refenciar o arquivo para abrir, pegar as posições da planilha separada por vírgula
import csv


def ler_arquivo():
   with open('manipulacao/curso-mvcad.csv', encoding="utf8") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter = ",")

    for item in leitor:
        print(item)
    lista_pessoa = [item for item in leitor]
    print(lista_pessoa)

ler_arquivo()