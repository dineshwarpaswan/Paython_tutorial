print("\nSTATIC METHODS:- Methods that don't use the self parameter(work a class level.\n")
# Bellow Syntax:
#	class Student:
#		@staticmethod  <-- Decorator:  
#	def hello():
#		print("This is my project static method")
#std = Student()
#print(std)

print("\nDecorator:- Decorator allow us to wrap another function in oder to extend the behaviour of the wrapped function, without permannentaly modifying\n")
# ----Type 1----------------

class Person:
	@staticmethod  # decorator used for the error solving 
	def hello():
		print("Type 1, This is my Project static method(@staticmethod):- used for solve error")
		
per = Person()
per.hello() 
