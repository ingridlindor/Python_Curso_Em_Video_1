# Leia o salario do funcionario e mostre seu novo salario com 15% de aumento
salario=float(input('Qual é o seu salario? '))
n_salario=salario +((15/100)*salario)
print(' Seu novo salario ser[a de R${}'.format(n_salario))