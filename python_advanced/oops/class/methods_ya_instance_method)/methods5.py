print("\nMethod: are function that belong to objects.\n")
# TYPE 6 Lest Practice
class Student:

	print("\nHELLO MY DEAR STUDENTS!") # ager methods ke ya constructor ke inside print karayenge, to bar bar call hoga, isliye hamko reapet nahi chahi,
	
	def __init__(self, name, marks ,grad): # constructor
		self.name = name
		self.marks = marks
		self.grad = grad
		
	def topper_marks(self): # methods 1
		print("\nTopper Student Marks:",self.marks,"% and His name:" ,self.name)
	
	def get_avg(self): # methods 2
		sum = 0
		for value in self.marks:
			sum += value
		print("\nAgverage of Student Marks: ", sum/5 ," % and His name:", self.name,"GRAD:",self.grad)
			
		
# -------one object to calls loudes of methods------		
std = Student("Dineshwar paswan",[90, 75, 76, 98, 95],"A+") # instance class
std.topper_marks() # object methods
std.get_avg()
	
std1 = Student("Diwansu Gupta",{90, 94, 98, 95, 96},"A++") # instance class
std1.topper_marks() # object methods
std1.get_avg()

	