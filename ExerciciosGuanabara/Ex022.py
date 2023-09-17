nome = input("Informe seu nome completo:     ")

print(f"Seu nome em maiúsculo é {nome.upper()}")
print(f"Seu nome em minúsculo é {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras sem contar os espaços")
print(f"Seu primeiro nome tem {len(nome[:nome.find(' ')])} letras")