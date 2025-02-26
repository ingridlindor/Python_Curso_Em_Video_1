# Faça um programa que leia a largura e altura da parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-lo, sabendo que  cada litro de tinta pinta 2m²
largura=(float(input('Qual a largura da parede?')))
altura=(float(input('Qual a altura da parede? ')))
area=largura*altura
qt_tinta=area/2
print('Para pintar uma parede de {}m² será necessario {} litros de tinta'. format(area,qt_tinta))