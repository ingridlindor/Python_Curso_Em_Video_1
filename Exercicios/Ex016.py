#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela sua porção inteira
#Exemplo 6.876 mostre apenas 6
from math import trunc
n=float(input('Digite um valor: '))
print('A parte inteira do numero é {}'. format(trunc(n)))

# Outra alternativa sem importar nenhum modulo
print('A parte inteira do numero é {}'. format(int(n)))
