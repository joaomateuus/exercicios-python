#Faca um programa que sorteie uma ordem para os alunos apresentarem o trabalho
import random

nome1 = input('Digite o nome do primeiro aluno:  ')
nome2 = input('Digite o nome do segundo aluno:  ')
nome3 = input('Digite o nome do terceiro aluno:  ')
nome4 = input('Digite o nome do quarto aluno:  ')

alunos = [nome1, nome2, nome3, nome4]

random.shuffle(alunos)

print(f'Os participantes terao que apresentar nessa ordem {alunos}')

