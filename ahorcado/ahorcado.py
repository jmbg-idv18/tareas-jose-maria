import random
x=0
intentos=4
with open("sowpods.txt","r") as file:
	for line in file:
		x+=1
	n=random.randint(1,x)

with open("sowpods.txt","r") as file:
	m=0
	for line in file:
		m+=1
		if (m==n):
			listword=list(line)
			word=line
listword.remove("\n")

print(word)
print("adivina la palabra, tienes ",intentos," oportunidades de fallar ")
guess=[]

for x in listword:
	guess.append("_")

perder=False
while guess!=listword:
	if intentos>0:
		encontrado=0
		puntos=0
		y=0
		intentos=str(intentos)
		print(guess)
		letra=str(input("introduce una letra de la palabra, errores restantes: "+intentos))
		intentos=int(intentos)
		for x in listword:
			if listword[y]==letra.upper():
				guess[y]=letra.upper()
				encontrado+=1
			if listword[y]==letra.lower():
				guess[y]=letra.lower()
				encontrado+=1
			y+=1	

		if encontrado==0:
			intentos-=1
	else:
		print("perdiste, la palabra es ",str(word))
		guess=listword
		perder=True
if perder==False:
	print("ganste, la palabra es ",str(word))
		
	
