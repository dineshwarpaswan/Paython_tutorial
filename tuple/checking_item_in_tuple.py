print("\nCheaking if an item Exists in Tuple.\n")

brand = ("Leptop","Mobile","Desktop","Moniter") # string data in Tuple
print("Print will be Tuple:",brand) # print will be Tuple
print()
print("Mobile" in brand) # TYPE 1, Cheaking if an item Exists: True	
print("SMART TV" in brand) # TYPE 1, Cheaking if item not Exists in Tuple, print will be: False 


if "Desk" in brand:     # TYPE 2
   print("Yes") #  Cheaking if an item Exists: Yes
else:
    print("\nNo Exists") # if item not Exists in Tuple, print will be: No Exists 
	
	
if "Moniter" in brand:     # TYPE 3
   print("Yes") #  Cheaking if an item Exists: Yes


print("ANOTHER WAY TO CREATE A TUPLE BELLOW:-Another way to create a tuple is  to use  the tuple()  Constructor.") 

brand = tuple(("Leptop","Mobile","Desktop","Moniter","Computer")) # Take note of the double brackets
print("Print will be Tuple:",brand) # print will be Tuple