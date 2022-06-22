#Escreva um programa que pergunta a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que 
# o carro custa R$60 por dia e R$0.15 km rodado

dias = int(input('Quantos dias o carro foi alugado ?  ')) 
km = float(input('Quantos km foram rodados ?  '))

total_pagar = (dias*60) + (km*0.15)

print(f'O valor a ser pago pelo uso do carro por {dias} dias e {km:.2f} km rodados é: {total_pagar:.2f}  ')

