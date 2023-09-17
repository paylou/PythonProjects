from math import sqrt, pow

cateto_oposto = float(input("Informe o valor do cateto oposto:  "))
cateto_adjacente = float(input("Informe o valor do cateto adjacente:   "))

hipotenusa = sqrt(pow(cateto_adjacente, 2) + pow(cateto_oposto, 2))

print(f"O valor da hipotenusa é:    {hipotenusa:.2f}")