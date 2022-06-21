# Crie um programa que leia algo no teclado e mostre na tela 
# seu tipo primitivo e retorne todos os dados sobre ele

input_primitivo = input('Digite algo:  ')

print('O tipo primitivo desse valor é: ', type(input_primitivo))
print('Só tem espacos ?', input_primitivo.isspace)
print('É um número', input_primitivo.isnumeric)
print('É alfabetico', input_primitivo.isalpha)
print('É alfanumerico', input_primitivo.isalnum)
#Checa tudo maiusculo
print('Esta em letras maiusculas ?', input_primitivo.isupper)
#Checa tudo minusculo
print('Esta em letras minusculas ?', input_primitivo.islower)
#Checa primeira letra minuscula
print('Está capitalizada ?', input_primitivo.istitle)
