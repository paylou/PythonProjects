ano = int(input("Informe um ano qualquer:   "))

print(f"O ano {ano} é bissexto!" if ano % 4 == 0 else f"O ano {ano} não é bissexto!")