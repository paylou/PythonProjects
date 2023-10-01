dist = float(input("Informe a distância da viagem em km:    "))

print(f"Sua viagem de {dist}km vai custar R${dist*0.5:.2f}" if dist <= 200 else f"Sua viagem de {dist}km vai custar R${dist*0.45:.2f}")