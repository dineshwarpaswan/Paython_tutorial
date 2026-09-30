print("\nDEFULT PARAMETERS/ARGUMENTS VARIABLE FUNCTION:-If you don't pass the argument,  when the defult argument will be used instead. assignment operator(=)\n")
# TYPE 1
def my_func(name = "Rubi", age = "35", city = "PATNA"): # defult parameter/argument pass variable data
	names = "My name is : " + name +" "+ age + " year old mane and live form " + city
	print("\n",names)
	
my_func("DINESHWAR") #  Recive will be Defult argument step by step pass
my_func()
my_func("MAHENDR SINHA","40")
my_func("SUDHIR KUMAR","50")

# TYPE 2
def emp_fun( dign= "Enginer",int ="50000"):
	x = "I AM : " + dign + " AND My Sallary : " + int
	print("\n", x)
	
emp_fun() # Recive will be Defult argument step by step pass
emp_fun("DOCTOR")
emp_fun("MANAGER","78000")
emp_fun("AVOCATE","80500")