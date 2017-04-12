def checa_tamanho():
	for t in idades:
		if idades[t] > 14:
			if alturas[t] < media:
				cont += 1
		return(cont)

nomes = []
idades = []
alturas = []

cont_z = 0
cont_x = 0
cont_y = 0
soma = 0
w = 0

for z in range(0,2):
	z = input("Digite o nome dos alunos: ")
	nomes.append(z)
	cont_z += 1
	
for x in range(0,2):
	x = eval(input("Digite a idade: "))
	idades.append(x)
	cont_x += 1
	
for y in range(0,2):
	y = int(input("Digite a altura: "))
	alturas.append(y)
	cont_y += 1
	soma += alturas[w]
	
print("Tamanho aluno: ",checa_tamanho()) 
print("Soma das alturas: ",soma)  	
print("Foram digitadas ",cont_z," nomes")
print("Foram digitadas ",cont_x," idades")
print("Foram digitadas ",cont_y," alturas")
print("As idades:",idades,"As alturas:",alturas)

#-----------------------------------------------------------------------

#idades = []
#alturas = []

#soma_alt = 0
#cont_alt = 0
#cont = 0

#for n in range(0,11):
	#alunos.append(input("digite o nome do aluno:"))
	#idades.append(eval(input("digite a idade:")))
	#alturas.append(eval(input("digite a altura:")))
	#if idades >= 14:
		#cont += 1
		#print("media altura:",media_alt)
		#print(cont,"aluno(s) com idade maior que 14 e com altura abaixo da média.")

#media_alt = alturas / 12
#print(media_alt)
#soma_alt = soma_alt + 1
#cont_alt = cont_alt + 1 		
#print(alunos,"Está abaixo da média.")
#print(cont_alt,"Com altura abaixo da média.")


#def checa_tamanho():
	#for n in idades:
		#if idades[n] > 14:
			#if alturas[n] < media:
				#cont += 1
	#return(cont)
			 
		

	
