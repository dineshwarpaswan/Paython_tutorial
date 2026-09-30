print("class method:-A class method is bound to the class & receives the class as an implicit first argument.  NOTE- static method can't access or modify class state & generally for utility.\n")
# Syntax here:-bellow

#    class Student:    
#		@classmethod     <--#decorator
#		def college(class):
#				pass
class Person:
	name = "DINESHAR PASWAN"

	@classmethod     # <--decorator
	def changeName(clas, name):
		clas.name = name

p = Person()

print(Person.name)

p.changeName("RAKESH PARSAD")

print(f"DINESHAR PASWAN will be Change :[{p.name}]")

print(Person.name)	
		
