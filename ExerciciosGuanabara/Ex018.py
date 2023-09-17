from math import sin, cos, tan, radians
angulo_graus = float(input("Informe um angulo em graus:   "))

angulo_rads = radians(angulo_graus)

print(f"Sobre o angulo de {angulo_graus}°, seu seno é {sin(angulo_rads):.2f}, seu cosseno é {cos(angulo_rads):.2f}, e sua tangente é {tan(angulo_rads):.2f}")