
notas = []
i = 1

while i <= 5:
	n = float(input('digite um numero:'))
	notas.append(n)
	i  += 1
soma = 0
i = 0
while i <= 4:
	soma += notas[i]
	i += 1
print("Notas:",notas)
print("Média:", (soma/4))

#-----------------------------------------------------------------------	
#soma = 0
#for e in l:
#	soma = soma + e
#media = float(soma)/len(1)
#print(media)

#-----------------------------------------------------------------------
#notas = []
#soma = 0
#x = 0

#while x <= 5:
#	n = int(input("Digite as notas:"))
#	notas.append(n)
#	x = x + 1
	
