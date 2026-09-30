print("\nPython program to a simple Calclator.\n")

#1 Python program to a simple Calclator
#2 functin used for operation
#3 user input 
#4 type casting
#5 print result
#6 used if..elif
 
# STEP 1:
# Function to addition  two numbers
def addition(num1, num2):
	return num1 + num2
	
# Function to substract  two numbers	
def substract(num1, num2):
	return num1 - num2
	
# Function to multiply  two numbers	
def multiply(num1, num2):
	return num1 * num2
	
# Function to division  two numbers	
def division(num1, num2):
	return num1 / num2
	
# Function to avrage  two numbers	
def avrage(num1, num2):
	return (num1 + num2)/2
	
# Step 2: user input	
print("Please Selsect an Operation:\n" \
	"0.Addition\n"\
	"1.Substracion\n"\
	"2.Multiply\n"\
	"3.Division\n"\
	"4.Avarage\n")

try:
	choice = int(input("Please enter the number (0,1,2,3,4) here: "))
	if not(choice<4): print("Please Enter the Choice number!(0,1,2,3,4)!") 
	
	try:
		num1 = int(input("ENTER THE FIRST VALUE:"))
		num2 = int(input("ENTER THE SECOND VALUE:"))
		if choice == 0: print("Sum of two numbere:",num1,"+", num2,"=", addition(num1, num2))
			
		elif choice== 1: print("Substarct of two numbere:",num1,"-", num2,"=", substract(num1, num2))
			
		elif choice== 2: print("Multipliction of two numbere:",num1,"*", num2,"=", multiply(num1, num2))

		elif choice== 3: print("Division of two numbere:",num1,"/", num2,"=", division(num1, num2))
			
		elif choice== 4: print("Avrage of two numbere:","(", num1,"+", num2,")","/","2","=", avrage(num1, num2))
		else: 
			print("Invalid Operational!")
	except ValueError: print("Invalid Operational, Please Only For Number!")
	except ZeroDivisionError: print("Invalid Operational, Please Only For Number!")
except ValueError: print("Invalid Operational, Please Only For Number!")
	

#try:
	#age = int(input("Please enter the Age here: "))
	#print("Your Age:", age)
	
#except ValueError:
#	print("Please enter the number!")       
	
#finally:
#	print("\nCode execution, Thanku!") # execution<-- pura ho gaya/Samapt ho gaya
