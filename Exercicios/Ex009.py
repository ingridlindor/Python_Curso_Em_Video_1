# Faça um programa que leia um numero inteiro e mostre sua tabuada
n=(int(input('Digite um numero: ')))
x=0
while x <= 10:
    m=n*x
    print('{} x {} = {}'.format(n,x,m))
    x +=1