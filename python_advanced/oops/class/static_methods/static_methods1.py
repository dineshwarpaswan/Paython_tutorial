print("\nSTATIC METHODS:- Methods that don't use the self parameter(work a class level.\n")
# <Type 2---- @staticmethod bellow:- used and handel error --->
class Student:
	def __init__(self, name): # constructor
		self.name = name
	
	def topper(self, marks,grad): # medhod 1
		print("\nTOPPER STUDENT!",self.name," AND HIS MARKS:",marks,"GRAD:",grad,"ACHIVED!")
		
	def avrage(self,marks,grad): # medhod 2
		print("\nAVERAGE STUDENT!",self.name," AND HIS MARKS:",marks,"GRAD:",grad,"ACHIVED!\n")
		
	@staticmethod  # <-- error ko hatane keliye used kiya jata hai,
	def faild(name,low_pass): # medhod 3 <-self.name nahi pass hoskta hai, keoki ye static methods hai,kintu appna parameter pass kar sakte hai 
		print(name,":IS A FAILD STUDENT, BECAUSE:",low_pass,"MARKS ACHIVED!")
		
std = Student("Dineshwar Paswan")
std.topper("96%","A++")
std.avrage("65%","B")
std.faild("RAHUL TIWARI","29%") 

std1 = Student("MAHENDERA PANDIT")
std1.topper("86%","A+")
std1.avrage("55%","C")
std1.faild("TUNTUN THAKUR","28%")