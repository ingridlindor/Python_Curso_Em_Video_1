# Leia o preço de um produto e mostre seu novo valor com 5% de desconto
valor=float(input('Qual o valor original do produto? '))
novo_valor=valor -((5/ 100)*valor)
print('O novo valor com desconte é R$ {:.2f}'.format(novo_valor))