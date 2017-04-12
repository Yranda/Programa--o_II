import math

r = eval(input('Digite o valor do raio: '))

area = math.pi * r**2
print('O valor arredondado da área é ', round(area, 2))
print('O valor não arredondado da área é ', area)

