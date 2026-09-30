print("\nTHE RETURN STATEMENT FUNCTION: The Return statement is used function caller.\n")
#type 1
def add_value(num1, num2):
	sum = num1 + num2
	return sum
	
print("Totale Sum:",add_value(50, 20)) # calling the funtion
print("Totale sum:",add_value("Apple", " Fruit")) # calling the funtion
print("Totale Sum:",add_value(2.05, 5.45)) # calling the funtion

#type 2
print("\nType 2 THE RETURN STATEMENT.\n")

def add(a, b):
	c = a * b
	return c
x = add(2,3)
x1 = add(4,4)
x2 = add(4,5)
x3 = add(5,6) # object calling the funtion
 
print("Multiply 2 * 3: ", x) # object will br print
print("Multiply 4 * 4: ", x1)
print("Multiply 4 * 5: ", x2)
print("Multiply 5 * 6: ", x3)
	