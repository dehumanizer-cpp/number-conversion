
def binary_to_decimal():
	k=8
	ff=0

	a=input()


	for i in range(8):
		
		ff+=(int(a[i])*pow(2,k-1))
		k-=1

	print(ff)

def decimal_to_binary():
	ff=[]


	yy=int(input())

	for i in range(8):
		
		if(yy%2==0):
			ff.append(0)
			yy=int(yy/2)
		else:
			ff.append(1)
			yy=int(yy/2)
	ff1=""
	for i in range(-7,1):
		ff1+=str(ff[-i])


	print(ff1)


select=input("1)Binary to Decimal\n2)Decimal to Binary\n\n>>>")

if(select=="1"):
	binary_to_decimal()
elif(select=="2"):
	decimal_to_binary()
else:
	exit()


