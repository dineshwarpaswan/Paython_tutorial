print("\nPython Single Inheritance:- inheritance feature that allows us to create a class that inherits the attributes(or properties) and methods of another class\n")
# type 2
# Syntex:
#   class A: 	<-- Super class/Paraint class
#		....
#
#   class B(A):   Base class/childe class <--Used properties and methods of Super class

class Employee: #pairent class
	def __init__(self, emp_id, name, degnition, sallary): # costructor ya initilise
		self.emp_id = emp_id
		self.name = name
		self.degnition = degnition
		self.sallary = sallary
		
	def Government(self): # method
		print("\nEmplopee id: " + self.emp_id + " Degination: " + self.degnition + " How get sallary: " + self.sallary + " Your name:" + self.name)
		
class Private(Employee): #sub class
	def __init__(self, emp_id, name, degnition, sallary):
		super().__init__(emp_id, name, degnition, sallary) # pairant class
	def Private_employee(self):
		print("\nYou are:" + self.degnition +" Sale Tv " + " Get Sallary: " + self.sallary)
		

emp = Private("001", "Dineshwar", "Engineer","95000") # instance class
emp.Government() #  method of instance object

emp1= Private("003", "Sudhir", "Doctor", "150000") # instance class
emp1.Government()

emp2= Private("002", "Kirishana", "Salles Manager","85000") # instance class 
emp2.Private_employee()

emp3= Private("004", "Ravinder", "Associate Manager","85000") # instance class
emp3.Private_employee()