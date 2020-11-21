import csv

from pessoa_psycopg import insere_pessoa, retorna_pessoas


def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimeter=',')

        #print(db.get_tables())
        lista_pessoas = [item for item in leitor]

       # cursor.execute("select relname from pg_class where ")
        #lista_pessoas = [item for item in leitor]
       # print(lista_pessoas)


       # for item in lista_pessoas:
             #print(item)

#ler_arquivo()
pessoa = {
    'nome':"Pryscila Power",
    'endereco':"Vila Nova",
    'cpf':"12312312312",
    'estado':"Santa Catarina",
    'turma':"MVCAD Python 1",
    'periodo':"matutino",
    'modulo':"MVCAD"
}
insere_pessoa(pessoa)
print(retorna_pessoas())