# Faca um programa que leia a largura e a altura de uma parede em metros 
# e calcule sua area e a quantidade de tinta necessaria, sabendo que cada litro pinta uma area de 2 metros quadrados 
largura = float(input('Qual a largura da sua parede ?  '))
altura = float(input('Qual a altura da sua parede ?  '))

area = largura*altura
tinta = area/2

print(f'Sua parede tem dimensao de {largura} x {altura} e sua área é de {area} metros quadrados')
print(f'E voce precisara de {tinta} litros de tinta')


