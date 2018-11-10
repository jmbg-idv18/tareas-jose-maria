def fact(num,res):
	if num==1:
		print(res)
	else:
		res*=num
		num-=1
		fact(num,res)
num=int(input("introducir nùmero"))
x=1
res=1
fact(num,res)
