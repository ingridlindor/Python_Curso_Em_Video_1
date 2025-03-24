#17
#Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo e mostre a hipotenusa

from math import hypot
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
h=hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(h))