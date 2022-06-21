#Faca um programa que calcule a media do trimestre de um anulo
operador = 1
while operador != 0:
    print('0-Sair')
    print('1-Calcular media parcial')
    operador = int(input('Digite uma opcao: '))
    if operador == 1:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota:  '))
        if(nota1 > nota2):
            menor_nota = nota2
        else:
            menor_nota = nota1
        if(nota1 < 7 or nota2 < 7 ):
            paralela = float(input('Digite sua nota paraleal:  '))  
            if(paralela > menor_nota ):
                print('Voce recuperou sua menor nota com a parelala')
                if(menor_nota == nota1):
                    nota1 = paralela
                    print('A sua primeira nota sera substituida')
                    print('E sua média parcial é: ', float(nota1+nota2) /2)
                else:
                    nota2 = paralela
                    print('A sua segunda nota sera substituida')
                    print('E sua média parcial é: ', float(nota1+nota2) /2)
            else:
                print('Voce nao passou na parela e suas notas nao serao subsituidas')
                print('Sua média parcial é: ', float(nota1+nota2) /2)  
        else:
            print('Sua média parcial é: ', float(nota1+nota2) /2)
    elif operador == 0:
        break
    
    
                       