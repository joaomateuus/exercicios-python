#Faca um programa q receba um salario e o retorne com o reajuste salarial de 15%

salario_atual = float(input('Qual o salario do funcionario ?  '))

salario_ajustado = salario_atual + (salario_atual*15/100)

print(f'O salario do funcionario era {salario_atual:.2f}, e após ao reajuste de 15% passou a ser {salario_ajustado:.2f}')