# Crie um programa que mostre quanto de dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar

real=(float(input('Quantos reais você tem? ')))
convercao=real/5
print('Com R$ {} reais é possivel comprar R${} dolares'.format(real,convercao))