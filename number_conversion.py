import os
try:
	def binary_to_decimal():
		os.system("cls")
		print("\t\tBINARY TO DECIMAL\n")
		
		kk=0
		fy=["2","3","4","5","6","7","8","9"]
		a0=int(input("t: "))
		while a0>kk:
			k=8
			ff=0
			a=input(">>>")
			
			for s in range(7):
				if(len(a)!=8 or fy[s] in a):
					os.system("pause")
				else:
					pass
			for i in range(8):
				ff+=(int(a[i])*pow(2,k-1))
				k-=1

			print(f"\n>>>{ff}\n")
			
			kk+=1
		os.system("pause")
	
	
	
	def decimal_to_binary():
		os.system("cls")
		print("\t\tDECIMAL TO BINARY\n")
		
		kk=0
		a0=int(input("t: "))
		while a0>kk:
			ff1=""
			yy=int(input(">>>"))
			if(yy>255 or yy<128):
				os.system("pause")
			else:
				ff=[]
				for i in range(8):
					
					if(yy%2==0):
						ff.append(0)
						yy=int(yy/2)
					else:
						ff.append(1)
						yy=int(yy/2)
				
				for i in range(-7,1):
					ff1+=str(ff[-i])


				print(f"\n>>>{ff1}\n")
				
			kk+=1
		os.system("pause")

	select=input("1)Binary to Decimal\n2)Decimal to Binary\n\n>>>")

	if(select=="1"):
		binary_to_decimal()
	elif(select=="2"):
		decimal_to_binary()
	else:
		os.system("pause")
except ValueError:
	os.system("pause")
