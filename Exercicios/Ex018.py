#18
#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente desse angulo

import math
angulo=float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangente= math.cos(math.radians(angulo))
print(' O angulo de {:.2f} tem o SENO de {:.2f}, a TANGENTE de {:.2f} e a tangente de {:.2f}' .format (angulo,seno,cosseno,tangente))