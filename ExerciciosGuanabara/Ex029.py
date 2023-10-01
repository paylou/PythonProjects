velocidade = float(input("Informe a velocidade do seu carro em km/h:  "))

if velocidade <= 80:
    print("Não ultrapasse os 80km/h ou ira levar multa!")
else:   
    print(f"Voce ultrapassou os 80km/h e foi multado em R$ {(velocidade - 80)*7:.2f} ")