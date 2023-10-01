"""Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input("Informe seu salário:     "))
salario_com_aumento = salario + (salario*(10/100)) if salario > 1250.00 else salario + (salario*(15/100))

print(f"Seu salario antigo era {salario}, e seu novo salario será {salario_com_aumento}")
