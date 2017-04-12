#RECEBE O VALOR
x=input('Digite o numero ')
#FUNCAO ACHA O ULTIMO E MOSTRA
def mostra_val(num1):
	print(num1[len(num1)-1])
	print(len(num1))
#CHAMA A FUNCAO
mostra_val(x)
