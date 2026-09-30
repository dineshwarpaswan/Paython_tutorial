print("\n USING INDEXES:-We can use index numbers to specify exactly where the value should be placed. The index number should be inside the curly bracket{index_number}.\n")  

fruits = "Apple {2} Banana {1} Greps {0} Naspati"
frt = fruits.format("Mango","Orange","Lichi")
	
print("This IS Formating:",frt) 

TX = "I Love {2}, {1} AND {0} Very Much!"

T = TX.format("PYTHON", "JAVASCRIPT", "HTML")

print("\nEXAMPLE 1:",T)

x = "This is my fevrate {0}, {1} and {2}"
taxt =x.format("FRUIT","MANGO","BANANA")

print("\nEXAMPLE 2: ",taxt)
