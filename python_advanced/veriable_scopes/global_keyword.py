print("\nPython Variable Scopes: There are two variable scope:- Global scope and Local scope.\n ")
print("Global Keyword:- We can force a local variable to be a global variable by using the global keyword.\n")


def my_name():

	global name   # <--exchange in Global keyword variable
	name = "Dineshwar" 
#   name <--Local Scope variable

	print("\nThis is local variable data: ",name)
	
	global fruits  # <--exchange in Global keyword variable
	fruits = ["Apple","Mango","Banana","Orange"]
#	fruits <--Local Scope variable

	print("\nThis is local variable data: ",fruits) 
	 	
	
my_name()

# name can be used here
print("\nOutside calling local variable helps of Global keyword: ",name) 
# fruits can be used here
print("\nOutside calling local variable helps of Global keyword: ",fruits) 