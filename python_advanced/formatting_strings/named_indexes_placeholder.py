print("\nUSING NAMED INDEXES:-We can also use named indexes to specify exactly where the value should be placed. The arguments of the format() function shoud be key/value pairs i.e. key = value.  The key/value pairs should be placed seprated by commas. \n")  

fruits = "This is a louds of fruits like:- {fruit} Banana {fruit1} Greps {fruit2} Naspati"

frt = fruits.format(fruit = "Mango", fruit1 = "Orange",fruit2 = "Lichi")
	
print("\nType 1:",frt)

x = "The Color of {fruit} is {color} and my fevarate vegetable {veg} and {veg1}"

taxt = x.format(fruit = "MANGO", color = "yellow", veg = "POTATO", veg1 = "TOMATO")

print("\nType 2:",taxt)