num1 = int(input("Informe o primeiro numero:    "))
num2 = int(input("Informe o segundo numero:    "))
num3 = int(input("Informe o terceiro numero:    "))

menor = num1

if num2  < menor:
    menor = num2
if num3 < menor:
    menor = num3

maior = num1

if num2  > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f"O maior numero é {maior}, e o menor numero é o {menor}")

