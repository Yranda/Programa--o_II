def media(primeiro, *outros):
 return (primeiro + sum(outros)) / (1 + len(outros))
 
# Exemplos de uso  
print(media(1, 2))
print(media(1, 2, 3, 4))

