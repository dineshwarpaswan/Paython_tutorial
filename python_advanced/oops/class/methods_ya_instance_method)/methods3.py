print("\nMethod: are function that belong to objects.\n")
# TYPE 4 Lest Practice
class Student:

	print("\nHELLO MY DEAR STUDENTS!") # ager methods ke ya constructor ke inside print karayenge, to bar bar call hoga, isliye hamko reapet nahi chahi,
	
	def __init__(self, name, marks ,grad): # constructor
		self.name = name
		self.marks = marks
		self.grad = grad
		
	def topper_marks(self): # methods 1
		print("\nTopper Student Marks:",self.marks,"% and His name:" ,self.name,"and GRAD:",self.grad)
	
	def get_marks(self): # methods 2
		return self.name,self.marks, self.grad # get method used for outside print
		
		#print("\nAgverage Student Marks:", self.marks,"% and His name:",self.name,"GRAD:",grad)
		
# -------one object to calls lodes of methods------		
std = Student("Dinesh paswan", 90, "A++") # instance class
std.topper_marks() # object methods
print(std.get_marks())

std = Student("Rahul kumar", 96, "A++") # instance class
std.topper_marks() # object methods
print(std.get_marks())

std1 = Student("Karan Singh", 98, "A++") # instance class
std1.topper_marks()
print(std1.get_marks())	
	