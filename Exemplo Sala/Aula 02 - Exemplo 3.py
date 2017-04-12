def recebe(tamanhomax, *, bloco):
	print(tamanhomax)
#recebe(1024, True)	     #TypeError - ERRADO
recebe(1024, bloco=True) #OK - CORRETO
print(recebe.__doc__)
