#programa que leia o valor em metros e exiba convertido em centrimetros e milimetros
m=float(input('Digite quantos metros deseja converter: '))
cm=m*100
ml=m*1000

print ('{} metros sao {} centimetros ou {} milimetros'.format(m,cm,ml))