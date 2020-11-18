presentes = int (input("Quantas pessoas são presentes? "))
pessoas = []
for i in range(presentes):
  pessoas.append((input("Digite o nome do participante: ")))
pessoas.sort()
print("Participantes por ordem alfabetica: ")
print("\n".join(pessoas))