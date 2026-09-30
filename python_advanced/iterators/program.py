print("\nPython me Iterator ya Dictionary se data fetch kanrne ka alag-alag tarika hota hai.\n")

mixture = {"Fruit": "APPLE", "Vegetable": "Potato", "Groseiry": "Bred", "Liquid": "Milk"} # Dict
   # iterator/iterable <--- ka matalb hai ki ak-ak kr ke data nikalana ak bag se kuch object

# Type 1
print("Iterator Type 1: ", mixture["Fruit"]) 
print("Iterator Type 1: ", mixture["Vegetable"]) 
print("Iterator Type 1: ", mixture["Groseiry"])
print("Iterator Type 1: ", mixture["Liquid"])
print()

# Type 2
print("Iterator Type 2: ", mixture.get("Fruit"))
print("Iterator Type 2: ", mixture.get("Vegetable")) 
print("Iterator Type 2: ", mixture.get("Groseiry"))
print("Iterator Type 2: ", mixture.get("Liquid"))
print()


# Type 3
for	all in mixture.items():
	print("Iterator Type 3, print will be in pairs: ", all) # print will be: in tuple
	
print()	

# Type 4
for key in mixture:
	print("Iterator Type 4, key_name: ", key) # print will be: key_name of Dictionary

print()	

# Type 5
for value in mixture.values():
	print("Iterator Type 5, key_vlue: ", value) # print will be : key_value of Dictionary

print()	

# Type 6
for key, value in mixture.items():
	print(f"Iterator Type 6 : {key} : {value}") # print will be: in pairs
	
print()
print("Iterator Type 7: ", mixture.keys())
print()
print("Iterator Type 8: ", mixture.values())
