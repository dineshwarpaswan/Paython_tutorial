print("Multi Level Inheritance:- one chield to another chield Inherita!\n")

# Syntax:
#  class A:
#    ------
#  class B(A):
#    -----
#   class C(B):
#		-----
class Car:
	"""docstring for ClassName"""
	def __init__(self, name, color,sit,price):

		self.name = name
		self.color = color
		self.sit = sit
		self.price = price

		print(f"\nMy feverate: [{self.name}] Car and: [{self.color}] color is beutifull and Price: [{self.price}] Lakh")
	@staticmethod
	def Start():
		print("\nThe Car is Starte!")
	@staticmethod
	def Stop():print("\nThe Car Chas been Stoped!")
class Suzuki(Car):
	"""docstring for Suzuki"""
	def __init__(self,name, color,sit,price,milage):
		super(Suzuki, self).__init__(name, color, sit, price)
		self.milage = milage

		print(f"\nThe name of car [{self.name}] and Price:[{self.price}Lakh] Milage of Car: [{self.milage}]1 hourse")

class TharCar(Suzuki):
	"""docstring for ClassName"""
	def __init__(self, name, color, sit, price, milage, mode):
		super(TharCar, self).__init__(name, color, sit, price, milage)
		self.mode = mode

		print(f"\nMode OF Car: [{self.mode}] Price :[Rs.{self.price} Lakh] Milage: [{self.milage}]1 House and Total Sit: [{self.sit}] Color is : [{self.color}] Beautifull and name of Car: [{self.name}]")

thar = TharCar("Anova", "White", 6, 35, 45, "Electricity")
thar.Start()
thar.Stop()

print(f"\nExrnal Result Here:- [{thar.name} car],[Color: {thar.color}],[Total: {thar.sit} sit],[Price: {thar.price}Lakh],[{thar.milage} 1 hourse],[{thar.mode}]")

thar1 = TharCar("TOYOTA", "BLUE", 8, 45, 40, "PETROL")
print(f"\nExrnal Result Here:- [{thar1.name} car],[Color: {thar1.color}],[Total: {thar1.sit} sit],[Price: {thar1.price}Lakh],[{thar1.milage} 1 hourse],[{thar1.mode}]")
thar1.Start()
thar1.Stop()
		
