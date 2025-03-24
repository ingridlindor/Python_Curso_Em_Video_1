#19
# O professor quer sortear um dos seus alunos para apagar o quadro, faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random
n1= str(input('Primeiro Aluno: '))
n2= str(input('Segundo Aluno: '))
n3= str(input('Terceiro Aluno: '))
n4= str(input('Quarto Aluno: '))

lista = [n1,n2,n3,n4]
escolhido =random.choice(lista)

print('O Aluno Escolhido foi {}'. format(escolhido))