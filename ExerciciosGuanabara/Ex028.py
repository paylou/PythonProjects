from random import randint
from time import sleep
random_number = randint(0, 5)

print(":-="*20 + "\n\t Vou pensar num numero entre 0 e 5 \n" + ":-=" *20)
try_number = int(input(" Tente advinhar o numero que eu pensei:     "))

print("EM ANALISE...")
sleep(3)

if random_number == try_number:
    print(f"Você ganhou! O numero que eu pensei foi mesmo o {random_number}.")

else:
    print(f"Eu ganhei! Eu pensei no {random_number}, mas voce pensou no {try_number}")

