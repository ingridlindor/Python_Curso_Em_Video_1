# Tipos Primiticos de Dados

#Int
numeroInteiro=int(7)

#float
numeroDecimal=float(7.8)

#bool
booleano=(True)
booleano=(False)

#srt
texto=('Ola mundo')
textoVazio=('')

#Outra forma de fazer um print
soma=5+4
print('A soma vale {}'.format(soma))

# Desafio 1 - Faça um programa que leia dois numero e retorne '' A some entre o n1 e n2 é igual a ...'' 
n1=(int(input('Primeiro Numero: ')))
n2=(int(input('Segundo Numero: ')))
soma=n1+n2
print('A soma entre {} e {} é igual a {}'.format(n1,n2,soma))

#Desafio 2 - Faça um programa que leia algo e mostre o seu tipo primitivo e todas as informaçõe possiveis sobre ele
x=(input('Digite algo: '))
print('O valor é numerico? ',(x.isalnum))
#Desafio 2 - Faça um programa que leia algo e mostre o seu tipo primitivo e todas as informaçõe possiveis sobre ele
x=(input('Digite algo: '))
print('O valor é alfa numerico? ',(x.isalnum()))
print('O valor é um numero? ', (x.isnumeric()))
print('O valor é um texto? ',(x.isalpha()))
print (' O valor é decimal  ?', (x.isdecimal()))

