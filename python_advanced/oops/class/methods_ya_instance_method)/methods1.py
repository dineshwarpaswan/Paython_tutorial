print("\nMethod: are function that belong to objects.\n")
# TYPE 3
class Student:
	
	print("\nHello my dear Students!") # ager methods ke ya constructor ke inside print karayenge, to bar bar call hoga, isliye hamko reapet nahi chahi, 
	
	def __init__(self, name, marks): # constructor
		self.name = name
		self.marks = marks
		
	def toper(self): # methods
		print("\nTopper Student Marks:" , self.marks)
		print("\nTopper Student Marks: ", self.marks, " % and name:" ,self.name)
		
		
std = Student("Dinesh", 90) # instance class
std.toper() # methods object

std1 = Student("Papu Parsad", 80) # instance class
std1.toper() # methods object

		