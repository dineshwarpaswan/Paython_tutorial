print("\nMULTIPLE PARAMETER/ARGUMENT VARIABLE FUNCTION PASS IN BELLOW:-\n")
# TYPE 1
def my_func(name, age, city): #parameter/argument pass variable
	names = "My name is : " + name +" "+ age + " year old mane and live form " + city
	print("\n",names)
	
my_func("DINESHWAR PASWAN","30","BOKARO") # argument pass variable data
my_func("SUDHIR SINHA","40","RANCHI")     
my_func("NARAYAN SARAM","56","TATA")
my_func("BINOD KUMAR","50","DANBAD")


# TYPE 2
def my_fun(a, b):  #parameter/argument pass variable
	c = a + b
	print("\nTotale: ",c)
	
	
# Two argument are required, But only one is passed
my_fun(40,50)  # argument pass variable data
my_fun(20,10)
my_fun(15,2.50)
my_fun(4.25,5.75)
my_fun(20)