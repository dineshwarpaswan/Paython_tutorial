print(" Multi level Inheritance:- one chield to another chield Inherita!\n")

# Syntax:
#  class A:
#    ------
#  class B(A):
#    -----
#   class C(B):
#		-----
class CarA:
	car_a = "HONDA CITY"
	print("\nMy febrate of  CarA: ",car_a)
	
class CarB(CarA):
	Supper().__init__()
	pass
        car_b = "TOYOTA"
        print("\nMy febrate of  CarB: ",car_b)
class CarC(CarB):
	Supper().__init__()
	pass
	car_c = "THAR"
	print("\nMy febrate of  CarC: ",car_c)

obj = CarC()
obj.car_a()
obj.car_b()
obj.car_c()
		
