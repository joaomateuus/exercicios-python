#Desenvolva um programa que leia os catetos de um triangulo e retorne o calculo da hipotenusa

cateto_adjacente = float(input('Digite o valor do cateto adjacente:  '))
cateto_oposto = float(input('Digite o cateto oposto:  '))

hipotenusa = (cateto_adjacente**2 + cateto_oposto**2)**(1/2)

print(f'A hipotenusa vai medir é: {hipotenusa:.2f}')