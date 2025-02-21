#Desafio 2 - Faça um programa que leia algo e mostre o seu tipo primitivo e todas as informaçõe possiveis sobre ele
x=(input('Digite algo: '))
print('O valor é alfa numerico? ',(x.isalnum()))
print('O valor é um numero? ', (x.isnumeric()))
print('O valor é um texto? ',(x.isalpha()))
print (' O valor é decimal  ?', (x.isdecimal()))