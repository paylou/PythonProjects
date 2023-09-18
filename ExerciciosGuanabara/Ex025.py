nome = str(input("Informe seu nome completo:    ")).strip().upper()

nomes = nome.split()

print(f"Existe o sobrenome 'SILVA' no nome {nome}?  {'SILVA' in nomes}")