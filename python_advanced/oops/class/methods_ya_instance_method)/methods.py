print("\nMethods: Methods are function that can access the class attributes. These methods should be defined(created) inside the class.\n")
# TYPE 1
class Student:
	def __init__(self, id_number, name , titale, age):  # constructor
		self.id_number = id_number
		self.name = name
		self.titale = titale
		self.age = age
	def great_student(self): # method
		print("Hello: " + self.name + " How are you?" + " I am fine and My age: " + self.age)
		

object = Student("001", "Dineshwar", "Paswan", "35") # instance class
object.great_student() # object method

object1 = Student("002", "Bharat", "Parsad", "40") # instance class
object1.great_student() # object method

object2 = Student("003", "Rahul", "kumar", "50") # instance class
object2.great_student() # object method

object3 = Student("004", "Mohit", "Sinha", "60") # instance class
object3.great_student() # # object method 

print("------------------------------")

# type 2
class Employee:
	def __init__(self, emp_id, name , titale, degnition, sallary, age):
		self.emp_id = emp_id
		self.name = name
		self.titale = titale
		self.degnition = degnition
		self.sallary = sallary
		self.age = age
	def great_employee(self,city): # method
		print("\nemp id: " + self.emp_id + " Hello " +self.degnition + " How get sallary?: " + self.sallary + " and Your name:" + self.name + " and your Titale: " + self.titale + " and your age: " + self.age + " city: " + city)
		

emp = Employee("001", "Dineshwar", "Paswan", "Engineer","95000","36") # instance object
emp.great_employee("Bokaro") #  method of instance object

emp1= Employee("002", "Kirishana", "Sectiona", "Manager","85000","30") # instance object
emp1.great_employee("Dhanbad")

emp2= Employee("003", "Sudhir", "Mahatra", "Doctor", "150000", "45") # instance object
emp2.great_employee("Ranchi")