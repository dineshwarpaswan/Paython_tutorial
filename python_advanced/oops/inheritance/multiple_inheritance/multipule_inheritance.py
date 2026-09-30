print("\nPython Multiple Inheritance:- inheritance feature that allows us to create a class that inherits the attributes(or properties) and methods of another class\n")
#   class A: 	<-- Super class/Paraint class
#		....
#
#   class B:    class/Super childe class 1 <--Used properties and methods of Super class
#     ......
#   class C(A,B):   Base/Childe class  <--Used properties and methods of Super class
#      ------

class Computer:
	def __init__(self,brand, ram):
		self.brand = brand
		self.ram = ram
		print(f"I have a : [{self.brand}] Computer With: [{self.ram}GB Ram]")	
class Desktop:
	def __init__(self, hard_dic):
		self.hard_dic = hard_dic
		print(f"I have a : [{self.brand}] Desktop With: [{self.ram}GB Ram] and [{self.hard_dic}GB] Hard dic")	

class Laptop(Computer, Desktop):
	def __init__(self,brand, ram, hard_dic, mode):
		Computer.__init__(self,brand, ram)
		Desktop.__init__(self, hard_dic)
		self.mode = mode
		print(f"I have a System of : [{self.brand}] brand  With: [{self.ram}GB Ram] and [{self.hard_dic}GB] Hard dic and [{self.mode}] Charjeble]")

		
lap = Laptop("SONY",8,360,"Electricity")
print(f"External Resulte, I have a : [{lap.brand}] Computer With: [{lap.ram}GB Ram] and [{lap.hard_dic}GB] Hard dic and [{lap.mode}] Charjeble]\n")

lap1 = Laptop("APPLE",10,556,"Power Less")
print(f"External Resulte, I have a : [{lap1.brand}] Computer With: [{lap1.ram}GB Ram] and [{lap1.hard_dic}GB] Hard dic and [{lap1.mode}] Charjeble]")
