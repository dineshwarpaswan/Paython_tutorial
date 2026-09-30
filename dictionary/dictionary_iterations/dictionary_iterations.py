print("\nA Dictionary can be iterated using for loop. We can loop through dictionary by keys, values or both.\n")

#1. Add or Modify items: use assign-operator '=' to add/Modify items in a dictionary

# Syntax :  

employee = {
			"Name": "DINESHWAR",
			"Age":"36",
			"Dignation": "ENGINEER",
			"Sallary": 76000,
			1: "Ratu road"
        } # Dictionary

# A. Loop through keys
for key in employee:
	print(key)
print()	

# B. Loop through values
for value in employee:
	print(employee[value])

print()
 
# C. Loop through values: Using values() Method
for value in employee.values():
	print(value)

print()

# D. Loop through Keys: Using keys() Method
for key in employee.keys():
	print(key)

print()
# E. Loop through both key and value : Using items() Method
for key,value in employee.items():
	print(key,value)
