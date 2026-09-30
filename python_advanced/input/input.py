print("\nPython user input: in pythaon interactive mode, we can ask and get a user input. The input() function takes an input from the user.\n")
#type 1

num = int(input("Type 1 , Please enter the Age here(no Vailidation): "))
print("\nYour Age:",num)

#type 2 with vailidation
try:
	age = int(input("\nType 2,Please enter the Age here( with Vailidation): "))
	print("\nYour Age:", age)
	
except ValueError:
	print("\nNot Characture, only for Please Enter the Number!")
	
finally:
	print("\nCode execution, Thanku!") # execution<-- pura ho gaya/Samapt ho gaya
