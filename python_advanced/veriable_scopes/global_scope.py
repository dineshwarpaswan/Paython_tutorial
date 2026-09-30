print("\nPython Variable Scopes: There are two variable scope:- Global scope and Local scope.\n ")
print("Global Scope:- A variable that is defined(create) outside a function has a global scope. A global variable can be used anywhere in the program!\n")

name = "Dineshwar" 
# name <--Global Scope variable
print(name)

fruits = ["Apple","Mango","Banana","Orange"]
# fruits <--Global Scope variable

def my_name():

	print("\nThis is a global data of Fruits:",fruits) # <- calling Global Scope variable
	
	print(name) # <- calling Global Scope variable
	
my_name()