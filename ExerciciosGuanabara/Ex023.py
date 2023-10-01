numero = str(input("Informe um número de 0 a 9999:  ")).zfill(4)

print(f"Unidade:   {numero[-1]}")
print(f"Dezena:    {numero[-2]}")
print(f"Centena:   {numero[-3]}")
print(f"Milhar:    {numero[-4]}")

print(numero)

