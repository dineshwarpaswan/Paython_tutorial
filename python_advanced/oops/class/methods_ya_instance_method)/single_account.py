print("\n --------------- SNGLE USEER ACCOUNT JENRATE FOR BANKING SYSETM!----------------\n")

class Account:  # class name 

	def __init__(self, holder, balance, account): # constructor
		self.holder = holder
		self.balance = balance
		self.account = account
		
	def debit(self, amount): # method 1
		self.balance -= amount
		print("\n",self.holder,"Rs.",amount," Your account has debite Succefully! AND Main Balance:Rs.",self.get_balance()," Thanku you!")
		
	def credit(self, amount):	# method 2
		self.balance += amount
		print("\n",self.holder,"Rs.",amount,"Your account has Creadite Succefully! AND Main Balance:Rs.",self.get_balance()," Thanku you!")
		
	def get_balance(self): # method 3
		return self.balance
		
sing = Account("DINESHWAR",15000, 87654955661)	#instance class	 
# -------one object to calls loudes of methods------		
print("\nThe Main Balance:Rs.",sing.balance,"Account Holder:",sing.holder," AND Account Number:",sing.account," Thanku you!") #object attributes
sing.debit(500) 	# object medhod
sing.credit(1500)  # object medhod
#print("\nMain Balance:Rs.",sing.get_balance()," Thanku you!") # outside print object medhod
sing.debit(3000)
sing.credit(8000)

#print("\nMain Balance:Rs.",sing.get_balance()," Thanku you!")
st1 = Account("MANISHA",25000, 23654955502)
print("\nThe Main Balance:Rs.",st1.balance,"Account Holder:",st1.holder," AND Account Number:",st1.account," Thanku you!") #object attributes
st1.debit(4500)
st1.credit(8000)
