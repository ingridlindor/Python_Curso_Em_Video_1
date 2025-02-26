# Crie um programa que mostre quanto de dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar

real=(float(input('Quantos reais você tem? R$:')))
convercao=real/5
print('Com R$ {:.2f} reais é possivel comprar R${:.2f} dolares'.format(real,convercao))