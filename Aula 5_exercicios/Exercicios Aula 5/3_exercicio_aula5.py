""" o "i" e o "v", sao valores que vao ser usados de formas diferentes, o  "i" sera o numero usado para comparar com o 
valor dado na pergunta abaixo do while, ja o "v" estava sendo usado tanto para fazer a comparaçao quanto para ser 
adicionado na lista, agora ele sera usado apenas para adicionar a lista o valor dado pelo numero"""

lista = []
i = 0
v = 0
soma = 0

while v != -1:
	v = eval(input("Digite as notas:"))
	lista.append(v)
	i = i + 1
	soma += v
	media = soma / i

if v > media:
	print("Valores maiores que a media:",v)
else:														            # contador que equivale a i += 1
	if v < 7:
		print("Valores menores que 7:",v)
print("A media da soma:",media)
print("A soma dos valores:",soma)
print("Quantidades digitadas:",i)
print("Lista:",lista)
print("O programa sera encerrado")
