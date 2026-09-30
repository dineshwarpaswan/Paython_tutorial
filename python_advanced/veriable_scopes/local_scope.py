print("\nPython Variable Scopes: There are two variable scope:- Global scope and Local scope.\n ")
print("Local Scope:- A variable that is defined(create) inside a function has a local scope. A local variable can be used only inside the function!\n")




def my_name():

	name = "Dineshwar" 
#   name <--Local Scope variable
	print(name)
	
	fruits = ["Apple","Mango","Banana","Orange"]
#	fruits <--Local Scope variable

	print("\nThis is local variable data:",fruits) 
	 	
	
my_name()
print("")
# name can Not be used here
print(name) # <---if you calls local variable, result will be: error
# fruits can Not be used here
print(fruits) #  <---if you calls local variable, result will be: error