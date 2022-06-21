# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
operador = 1

while operador !=0:
    print('1-Calcular média do aluno')
    operador = int(input('Digite a opcao que deseja:  '))
    if operador == 1:
        n1 = float(input('Digite sua primeira nota:  '))
        n2 = float(input('Digite sua segunda nota:  '))

        media = (n1+n2)/2

        print(f'Sua média é: {media}')
        break
