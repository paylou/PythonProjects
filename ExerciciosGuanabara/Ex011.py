altura = float(input("Informe a altura da parede:  "))
largura = float(input("Informe a largura da parede: "))

area = altura * largura

tinta = area/2

print("São necessários {:.2f} litros de tinta para pintar a parede de {:.2f} metros quadrados".format(tinta, area))