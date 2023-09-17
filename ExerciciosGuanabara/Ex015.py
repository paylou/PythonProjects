dias = int(input("Por quantos dias seu carro foi alugado?   "))
km = float(input("Quantos km rodados?   "))

total = (dias*60) + (km*0.15)

print(f"O valor do aluguel é {total:.2f}")