def grade_name(x,y):
	name = x
	grade = y
	print("Nome do aluno:",x.lower(),"Nota:",y)
	#print("Nota:",y)

n=""	
#name = eval(input("digite o nome do aluno:"))
grade = eval(input("digite a nota do aluno:"))

if grade >= 7:
	#print(name)
	print(grade_name,"APROVADO")
else:
	if grade < 7:
		#print(name)
		print(grade_name,"REPROVADO")
	

	
	


