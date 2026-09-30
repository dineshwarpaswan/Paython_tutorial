print("\nPolymorphism : ak operator(+) ak hi chije ke alag-alag role defined hai bellow isko Polymorphism ya  Operator Overloading kaha jata hai!\n")
class Complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def shodata(self):

		print(f"[{self.a}i + {self.b}j]")

	def __add__(self,com2):
		newA = self.a + com2.a
		newB = self.b + com2.b
		
		return Complex(newA, newB)

	def __sub__(self,com2):
		newA = self.a - com2.a
		newB = self.b - com2.b
		return Complex(newA, newB)

	def __mul__(self,com2):
		newA = self.a * com2.a
		newB = self.b * com2.b
		return Complex(newA, newB)

	def __truediv__(self,com2):
		newA = self.a / com2.a
		newB = self.b / com2.b
		return Complex(newA, newB)

	def __mod__(self,com2):
		newA = self.a % com2.a
		newB = self.b % com2.b
		return Complex(newA, newB)

	def __pow__(self,com2):
		newA = self.a ** com2.a
		newB = self.b ** com2.b
		return Complex(newA, newB)

	
                

com1 = Complex(3,4)
com1.shodata()

com2 = Complex(2,5)
com2.shodata()

com3 = com1 + com2
com3.shodata()

com3 = com1 - com2
com3.shodata()

com3 = com1 * com2
com3.shodata()

com3 = com1 / com2
com3.shodata()

com3 = com1 % com2
com3.shodata()

com3 = com1 ** com2
com3.shodata()

