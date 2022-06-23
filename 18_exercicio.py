import math

angulo = float(input('Digite o angulo que deseja calcular:  '))

seno =  math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O angulo informado foi {angulo}, o seno é {seno:.2f} o coseno é {coseno:.2f} e a tangente é {tangente:.2f}')
