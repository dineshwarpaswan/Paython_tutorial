print("\nWe can Add, Modify and Remove items in Dictionary.\n")

# 1.Add or Modify items: use assign-operator '=' to add/Modify items in a dictionary

# Syntax :  
#  employee["key-name"] = "value-name"

employee = {
			"Name": "DINESHWAR",
			"Age":"36",
			"Dignation": "ENGINEER",
			"Sallary": 76000,
			1: "Ratu road"
        } # Dictionary



print("\nDictionary",employee) 	# dictionary

#  Adding a new key-value pair
employee["mobile"] = 8776555567
print("\nAdding a new kye-value in Dictionary:",employee) 	# Adding a new kye-value in dictionary

# Modifying on existing value
employee["Age"] = 30
print("\nModifying Age-value in Dictionary:",employee) 	# Modifying Age-value in dictionary


# 2.Remove item: use del or pop() to remove items from a dictinary.
#   del employee["key-name"]
#   Removed with del 
del employee["Sallary"] #<------- --------but key-name and value-name delete in pair

print("\nSallary is delet for Dictionary:",employee) 	# dictionary

# Remove with pop() and store the removed value
emp = employee.pop("Age")   #<------- --------but key-name and value-name delete in pair
print("Age delet for dictionary:",emp) 
print("Dictionary",employee) 	# dictionary
 
