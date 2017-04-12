lista=["a","b","c","d","e",1]
print(lista[1:3])
print(lista[:4])
print(lista[2:])
print(lista[:])

lista=[[10,20],[100,200]]
print("Valor 0,0 "+str(lista[0][0]))
print("Valor 0,1 "+str(lista[0][1]))
print("Valor 1,0 "+str(lista[1][0]))
print("Valor 1,1 "+str(lista[1][1]))

lista=[[1,2,3],[4,5,6],[7,8,9]]
print(lista[0][2])

lista=[None]*10
x=0
for x in range(0,4):
	lista[x]="teste"+str(x)
print(lista)
