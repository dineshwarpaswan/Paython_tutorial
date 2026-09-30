print("\nMethod: are function that belong to objects.\n")
# TYPE 4
class Student:

	print("\nHELLO MY DEAR STUDENTS!") # ager methods ke ya constructor ke inside print karayenge, to bar bar call hoga, isliye hamko reapet nahi chahi,
	
	def __init__(self, name, marks): # constructor
		self.name = name
		self.marks = marks
		
	def toper(self,grad): # methods 1
		print("\nTopper Student Marks:",self.marks,"% and His name:" ,self.name,"GRAD:",grad)
	
	def agverage(self,grad): # methods 2
		print("\nAgverage Student Marks:", self.marks,"% and His name:",self.name,"GRAD:",grad)
		
# -------one object to calls lodes of methods------		
std = Student("Dinesh", 90) # instance class
std.toper("A++") # object methods

std = Student("Mahesh", 55) # instance class
std.agverage("D") # object methods

std = Student("Ramesh", 60) # instance class
std.agverage("C") # object methods 

std = Student("Neha", 95) # instance class
std.toper("A++") # object methods
		