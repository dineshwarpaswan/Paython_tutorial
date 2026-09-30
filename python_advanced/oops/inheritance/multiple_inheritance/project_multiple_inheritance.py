print("\nPython Multiple Inheritance with Project\n")
#   class A: 	<-- Super class/Paraint class
#		....
#
#   class B:    class/Super childe class 1 <--Used properties and methods of Super class
#     ......
#   class C(A,B):   Base/Childe class  <--Used properties and methods of Super class
#      ------

class Computer:
	def __init__(self,brand, ram, processor):

		self.brand = brand
		self.ram = ram
		self.processor = processor

	def get_computerDtails(self):

		return f"Brand name: [{self.brand}] Computer Ram: [{self.ram}GB] and Processor: [{self.processor}]"
			
class Desktop:
	def __init__(self, hard_dic):

		self.hard_dic = hard_dic
	
	def get__Desktop_Infor(self):

		return f"Brand name: [{self.brand}] Desktop Hard dic:[{self.hard_dic}GB]"	

class Laptop(Computer, Desktop):
	def __init__(self,brand, ram,processor, hard_dic, power_bacup):

		# dono paraint class __init__ ko call karna hai
		Computer.__init__(self,brand, ram,processor)
		Desktop.__init__(self, hard_dic)

		self.power_bacup = power_bacup
		
		print(self.get_computerDtails())
		print(self.get__Desktop_Infor())

	def ShowDetails(self):
		print(
			f"Brand : {self.brand} | Ram: {self.ram}GB | Processor :{self.processor} | Hard Disk: "
			f"{self.hard_dic}GB | Power Bacup:{self.power_bacup} Hourse"
		)

		
lap = Laptop("SONY",12,"Intel CORE i12",360,8)

print(lap.get_computerDtails())
print(lap.get__Desktop_Infor())
lap.ShowDetails()
print(f"\nExternal Resulte, I have a : [{lap.brand}] Computer With: [{lap.ram}GB Ram] and [{lap.hard_dic}GB] Hard dic and Processor[{lap.processor}] Power Bacup :[{lap.power_bacup} Hourse]\n")

lap1 = Laptop("APPLE",8,"Intel CORE i9",556,6)

print(lap1.get_computerDtails())
print(lap1.get__Desktop_Infor())
lap1.ShowDetails()
print(f"\nExternal Resulte, I have a : [{lap1.brand}] Computer With: [{lap1.ram}GB Ram] and [{lap1.hard_dic}GB] Hard dic and Processor[{lap.processor}] Power Bacup :[{lap1.power_bacup} Hourse]\n")
