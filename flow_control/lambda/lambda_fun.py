print("\nLAMBDA FUNCTIONS : The body of a lambda function can only have one expression, but can have multiple arguments. The result of the expression is automatically returned.\n")

# simple function
print("\nThis function has a very simple task, add two numbers.\n")

def add_value(x, y):
	return x + y
	
print(add_value(50, 20)) # calling the funtion, print: 70
print("Totale Sum:",add_value(20.05, 30.45)) # calling the funtion

#Type 1
print("\nType 1, THIS IS LAMBDA VERSION BELOW.\n")
# Syntex below:
# lambda arguments: experession
add = lambda a, b: a + b
	
print(add(20,30)) # calling the lambda funtion , print will be a+b : 50
print("Add 2 number of 40.05 + 45: ", add(40.05,45))  # calling the lambda funtion, print will be a+b : 85.05
print("Add 2 number of 50.45 + 6.20: ", add(50.45,6.20)) # calling the lambda funtion
 

#Type 2
print("\n Type 2, THIS IS LAMBDA VERSION BELOW.\n")

mul = lambda a, b: a * b
	
x = mul(2,3)
x1 = mul(4,4)
x2 = mul(4,5)
x3 = mul(5,6) # object calling the lambda funtion
 
print("Multiply 2 * 3: ", x) # object will br print
print("Multiply 4 * 4: ", x1)
print("Multiply 4 * 5: ", x2)
print("Multiply 5 * 6: ", x3)


	