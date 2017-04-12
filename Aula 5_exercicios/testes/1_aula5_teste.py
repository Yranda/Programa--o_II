
alunos = []
lista_alturas = []
lista_idades = []

alturas = 0
media_alt = 0
cont_alunos = 0
cont_idades = 0

#for i in range(0,2):
	#alunos.append(input("Nome dos alunos:"))
	#print(alunos)
	
i = 0
	
while i <= 12:
	idades = eval(input("Digite as idades:"))
	lista_idades.append(idades)
	print("Idades digitadas:",lista_idades)
	alturas = eval(input("Digite as alturas:"))
	lista_alturas.append(alturas)
	alturas += 1
	alt_contadas = (alturas - 1)
	print("Alturas contadas:",alt_contadas) 
	print("altura dos alunos:",alturas)
	media_alt = alturas / 2
	print("media das alturas dos alunos:",media_alt)
	cont_idades += 1
	if idades >= 14 and alturas <= media_alt :
		cont_alunos += 1
		print("Alunos maior ou igual a 14 anos com altura inferior a media:",cont_alunos)
	

		
	
	
