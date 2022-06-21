medida = float(input('Digite uma distancia em metros:  '))

print(f'A medida de {medida}m corresponde a:  ')

kilometros = medida/1000
hectometros = medida/100
decametros = medida/10
decimetros = medida*10
cemtrimetros = medida*100
milimetros = medida*1000



print(f'{kilometros}km')
print(f'{hectometros}hm')
print(f'{decametros}dam')
print(f'{decimetros}dm')
print(f'{cemtrimetros}cm')
print(f'{milimetros}mm')