
level = ["Suspeito","Cúmplice","Assasino","Inocente"]
print(" Categorias: \n  Suspeito \n  Cúmplice \n  Assasino \n  Inocente")

option = ["sim","não"]
print("\n Marque com: \n  Sim \n  ou \n  Não \n")

perguntas = ["Telefonou para a vitima?","Esteve no local do crime?","Mora perto da vitima?","Devia para a vitima?","Ja trabalhou com a vitima?"]

sim = option[0]
nao = option[1]

cont_sim = 0
cont_nao = 0

                                                                        #for i in range(0,5):
i = 0

while i != nao:  
	i = eval(input("Respostas:"))
	cont_sim += 1
	                                                                    #cont_nao += 1
	
print("Numeros de sim:",cont_sim)
                                                                        #print("Numeros de nao:",cont_nao)

if cont_sim <= 2:
	print("Suspeita")
else:
	if cont_sim > 2 and cont_sim <= 4:
		print("Cúmplice")
	else:
		if cont_sim == 5:
			print("Assasino")
		else:
			if cont_sim <= 1:
				print("Inocente")

#-----------------------------------------------------------------------

#pq1 = eval(input("1ª-Telefonou para a vitima?"))
#pq2 = eval(input("2ª-Esteve no local do crime?"))
#pq3 = eval(input("3ª-Mora perto da vitima?"))
#pq4 = eval(input("4ª-Devia para a vitima?"))
#pq5 = eval(input("5ª-Ja trabalhou com a vitima?"))

#-----------------------------------------------------------------------
#if sim == 1:
#	print("Inocente")
#else:
#	if sim == 2:
#		print("Supeito")
#	else:
#		if sim == 3 or sim == 4:
#			print("Cúmplice")
#		else:
#			if sim == 5:
#				print("Assasino")
#-----------------------------------------------------------------------
