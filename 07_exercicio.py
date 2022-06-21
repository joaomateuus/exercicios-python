#Faca um programa que calcule a media do trimestre de um anulo
nota1 = 0
nota2 = 0
paralela = 0
operador = 1
while operador != 0:
    print('0-Sair')
    print('1-Calcular media parcial')
    operador = int(input('Digite uma opcao: '))
    if operador == 1:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota:  '))
        if(nota1 < 7 or nota2 < 7 ):
            paralela = float(input('Digite sua nota paraleal:  '))  
            if(paralela > nota1 or nota2):
                print('Parabéns voce passou na paralela')
                if(paralela > nota1):
                    print('A sua primeira nota sera substituida')
                    paralela = nota1
                    print('Sua média é: ', float(nota1+nota2) /2)
                else:
                    print('A sua segunda nota sera substituida')
                    paralela = nota2
                    print('Sua média é: ', float(nota1+nota2) /2)
            else:
                print('Ahh voce n passou na parela')
                print('Sua média parcial é: ', float(nota1+nota2) /2)     
        else:
            print('Sua média parcial é: ', float(nota1+nota2) /2)
    elif operador == 0:
        break
    
    
                       