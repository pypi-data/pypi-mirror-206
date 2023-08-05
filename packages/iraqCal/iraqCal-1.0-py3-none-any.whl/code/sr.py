def sr():
		num1 = int(input("Enter num1 :"))
		ope = input("Enter ope :")
		num2 = int(input("Enter num2 :"))
		
		d = "is :"
		if(ope=='+'):
			print(d, num1 + num2)
		elif(ope=='-'):
			print(d, num1 - num2)
		elif(ope=='/'):
			print(d, num1 / num2)
		elif(ope=='%'):
			print(d, num1 % num2)
			
		if(True):
			start()