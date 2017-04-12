lista = []
i = 1
soma = 0
mult = 1

while i <= 6:
	n = int(input("Digite um numero:"))
	lista.append(n)
	i = i + 1
	mult = mult * n
	soma += n
	
print(lista)
print(soma)
print(mult)

#-----------------------------------------------------------------------

#soma += n # mesma coisa que soma = soma + 1
