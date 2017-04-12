
palavra = eval(input("Digite a palavra:"))

vogais = [a,e,i,o,u]
letras = []
i = 1
while i <= 8:
	letras.append(input("Letra: "))
	i += 1
i = 0
cont = 0
while i <=9:
	if letras[i] in "aeiou":
		cont += 1
	i += 1
print("foram lidos %d vogais" %cont)
	
#-----------------------------------------------------------------------
#i = 1
#if len(palavra) == 8:
#	print("Possui",vogais in palavra"vogais nesta palavra")
	#n = int(input("digite um numero: "))
	#vetor.append(n)
	#i = i + 1
#print("Vetor lido:", vetor)

#for vogais in palavra:
#	if len(palavra) == 8:
#		print(palavra)
		
		
#if len(palavra) == 8:
#	for vogais in palavra:
#		print(palavra)
