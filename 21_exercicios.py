nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome maiusculo é: ', nome.upper())
print('Seu nome minusculo é: ', nome.lower())
print('Seu nome tem o total de {} letras'.format(len(nome)-nome.count(' ')))



