frase = str(input("Digite uma frase:    ")).strip().upper()

print(f"Nessa frase a letra 'A' aparece {frase.count('A')} vezes, e o primeiro 'A' aparece na posição {frase.find('A')}, e o segundo 'A' aparece na posição {frase.rfind('A')}")
