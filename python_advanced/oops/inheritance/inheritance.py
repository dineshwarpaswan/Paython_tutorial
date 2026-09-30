print("\nPython Inheritance:- inheritance feature that allows us to create a class that inherits the attributes(or properties) and methods of another class. When one class(child/derived) derives the properties & method class(parent/base).\n")
# type 1
# Syntex:
#   class A: 	<-- Super class/Paraint class
#		....
#
#   class B(A):   Base class/childe class <--Used properties and methods of Super class
#       .....


class Employee:
	def __init__(self, emp_id, name, degnition, sallary): # initialise
		self.emp_id = emp_id
		self.name = name
		self.degnition = degnition
		self.sallary = sallary
		
	def manager(self): # method
		print("\nEmplopee_id:" + self.emp_id + " Your Degination: " + self.degnition + " How get sallary: " + self.sallary + " and Your name:" + self.name)
		

emp = Employee("001", "Dineshwar", "Engineer","95000") # instance class 
emp.manager() #  instance object

emp1= Employee("002", "Kirishana", "Manager","85000") # instance class 
emp1.manager() # instance object

emp2= Employee("003", "Sudhir", "Doctor", "150000") # instance class 
emp2.manager() # instance object