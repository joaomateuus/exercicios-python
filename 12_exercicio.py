#Crie um programa que receba o valor de um produto e o retorna com o desconto de 20%

valor = float(input('Digite o valor do produto que deseja comprar:  '))

valor_desconto = valor - (valor*5/100)

print(f'O valor do produto era {valor:.2f}, e agora esta por {valor_desconto:.2f} com 5% de desconto')