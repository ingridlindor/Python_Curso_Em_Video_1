#20
# O profeddor  quer sortear a ordem dos alunos que vao apresentar o trabalho, sao 4 alunos.

import random
n1= str(input('Primeiro Aluno: '))
n2= str(input('Segundo Aluno: '))
n3= str(input('Terceiro Aluno: '))
n4= str(input('Quarto Aluno: '))

lista = [n1,n2,n3,n4]
ordem = random.shuffle(lista)
print(' A ordem de apresentação será: ')
print(lista)