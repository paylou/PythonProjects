"""Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

lado1 = int(input("Informe o primeiro lado:     "))
lado2 = int(input("Informe o segundo lado:     "))
lado3 = int(input("Informe o terceiro lado:     "))

if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1  and (lado3 + lado1) > lado2:
    print("\033[32mÉ possivel sim formar um triangulo com os lados informados!")
else:
    print("\033[31mNão é possivel formar um triangulo com os lados informados :c")

