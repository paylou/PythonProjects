from random import shuffle
nome1 = input("Digite o nome do primeiro aluno: ")
nome2 = input("Digite o nome do segundo aluno: ")
nome3 = input("Digite o nome do terceiro aluno: ")
nome4 = input("Digite o nome do quarto aluno: ")

sequencia_nomes = [nome1, nome2, nome3, nome4]
shuffle(sequencia_nomes)

print(f"A ordem de apresentação será: {sequencia_nomes}")
