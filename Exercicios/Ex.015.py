#Calcular Aluguel de carro
#Calcule o preço a pagar sabendo que o carro custa 60 reais por dia e 15 centavos por km  rodado

dias=int(input('Por quantos dias voce ficou com o carro? '))
km =float(input('Quantos KM voce andou? '))

valorpg =(dias * 60) +(km * 0.15)

print('O valor total é de {:.2f}'.format(valorpg))