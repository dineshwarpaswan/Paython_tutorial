print("\nClass Attributes:- A class can have Attributes.\n")
print("For example: The Student class can have attributes like;- id_number, name ,titale, age.\n")

class Student:  # class name
	def __init__(self, id_number, name , titale, age): # constructor ya initialise
		self.id_number =id_number  # attributes
		self.name = name		   # attributes
		self.titale = titale	   # attributes
		self.age = age			   # attributes

object = Student("001", "Dineshwar", "paswan", "35")  # <--instantiating a class 

a = object.id_number # instantiat object
b = object.name		# instantiat object
c = object.titale
d = object.age
# access its properties
print("Student Id:", a)
print("Student Name:", b)
print("Student Titale:", c)
print("nStudent Age:", d)
 
 # access its all properties
print("\nPrint in list:",[a,b,c,d]) # print will be in :list 
b = object.name	= "Rajesh"  	# replace will be : name
c = object.titale = "Parasad" 	# replace will be :titale
print("Print in list:",[a,b,c,d]) # print will be in :list