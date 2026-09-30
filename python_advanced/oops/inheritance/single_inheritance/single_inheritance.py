print("\nPython Single Inheritance:- inheritance feature that allows us to create a class that inherits the attributes(or properties) and methods of another class\n")

#   class A: 	<-- Super class/Paraint class
#		....
#
#   class B(A):   Base class/childe class <--Used properties and methods of Super class
#       .....

class Car: # Parent class name
	def __init__(self,name,color,speed): # initialise ya cunstuctor
		self.name = name            # attributes
		self.color = color	   # attributes
		self.speed = speed
		
	def start(self):
		
		print(f"My :[{self.name}] Car is Started and My choice color: [{self.color}] is beautifull!")
		
	def stop(self):
		
		print(f"My :[{self.name}] Car is Stoped, Because no feeul!")
		
class Supercar(Car): # child class name
	def __init__(self,name,color,speed,map):
                
		super().__init__(name,color,speed) # super class used<-- call kiya gya hai parait class ka atrributes inherit ke liye
		self.map = map
		
		print(f"\nName of Car :[{self.name}], and Top Car High speed [{self.speed}] K/m 1 houre!  Choice Color [{self.color}] your location:[{self.map}]")
		

sup = Supercar("Honda City", "Red", 150,"Bokaro") #<-instantiating class11
sup.start() # object method class
sup.stop()

print(f"\nExtrnal 1 Result Print Here NAME OF CAR: {sup.name} COLOR: {sup.color} SPEED OF CAR :{sup.speed} LOCATON :{sup.map}")

Sup1 =Supercar("TOYOTA","BLUE",155,"Mumbai")# <-instantiating class 2
Sup1.stop() # object method class
Sup1.start()
print("\nExtrnal 2 Result Print Here: ",Sup1.name,Sup1.color, Sup1.speed, Sup1.map)

car = Supercar("THAR","Black",180, "Delhi") #<-instantiating class 3
car.start() # object method class
car.stop()
print("\nExtrnal 3 Result Print Here: ", car.name, car.color, car.speed, car.map)
