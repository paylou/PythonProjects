nome = str(input("Informe seu nome completo:    ")).strip()

nomes_divididos = nome.split()

print(f"Seja bem vindo(a), {nomes_divididos[0]} {nomes_divididos[-1]}")