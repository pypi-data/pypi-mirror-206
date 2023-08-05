from sr import *
def cul():
	def start():
		
		c = input("exit[e] | start[s] :")
		if(c.lower()== 'e'):
			exit()
		elif(c.lower()== 's'):
			sr()
		else:
			print(f"Error:{c} is Not Found!")
	start()
