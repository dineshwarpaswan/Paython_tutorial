print("\nUsing Logical Operators: We can use the and or operators with conditional statement.False.\n")
print("\nThe or operator returns True, if either of the expression(or boolean values) is True.")
# (False or False)= False, (False or True)= True, (True or True)= True

x =10	#Type 1
y = 15
if (x == 10) or (y ==10): 
	print("Type 1, If either conditional is correct,print will be True")# IF  either expression is correct, print will be :True
	
fruit = "Apple"	    # Type 2,
name = "Dineshar"
	
if (fruit == "Apple" or name == "Dineshar"):
	print("\nType 2, both data is matched")# IF both  or any one conditional is correct, print will be :True
	

if (fruit == "Apple" or name == "Dine"):
	print("\nType 2, both any one data is matched")# IF   both any one conditional is correct, print will be :True



if (fruit == "Appl") or (name == "Dine"):
	print("\nType 2, IF both or any one expression is correct")# IF both any one conditional is correct, print will be :True
	
else:
	print("Type 2,IF Either not any data is matched") # IF  either not any conditional is correct, print will be :False



if (5>4) or (6<10): #Type 3
	print("\nType 3,IF both conditional is correct,") # IF both OR any one conditional is correct, print will be :True

x4 = 100
if (x4 > 10) or (50 < x4):   # Type 4
	print("Type 4, IF both conditional is correct")  # IF both OR any one conditional is correct, print will be :True
	
a =  (4 > 5) or (5 < 3) # Type 5
print("Type 5:", a)  #if either not any conditional is correct, print will be :False

a1 = (15 == 15) or (10 == 10) # Type 6
print("Type 6:", a1) # IF both OR any one conditional is correct, print will be :True

a2 = (15 == 5) or (10 == 1) # Type 7
print("Type 7:", a2) # IF both OR any one conditional is correct, print will be :True
