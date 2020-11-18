'''
lista_vazia = []

lista_numeros = [1,2,3,4]

lista_strings = ['alini','pri']

lista_mista = [1, 'alini', lista_numeros]

#print(lista_mista[2])

devs = ['Andorinhas', 'Amelia','Azaleia', 'Melissa', 'Violeta']
num_letra_a = 0
for nome in devs:
    #Se a primeira letra for a
    if nome[0] == 'A':
        num_letra_a += 1
#print(num_letra_a)

n = int(input("Digite a quantidade de números que deseja processar: "))
maior = -1000000
menor = 1000000
entrada = map(int, input(f"Digite {n} números, separado por vírgula: ").split(","))

for atual in entrada:
    menor = min(menor, atual)
    maior = max(maior, atual)

#print(f"Maior: {maior}")
#print(f"Menor: {menor}")


presentes = int(input("Quantas pessoas estavam presentes: "))
lista = []
index = 0
while index < presentes:
    nome = input("Digite o nome da aluna presente: ")
    index += 1
    lista.append(nome)

lista.sort()
print("Participantes por ordem alfabética: ")
print("\n".join(lista))
'''
import csv

'''
arquivo = open('mvcad-exemplos', 'r')

arquivo.writelines("oi tudo bem clevi? ")
print(arquivo)



with open('mvcad-exemplo-csv.csv', 'w') as file:
    escritor = csv.writer(file)
    escritor.writerows('oi clevi')
'''


