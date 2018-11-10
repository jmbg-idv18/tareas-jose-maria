

def mult(base:int,factor:int,x:int,prod:int):
	if(x>=factor):
		print(prod)
	else:
		prod+=base
		x+=1
		mult(base,factor,x,prod) 

base=int(input("nùmero a multiplicar"))
factor=int(input("veces a multiplicar"))
prod=base
x=1
mult(base,factor,x,prod)