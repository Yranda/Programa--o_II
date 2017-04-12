def f(nome,saudacao="Oi",pontuacao="!!"): 
	return saudacao+","+nome+pontuacao 
print (f("Joao")) 
#Oi,Joao!! 
print (f("Joao","Parabens")) 
#Parabens,Joao!! 
print(f("Joao","Ah","...")) 
#Ah,Joao...
