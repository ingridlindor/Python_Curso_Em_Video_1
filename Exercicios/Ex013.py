# Calcule o aumento de salario
salario=float(input('Qual o salario do funcionario? '))
novo = salario + (salario *15 / 100)
print(' O novo salario com o aumento de 15% é {:.2f}'.format(novo))