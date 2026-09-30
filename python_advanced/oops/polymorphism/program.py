print("\nPolymorphism : ak operator(+) ak hi chije ke alag-alag role defined hai bellow isko Polymorphism ya  Operator Overloading kaha jata hai!\n")
class Complex:
	def __init__(self, real, imaj):
		self.real = real
		self.imaj = imaj

	def shodata(self):

		print(f"[{self.real}i + {self.imaj}j]")

	def __add__(self,com2):
		newReal = self.real + com2.real
		newImaj = self.imaj + com2.imaj
		return Complex(newReal, newImaj)

	def __sub__(self,com2):
		newReal = self.real - com2.real
		newImaj = self.imaj - com2.imaj
		return Complex(newReal, newImaj)

	def __mul__(self,com2):
		newReal = self.real * com2.real
		newImaj = self.imaj * com2.imaj
		return Complex(newReal, newImaj)

	def __truediv__(self,com2):
		newReal = self.real / com2.real
		newImaj = self.imaj / com2.imaj
		return Complex(newReal, newImaj)

	def __mod__(self,com2):
		newReal = self.real % com2.real
		newImaj = self.imaj % com2.imaj
		return Complex(newReal, newImaj)
                

com1 = Complex(1,3)
com1.shodata()

com2 = Complex(3,6)
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
