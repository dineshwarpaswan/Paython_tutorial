print("Multiple Inheritance:- one chield to another chield Inherita!\n")

# Syntax:
#  class A:
#    ------
#  class B:
#    -----
#   class C(A,B):
#		-----
class A:
	a = "WELLCOME to class A"
	print("My febrate of  Car A: ",a)
	
class B:
	b = "WELLCOME to class B"
	print("My febrate of  Car B: ",b)
class C(A, B):
	c = "WELLCOME to class C"
	print("My febrate of  Car C: ",c)

ob = C()
print("*******************")

print("My febrate of  Car A: ",ob.a)
ob.a ="HONDA CITY" # <---class propertis will be updat hare
print("My febrate of  Car A: ",ob.a)

print("My febrate of  Car B: ",ob.b)
ob.b ="TOYOTA"
print("My febrate of  Car B: ",ob.b) # <---class propertis will be updat hare

print("My febrate of  Car C: ",ob.c)
ob.c ="Thar"
print("My febrate of  Car C: ",ob.c) # <---class propertis will be updat hare

print("\nUpdate here bellow:-")
print(ob.a)
print(ob.b)
print(ob.c)

		
