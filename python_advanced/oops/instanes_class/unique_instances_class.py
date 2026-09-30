print("\nInstances are Unique: Lest say you have 500 students, and you need to manage their data. instead of doing that,you can just create unique instances of a class.\n")

class Student:
	def __init__(self, id_number, name , titale, age):
		self.id_number = id_number
		self.name = name
		self.titale = titale
		self.age = age

object = Student("001", "Dineshwar", "Paswan", "35")  #<--instantiating class 1
object1 = Student("002", "Dinesh", "Ram", "40") #<--instantiating class 2
object2 = Student("003", "Deepak", "Sarma", "50") #<--instantiating class 3


print("Student Id:", object.id_number) # Unique instances(object)
print("Student Name:", object.name)
print("Student Titale:", object.titale)
print("Student Age:", object.age)
print("------------------")
print("Student Id:", object1.id_number) # Unique instances(object)
print("Student Name:", object1.name)
print("Student Titale:", object1.titale)
print("Student Age:", object1.age)
print("------------------")
print("Student Id:", object2.id_number) # Unique instances(object)
print("Student Name:", object2.name)
print("Student Titale:", object2.titale)
print("Student Age:", object2.age)
