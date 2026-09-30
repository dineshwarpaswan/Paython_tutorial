print("\nPrivate(Like) Attributes & MethodS:- are meant to used only within the class and are not accessible form outside the class.")

# Synatax:

print(" __name = name <--double underscore is private(lagane se banjata hai ab isko class ke bahar print nahi karasakte hai\n") 

#  self.__acc_number = acc_number   <--double underscore is private(private ko class ke outeside nahi call kar sakte hai error de dega)
#  self.__acc_password = acc_password   <--double underscore laga ke private banaya ja sakta hai

class Account: # <---className
	
	def __init__(self, holder,acc_number , acc_password,bank): # < constructor with argumants
		self.holder = holder
		self.acc_number = acc_number
		self.acc_password = acc_password
		self.bank = bank

acc = Account("DINESHWAR PASWAN",23564780,"D045@682338AC","SBI")

print(f"Holder name:[{acc.holder}] Account: [{acc.acc_number}]Paswaord :[{acc.acc_password}] BANK: [{acc.bank}]")

acc1 = Account("SAMIR SECSENA",135649801,"S045$682338D0C","ICICI")
print(f"Holder name: [{acc1.holder}] Account : [{acc1.acc_number}] Paswaord : [{acc1.acc_password}] BANK: [{acc1.bank}]")

acc2 = Account("SEMEERAN AKHTON",1356749071,"SA045$682338D0C","BHANDHAN BANK")
print(f"Holder name: [{acc2.holder}] Account : [{acc2.acc_number}] Paswaord : [{acc2.acc_password}] BANK: [{acc2.bank}]")

print("\n-----------------------------------------------------------------\n")


class Account1:
	"""docstring for ClassName"""
	def __init__(self, holder,acc_number , acc_password,bank):
                
		self.holder = holder
		self.__acc_number = acc_number  # <private:--double underscore lagane se private ban gya, ab ye class ke bahar access nahi kar sake hai
		self.__acc_password = acc_password # <--double underscore is a private
		self.bank = bank

acc = Account1("MAMATA PASWAN",245564780,"M045@6823381C","KENA BANK")

print(f"HOLDER NAME:[{acc.holder}] and BANK NAME: [{acc.bank}]\n")
print(f"ACCOUNT NUMBER:[{__acc_number}] PASSWAORD:[{__acc_password}]\n") # Not Access private attributes  Out side the class

