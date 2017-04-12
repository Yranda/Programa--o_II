#from random import randrange

#lista = []
#time = 0

#while time < 50:
#	n = str(randrange(1, 7, 1))
#	lista.append(n)
#	time += 1
	
#print(lista) 
#print(len(lista))

#-----------------------------------------------------------------------	

perguntas = ["1ª-Telefonou para a vitima?","2ª-Esteve no local do crime?","3ª-Mora perto da vitima?","4ª-Devia para a vitima?","5ª-Ja trabalhou com a vitima?"]
print(perguntas)

option = ["1-sim","2-não\n"]
sim = 0
nao = 0
print(option)

respostas = []
print(respostas)

for n in range(0,5):
	if respostas == sim:
		sim += 1
	elif respostas == nao:
		nao += 1
#-----------------------------------------------------------------------	
#if sim == 2:	
#	print("Supeita")
#else:
#	if sim >= 3 and sim <= 4:
#		print("Cúmplice")
#	else:
#		if sim == 5:
#			print("Assasino")
#		else:
#			if sim < 2:
#				print("Inocente")
#print(respostas)
