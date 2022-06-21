#Desenvolva um programa que receba um valor e retorne quanto a pessoa pode comprar com esse valor em dolar e euro

dinheiro = float(input('Digite quanto vc tem em reais  : R$'))

valor_dolar = dinheiro/5.12
valor_euro = dinheiro/5.41

print('Na cotacao atual de 21-06-2022')
print(f'Voce consegue comprar com {dinheiro}R$, {valor_dolar:.2f} dolares e {valor_euro:.2f} euros.')