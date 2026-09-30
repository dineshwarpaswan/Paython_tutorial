print("\nPrivate(Like) Attributes & MethodS:- are meant to used only within the class and are not accessible form outside the class.")
# Synatax:

print(" __name = name <--double underscore is private(lagane se banjata hai private, ab isko class ke bahar print nahi karasakte hai\n") 

#  self.__acc_number = acc_number   <--double underscore is private(private ko class ke outeside nahi call kar sakte hai error de dega)
#  self.__acc_password = acc_password   <--double underscore laga ke private banaya ja sakta hai

class Account: # <---className
	
	def __init__(self, holder,acc_number , acc_password,bank): # < constructor with argumants

		self.holder = holder
		self.__acc_number = acc_number
		self.__acc_password = acc_password
		self.bank = bank

	def Holder(self):
		print(f"Holder  name: [{self.holder}], Bank name: [{self.bank}], ACCOUNT Number: [{self.__acc_number}], AND PASSWORD HERE: [{self.__acc_password}]\n") # <--internally private will be run

		

acc = Account("DINESHWAR PASWAN",23564780,"D045@682338AC","SBI")

print(f"acc Holder name:[{acc.holder}] And BANK name: [{acc.bank}]") # access iner and out side class

acc1 = Account("SAMIR SECSENA",135649801,"S045$682338D0C","ICICI")

print(f"\nacc1 Holder name: [{acc1.holder}] BANK: [{acc1.bank}]\n")# access iner and out side class
print("--------******* UPER OUT SIDE CLASS RESULT ********* and Bellow Inside class Result-------\n")

acc.Holder()# <--ye method class ke inside run karega
acc1.Holder()# <--ye method class ke inside run karega

print(f"object 1 method :[{acc.Holder()}], object 2 method : [{acc1.Holder()}]") # accesseble outsite of class  with method

print(f"ACCOUNT Number: [{acc.__acc_number}], AND PASSWORD HERE: [{acc1.__acc_password}]") # error dega<-- private attributes outside of class not run 


